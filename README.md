# ECE Formula Vault

A no-login, static ECE formula library organised as **Year → Subject → Unit → Formula**. It is designed for GitHub Pages and works without a server-side backend.

## What's included

- 62 theory subjects from the JNTUH R25 B.Tech ECE course structure: required theory courses and the professional/open elective choices listed in that structure.
- 310 unit cards and 812 formula cards.
- Search across subject names, course codes, unit headings, formula names and equation text.
- Year/semester filters, saved subjects (stored only in the visitor's browser), dark mode, copy-to-clipboard and print-current-unit controls.
- Responsive layout for desktop and phones.
- Python and C utilities to sanity-check the catalogue.

## Important scope and accuracy note

The theory-course names and semester placement use the **JNTUH R25 B.Tech ECE course structure for constituent colleges, applicable from the 2025–26 batch**. Lab courses, workshops, internships, projects and activity-only entries are not represented as five-unit formula subjects. JNTUH affiliated/autonomous colleges and other universities may use different regulations or elective syllabi. The elective unit headings in this starter library are concise topic groupings, not a claim that every college uses identical wording. Formula cards are standard study references and include operating assumptions where relevant. Check your prescribed textbook, faculty notes, official unit outline and device datasheet before relying on any formula in an exam or design.

Official references:

- [JNTUH R25 B.Tech ECE syllabus PDF](https://jntuhces.ac.in/web/notifications/153_R25%20B.Tech%20%20ECE%20%20Course%20Structure%20and%20Syllabus.pdf)
- [JNTUH syllabus portal](https://jntuh.ac.in/syllabus)
- [AICTE ECE model curriculum](https://www.aicte.gov.in/sites/default/files/Final_ECE.pdf)

## Run locally

You can open `index.html` directly because the catalogue is embedded as a local JavaScript file. For a local HTTP preview, from this folder run:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Deploy on GitHub Pages

1. Create a new GitHub repository.
2. Upload **all files and folders** from this project. Keep `index.html` at the repository root.
3. Open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select branch `main` and folder `/ (root)`, then save.
6. Open the Pages URL GitHub displays after deployment.

No API key, login, database, build step or paid hosting is required. The page is static; do not move `index.html` into a subfolder unless you also update its relative asset paths.

## Validate before publishing

Python validator:

```bash
python tools/validate_catalog.py
```

C validator (if a C compiler is installed):

```bash
gcc -std=c11 -Wall -Wextra -pedantic tools/validate_catalog.c -o validate_catalog
./validate_catalog data.json
```

Both utilities check catalogue structure, duplicate subject IDs, five units per subject and non-empty formula expressions. They do **not** mathematically prove every equation; formulas should be reviewed against course references.

## Updating catalogue data

`build_data.py` is the catalogue source generator. After editing its subject/unit/formula entries, run:

```bash
python build_data.py
python tools/validate_catalog.py
```

That refreshes `data.json` and `assets/js/catalog.js`. Commit both files together.

## Project structure

```text
index.html
README.md
data.json
build_data.py
assets/
  favicon.svg
  css/style.css
  js/app.js
  js/catalog.js
tools/
  validate_catalog.py
  validate_catalog.c
```
