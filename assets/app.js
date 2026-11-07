(() => {
  'use strict';

  const data = window.ECE_DATA;
  if (!data || !Array.isArray(data.subjects)) {
    document.body.innerHTML = '<main style="max-width:680px;margin:10vh auto;padding:24px;font:16px system-ui"><h1>Formula library unavailable</h1><p>The catalogue file could not be loaded. Make sure <code>assets/js/catalog.js</code> is present in the repository.</p></main>';
    return;
  }

  const $ = (selector) => document.querySelector(selector);
  const els = {
    heroStats: $('#heroStats'), catalogCount: $('#catalogCount'), search: $('#searchInput'), clear: $('#clearSearch'),
    searchHint: $('#searchHint'), semester: $('#semesterFilter'), subjectList: $('#subjectList'),
    subjectResultsTitle: $('#subjectResultsTitle'), subjectResultCount: $('#subjectResultCount'),
    emptyDetail: $('#emptyDetail'), subjectDetail: $('#subjectDetail'), detailOverline: $('#detailOverline'),
    detailTitle: $('#detailTitle'), detailMeta: $('#detailMeta'), detailSave: $('#detailSave'),
    subjectNote: $('#subjectNote'), unitGrid: $('#unitGrid'), unitTotal: $('#unitTotal'),
    selectedUnitLabel: $('#selectedUnitLabel'), selectedUnitTitle: $('#selectedUnitTitle'),
    selectedUnitTopics: $('#selectedUnitTopics'), formulaCount: $('#formulaCount'), formulaList: $('#formulaList'),
    savedToggle: $('#savedToggle'), savedCount: $('#savedCount'), themeToggle: $('#themeToggle'),
    resetFilters: $('#resetFilters'), printUnit: $('#printUnit'), toast: $('#toast')
  };

  const state = {
    year: 'all', semester: 'all', query: '', savedOnly: false,
    selectedId: null, unitIndex: 0, saved: loadSaved(), toastTimer: null
  };

  function loadSaved() {
    try {
      const value = JSON.parse(localStorage.getItem('ece-vault-saved') || '[]');
      return new Set(Array.isArray(value) ? value.filter(v => typeof v === 'string') : []);
    } catch (_) { return new Set(); }
  }

  function persistSaved() {
    try { localStorage.setItem('ece-vault-saved', JSON.stringify([...state.saved])); }
    catch (_) { showToast('Browser storage is unavailable'); }
  }

  function normalize(value) {
    return String(value ?? '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  }

  function byId(id) { return data.subjects.find(subject => subject.id === id) || null; }

  function countFormulas(subject) {
    return subject.units.reduce((sum, unit) => sum + unit.formulas.length, 0);
  }

  function countAllFormulas() {
    return data.subjects.reduce((sum, subject) => sum + countFormulas(subject), 0);
  }

  function subjectMatches(subject, query) {
    if (!query) return { match: true, unitIndex: 0, formulaMatches: 0 };
    const q = normalize(query);
    const core = normalize(`${subject.name} ${subject.code} ${subject.category} ${subject.semester} year ${subject.year}`);
    if (core.includes(q)) return { match: true, unitIndex: 0, formulaMatches: 0 };

    const unitNumber = q.match(/^(?:unit\s*)?(\d+)$/);
    const romanNumber = q.match(/^unit\s*(i{1,3}|iv|v)$/);
    let desiredUnit = null;
    if (unitNumber) desiredUnit = Math.max(1, Math.min(5, Number(unitNumber[1]))) - 1;
    if (romanNumber) {
      const roman = { i: 1, ii: 2, iii: 3, iv: 4, v: 5 };
      desiredUnit = roman[romanNumber[1]] - 1;
    }
    if (desiredUnit !== null && subject.units[desiredUnit]) return { match: true, unitIndex: desiredUnit, formulaMatches: 0 };

    let formulaMatches = 0;
    for (let i = 0; i < subject.units.length; i += 1) {
      const unit = subject.units[i];
      if (normalize(`${unit.title} ${unit.topics} unit ${i + 1}`).includes(q)) {
        return { match: true, unitIndex: i, formulaMatches };
      }
      const found = unit.formulas.some(formula => {
        const formulaText = normalize(`${formula.name} ${formula.formula} ${formula.variables} ${formula.note}`);
        if (formulaText.includes(q)) { formulaMatches += 1; return true; }
        return false;
      });
      if (found) return { match: true, unitIndex: i, formulaMatches };
    }
    return { match: false, unitIndex: 0, formulaMatches };
  }

  function filteredSubjects() {
    return data.subjects.filter(subject => {
      if (state.year !== 'all' && String(subject.year) !== state.year) return false;
      if (state.semester !== 'all' && subject.semester !== state.semester) return false;
      if (state.savedOnly && !state.saved.has(subject.id)) return false;
      return subjectMatches(subject, state.query).match;
    });
  }

  function createStarSvg() {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', '0 0 24 24');
    svg.setAttribute('aria-hidden', 'true');
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('d', 'm12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3l-5.6 2.9 1.1-6.2L3 9.6l6.2-.9L12 3Z');
    svg.appendChild(path);
    return svg;
  }

  function setSaved(subjectId) {
    if (state.saved.has(subjectId)) state.saved.delete(subjectId);
    else state.saved.add(subjectId);
    persistSaved();
    renderSavedControls();
    renderSubjectList();
    const selected = byId(state.selectedId);
    if (selected) renderDetail(selected);
    showToast(state.saved.has(subjectId) ? 'Subject saved' : 'Subject removed from saved');
  }

  function renderSavedControls() {
    els.savedCount.textContent = String(state.saved.size);
    els.savedToggle.setAttribute('aria-pressed', String(state.savedOnly));
    const subject = byId(state.selectedId);
    const isSaved = subject ? state.saved.has(subject.id) : false;
    els.detailSave.classList.toggle('saved', isSaved);
    els.detailSave.setAttribute('aria-pressed', String(isSaved));
    els.detailSave.setAttribute('aria-label', isSaved ? 'Remove saved subject' : 'Save subject');
  }

  function renderStats() {
    const unitCount = data.subjects.reduce((sum, s) => sum + s.units.length, 0);
    els.heroStats.textContent = `${data.subjects.length} subjects  ·  ${unitCount} units  ·  ${countAllFormulas()} formulas`;
    els.catalogCount.textContent = `${data.subjects.length} subjects`;
  }

  function renderSubjectList() {
    const visible = filteredSubjects();
    els.subjectResultCount.textContent = String(visible.length);
    if (state.savedOnly) els.subjectResultsTitle.textContent = 'Saved subjects';
    else if (state.query) els.subjectResultsTitle.textContent = 'Search results';
    else if (state.year !== 'all') els.subjectResultsTitle.textContent = `${ordinal(state.year)} year subjects`;
    else els.subjectResultsTitle.textContent = 'All subjects';

    els.subjectList.replaceChildren();
    if (!visible.length) {
      const empty = document.createElement('div');
      empty.className = 'empty-list';
      const title = document.createElement('strong');
      title.textContent = state.savedOnly ? 'No saved subjects yet' : 'No matching subjects';
      const text = document.createElement('span');
      text.textContent = state.savedOnly ? 'Tap the star on a subject to keep it here.' : 'Try another subject, unit title or formula keyword.';
      empty.append(title, text);
      els.subjectList.appendChild(empty);
      return;
    }

    visible.forEach(subject => {
      const match = subjectMatches(subject, state.query);
      const card = document.createElement('div');
      card.className = 'subject-card' + (subject.id === state.selectedId ? ' selected' : '');
      const openButton = document.createElement('button');
      openButton.type = 'button';
      openButton.className = 'subject-card-open';
      openButton.setAttribute('aria-pressed', String(subject.id === state.selectedId));
      openButton.setAttribute('aria-label', `Open ${subject.name}`);
      openButton.addEventListener('click', () => selectSubject(subject.id, state.query ? match.unitIndex : 0));

      const year = document.createElement('span');
      year.className = 'subject-year';
      year.textContent = `Y${subject.year}`;
      const main = document.createElement('span');
      main.className = 'subject-card-main';
      const name = document.createElement('span');
      name.className = 'subject-card-name';
      name.textContent = subject.name;
      const meta = document.createElement('span');
      meta.className = 'subject-card-meta';
      const code = document.createElement('span'); code.textContent = subject.code;
      const dot = document.createElement('span'); dot.className = 'dot'; dot.textContent = '•';
      const sem = document.createElement('span'); sem.textContent = subject.semester;
      meta.append(code, dot, sem);
      if (state.query) {
        const hit = document.createElement('span'); hit.textContent = `Unit ${match.unitIndex + 1}`;
        meta.append(dot.cloneNode(true), hit);
      }
      main.append(name, meta);
      openButton.append(year, main);

      const star = document.createElement('button');
      star.type = 'button';
      star.className = 'subject-card-star' + (state.saved.has(subject.id) ? ' saved' : '');
      star.appendChild(createStarSvg());
      star.setAttribute('aria-pressed', String(state.saved.has(subject.id)));
      star.setAttribute('aria-label', state.saved.has(subject.id) ? 'Remove from saved' : 'Save subject');
      star.title = state.saved.has(subject.id) ? 'Remove saved subject' : 'Save subject';
      star.addEventListener('click', (event) => { event.stopPropagation(); setSaved(subject.id); });
      card.append(openButton, star);
      els.subjectList.appendChild(card);
    });
  }

  function ordinal(n) {
    return ({ '1': 'First', '2': 'Second', '3': 'Third', '4': 'Fourth' })[String(n)] || `${n}th`;
  }

  function selectSubject(subjectId, unitIndex = 0, updateUrl = true) {
    const subject = byId(subjectId);
    if (!subject) return;
    state.selectedId = subjectId;
    state.unitIndex = Math.max(0, Math.min(subject.units.length - 1, Number(unitIndex) || 0));
    renderSubjectList();
    renderDetail(subject);
    renderSavedControls();
    if (updateUrl) {
      const url = new URL(window.location.href);
      url.searchParams.set('subject', subject.id);
      url.searchParams.set('unit', String(state.unitIndex + 1));
      history.replaceState(null, '', url.toString());
    }
    if (window.matchMedia && window.matchMedia('(max-width: 700px)').matches) {
      $('#detailPanel').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  function createUnitButton(unit, index, subject) {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'unit-button' + (index === state.unitIndex ? ' active' : '');
    button.setAttribute('aria-pressed', String(index === state.unitIndex));
    const number = document.createElement('span'); number.className = 'unit-number'; number.textContent = `UNIT ${String(index + 1).padStart(2, '0')}`;
    const title = document.createElement('span'); title.className = 'unit-name'; title.textContent = unit.title;
    const count = document.createElement('span'); count.className = 'unit-formula-total'; count.textContent = `${unit.formulas.length} formulas`;
    button.append(number, title, count);
    button.addEventListener('click', () => {
      state.unitIndex = index;
      renderDetail(subject);
      renderSubjectList();
      const url = new URL(window.location.href);
      url.searchParams.set('subject', subject.id);
      url.searchParams.set('unit', String(index + 1));
      history.replaceState(null, '', url.toString());
    });
    return button;
  }

  function createCopySvg() {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', '0 0 24 24'); svg.setAttribute('aria-hidden', 'true');
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttribute('d', 'M8 8V5a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2h-3M5 8h9a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2Z');
    svg.appendChild(path); return svg;
  }

  function createFormulaCard(formula, index) {
    const card = document.createElement('article');
    card.className = 'formula-card';
    const top = document.createElement('div'); top.className = 'formula-top';
    const name = document.createElement('div'); name.className = 'formula-name'; name.textContent = formula.name || 'Formula';
    const number = document.createElement('span'); number.className = 'formula-index'; number.textContent = `F${String(index + 1).padStart(2, '0')}`;
    top.append(name, number);

    const expression = document.createElement('code');
    expression.className = 'formula-expression';
    expression.textContent = formula.formula;

    const bottom = document.createElement('div'); bottom.className = 'formula-bottom';
    const variables = document.createElement('div'); variables.className = 'formula-variables';
    variables.textContent = formula.variables ? `Where: ${formula.variables}` : 'Standard relation';
    const copy = document.createElement('button'); copy.type = 'button'; copy.className = 'copy-button';
    copy.append(createCopySvg(), document.createTextNode('Copy'));
    copy.addEventListener('click', () => copyText(`${formula.name}\n${formula.formula}${formula.variables ? `\n${formula.variables}` : ''}${formula.note ? `\nCondition: ${formula.note}` : ''}`));
    bottom.append(variables, copy);
    card.append(top, expression, bottom);

    if (formula.note) {
      const note = document.createElement('div'); note.className = 'formula-note'; note.textContent = `Condition: ${formula.note}`;
      card.appendChild(note);
    }
    return card;
  }

  function renderDetail(subject) {
    els.emptyDetail.hidden = true;
    els.subjectDetail.hidden = false;
    els.detailOverline.textContent = `${subject.category.toUpperCase()} · YEAR ${subject.year}`;
    els.detailTitle.textContent = subject.name;
    els.detailMeta.textContent = `${subject.code}  ·  ${subject.semester}  ·  ${subject.units.length} units`;
    els.subjectNote.hidden = !subject.note;
    els.subjectNote.textContent = subject.note || '';
    els.unitTotal.textContent = `${subject.units.length} units`;
    els.unitGrid.replaceChildren();
    subject.units.forEach((unit, index) => els.unitGrid.appendChild(createUnitButton(unit, index, subject)));

    const unit = subject.units[state.unitIndex];
    if (!unit) return;
    els.selectedUnitLabel.textContent = `UNIT ${String(state.unitIndex + 1).padStart(2, '0')}`;
    els.selectedUnitTitle.textContent = unit.title;
    els.selectedUnitTopics.textContent = unit.topics || '';
    els.formulaCount.textContent = `${unit.formulas.length} formulas`;
    els.formulaList.replaceChildren();
    if (!unit.formulas.length) {
      const empty = document.createElement('div'); empty.className = 'no-formulas';
      empty.textContent = 'No fixed equation cards are listed for this unit. Use the unit topics as a guide and check your prescribed text for course-specific relations.';
      els.formulaList.appendChild(empty);
    } else {
      unit.formulas.forEach((formula, index) => els.formulaList.appendChild(createFormulaCard(formula, index)));
    }
  }

  async function copyText(text) {
    try {
      if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(text);
      else {
        const field = document.createElement('textarea');
        field.value = text; field.style.position = 'fixed'; field.style.opacity = '0';
        document.body.appendChild(field); field.select();
        const ok = document.execCommand('copy'); field.remove();
        if (!ok) throw new Error('Copy command failed');
      }
      showToast('Formula copied');
    } catch (_) { showToast('Copy unavailable on this browser'); }
  }

  function showToast(message) {
    els.toast.textContent = message;
    els.toast.classList.add('show');
    if (state.toastTimer) clearTimeout(state.toastTimer);
    state.toastTimer = setTimeout(() => els.toast.classList.remove('show'), 1900);
  }

  function renderAll() {
    state.query = els.search.value.trim();
    els.clear.hidden = !state.query;
    els.searchHint.textContent = state.query ? 'Search checks subject names, unit headings, formula names and equations.' : 'Try “Fourier”, “Unit III”, “BJT” or “Shannon capacity”.';
    renderSubjectList();
    renderSavedControls();
  }

  function setYear(year) {
    state.year = year;
    document.querySelectorAll('.filter-chip').forEach(button => {
      button.classList.toggle('active', button.dataset.year === year);
      button.setAttribute('aria-pressed', String(button.dataset.year === year));
    });
    renderAll();
  }

  document.querySelectorAll('.filter-chip').forEach(button => {
    button.addEventListener('click', () => setYear(button.dataset.year));
  });
  els.search.addEventListener('input', renderAll);
  els.clear.addEventListener('click', () => { els.search.value = ''; renderAll(); els.search.focus(); });
  els.semester.addEventListener('change', () => { state.semester = els.semester.value; renderAll(); });
  els.resetFilters.addEventListener('click', () => {
    state.year = 'all'; state.semester = 'all'; state.query = ''; state.savedOnly = false;
    els.search.value = ''; els.semester.value = 'all';
    document.querySelectorAll('.filter-chip').forEach(button => {
      const active = button.dataset.year === 'all';
      button.classList.toggle('active', active); button.setAttribute('aria-pressed', String(active));
    });
    renderAll();
  });
  els.savedToggle.addEventListener('click', () => {
    state.savedOnly = !state.savedOnly;
    if (state.savedOnly) {
      state.year = 'all'; state.semester = 'all';
      els.semester.value = 'all';
      document.querySelectorAll('.filter-chip').forEach(button => {
        const active = button.dataset.year === 'all'; button.classList.toggle('active', active);
        button.setAttribute('aria-pressed', String(active));
      });
    }
    renderAll();
  });
  els.detailSave.addEventListener('click', () => { if (state.selectedId) setSaved(state.selectedId); });
  els.printUnit.addEventListener('click', () => window.print());

  function setTheme(theme) {
    document.documentElement.dataset.theme = theme;
    try { localStorage.setItem('ece-vault-theme', theme); } catch (_) { /* theme still works for this session */ }
    els.themeToggle.setAttribute('aria-label', theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
    els.themeToggle.title = theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme';
  }
  let initialTheme = 'light';
  try { initialTheme = localStorage.getItem('ece-vault-theme') || 'light'; } catch (_) { /* ignore */ }
  setTheme(initialTheme === 'dark' ? 'dark' : 'light');
  els.themeToggle.addEventListener('click', () => setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'));

  document.addEventListener('keydown', event => {
    if (event.key === '/' && !['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)) {
      event.preventDefault(); els.search.focus();
    }
    if (event.key === 'Escape' && document.activeElement === els.search && els.search.value) {
      els.search.value = ''; renderAll();
    }
  });

  // Restore a subject/unit from a shareable URL, if one was supplied.
  const params = new URLSearchParams(window.location.search);
  const initialSubject = params.get('subject');
  const initialUnit = Math.max(1, Number(params.get('unit')) || 1) - 1;
  renderStats();
  renderAll();
  if (initialSubject && byId(initialSubject)) selectSubject(initialSubject, initialUnit, false);
})();
