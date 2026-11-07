import json, os

OUT = os.path.join(os.path.dirname(__file__), 'data.json')
subjects = []

def F(name, formula, variables='', note=''):
    return {'name': name, 'formula': formula, 'variables': variables, 'note': note}

def U(title, topics, formulas=None):
    return {'title': title, 'topics': topics, 'formulas': formulas or []}

def S(code, name, year, sem, category, units, note=''):
    subjects.append({
        'id': code.lower().replace(' ', '-'), 'code': code, 'name': name,
        'year': year, 'semester': sem, 'category': category,
        'units': units, 'note': note
    })

# --------------------------- YEAR 1 ---------------------------------
S('5MA101BS','Matrices and Calculus',1,'Semester I','Foundation',[
 U('Matrices and linear systems','Rank, inverse, consistency, Gauss–Jordan and Gauss–Seidel methods.',[
  F('Matrix inverse','A⁻¹ = adj(A) / det(A)','For square A with det(A) ≠ 0.'),
  F('Cramer’s rule','xᵢ = det(Aᵢ) / det(A)','For A x = b and det(A) ≠ 0.'),
  F('Gauss–Seidel iteration','xᵢ⁽ᵏ⁺¹⁾ = (bᵢ − Σⱼ<ᵢ aᵢⱼxⱼ⁽ᵏ⁺¹⁾ − Σⱼ>ᵢ aᵢⱼxⱼ⁽ᵏ⁾) / aᵢᵢ','Use the latest available values; convergence is not guaranteed for every matrix.')]),
 U('Eigenvalues and eigenvectors','Characteristic equation, diagonalization and quadratic forms.',[
  F('Characteristic equation','det(A − λI) = 0','Roots λ are eigenvalues.'),
  F('Eigenvector equation','(A − λI)x = 0','x ≠ 0.'),
  F('Cayley–Hamilton theorem','p(A) = 0','Every square matrix satisfies its characteristic polynomial.')]),
 U('Single-variable calculus','Limits, continuity, mean value theorems, Taylor series and curve tracing.',[
  F('Taylor series about a','f(x) = Σₙ₌₀∞ [f⁽ⁿ⁾(a)/n!](x−a)ⁿ','Valid within the interval of convergence.'),
  F('Lagrange mean value theorem','f′(c) = [f(b)−f(a)]/(b−a)','f continuous on [a,b] and differentiable on (a,b).'),
  F('Maclaurin expansion','f(x) = f(0)+xf′(0)+x²f″(0)/2!+…','Taylor series with a = 0.')]),
 U('Multivariable calculus – differentiation','Partial derivatives, total derivatives, Jacobians, Euler theorem and extrema.',[
  F('Total differential','df = (∂f/∂x)dx + (∂f/∂y)dy','For f(x,y); extend by adding variables.'),
  F('Euler theorem for homogeneous functions','x fₓ + y fᵧ = n f','If f(x,y) is homogeneous of degree n.'),
  F('Jacobian','J = ∂(u,v)/∂(x,y) = uₓvᵧ − uᵧvₓ','For a two-variable transformation.'),
  F('Lagrange multiplier condition','∇f = λ∇g','Stationary points subject to g(x,y,…)=0.')]),
 U('Multiple integrals','Double/triple integrals, coordinate transformations, area and volume.',[
  F('Area using a double integral','A = ∬ᴿ 1 dA','R is the region in the plane.'),
  F('Polar area element','dA = r dr dθ','x = r cosθ, y = r sinθ.'),
  F('Cylindrical volume element','dV = r dr dθ dz','Right-handed cylindrical coordinates.'),
  F('Spherical volume element','dV = r² sinθ dr dθ dφ','θ is the polar angle and φ the azimuth under the common physics convention.')])
])

S('5CH102BS','Engineering Chemistry',1,'Semester I','Foundation',[
 U('Water and its treatment','Hardness, alkalinity, complexometric estimation, reverse osmosis and water quality.',[
  F('Hardness as CaCO₃','Hardness (mg/L) = (mass of CaCO₃ equivalent in mg) / (sample volume in L)','For dilute water solutions, mg/L is approximately ppm.'),
  F('EDTA hardness calculation','Hardness as CaCO₃ (mg/L) = (V_EDTA × M_EDTA × 100000) / V_sample','Volumes in mL; use the stated titration stoichiometry.'),
  F('pH','pH = −log₁₀[H⁺]','[H⁺] in mol/L.')]),
 U('Electrochemistry and corrosion','Electrode potentials, Nernst equation, electrochemical cells and corrosion.',[
  F('Nernst equation','E = E° − (RT/nF) ln Q','For the cell reaction as written.'),
  F('At 25 °C','E = E° − (0.05916/n) log₁₀ Q','E in volts; Q is dimensionless.'),
  F('Faraday’s law','m = (MIt)/(nF)','m is deposited mass; M molar mass; I current; t time.')]),
 U('Batteries and energy sources','Cell voltage, capacity, energy density, fuel-cell and battery terms.',[
  F('Cell emf','E_cell = E_cathode − E_anode','Use reduction potentials for both electrodes.'),
  F('Battery capacity','Capacity (Ah) = I(A) × t(h)','For constant current discharge.'),
  F('Electrical energy','E(Wh) = V(V) × Capacity(Ah)','Nominal approximation; actual energy depends on discharge curve.')]),
 U('Polymers and engineering materials','Degree of polymerization, molecular mass and material-property relations.',[
  F('Degree of polymerization','DPₙ = Mₙ / M₀','Number-average molecular mass divided by repeat-unit molar mass.'),
  F('Weight-average molecular mass','M_w = ΣNᵢMᵢ² / ΣNᵢMᵢ','Nᵢ is the number of molecules with molar mass Mᵢ.'),
  F('Polydispersity index','PDI = M_w / Mₙ','PDI ≥ 1 for ordinary polymer distributions.')]),
 U('Spectroscopy and analytical methods','Beer–Lambert law, absorbance, transmittance and vibrational spectroscopy.',[
  F('Beer–Lambert law','A = εcl = log₁₀(I₀/I)','ε molar absorptivity; c concentration; l path length.'),
  F('Transmittance','T = I/I₀;  %T = 100T','I transmitted intensity; I₀ incident intensity.'),
  F('Wavenumber','ṽ = 1/λ','If λ is in cm, ṽ is in cm⁻¹.')])
])

S('5CS103ES','C Programming and Data Structures',1,'Semester I','Foundation',[
 U('C basics and expressions','Data types, operators, integer arithmetic and expression evaluation.',[
  F('Integer division','q = trunc(a / b)','For integer operands; remainder follows C integer-division rules.'),
  F('Bit mask – set bit','x_new = x | (1u << k)','Sets bit k (zero-based).'),
  F('Bit mask – clear bit','x_new = x & ~(1u << k)','Clears bit k (zero-based).')]),
 U('Control flow and functions','Iteration, recursion, functions and recurrence relations.',[
  F('Arithmetic progression loop','T(n) = Θ(n)','A loop with n constant-time iterations.'),
  F('Binary recursion example','T(n) = 2T(n/2) + Θ(1) = Θ(n)','For a balanced divide-and-conquer recurrence.'),
  F('Factorial recurrence','n! = n × (n−1)!, 0! = 1','For integer n ≥ 0.')]),
 U('Arrays, strings and pointers','Array indexing, pointer arithmetic and string storage.',[
  F('Row-major 2D array address','LOC(A[i][j]) = base + w[(i×N)+j]','Zero-based indices; N columns; w bytes per element.'),
  F('Pointer offset','address(p + k) = address(p) + k × sizeof(*p)','C pointer arithmetic scales by pointed-to element size.'),
  F('C string storage','bytes = strlen(s) + 1','The extra byte stores the null terminator.')]),
 U('Structures, unions and linked lists','Structure alignment, dynamic allocation and linked data structures.',[
  F('Singly linked-list traversal','T(n) = Θ(n)','Search/traversal visits at most n nodes.'),
  F('Array access','T(n) = Θ(1)','Indexed access for a valid array index.'),
  F('Stack push/pop','T(n) = Θ(1)','With a top pointer/index and no resizing cost.')]),
 U('Stacks, queues, trees and sorting','Core data-structure operations and common algorithm costs.',[
  F('Binary search comparisons','T(n) = Θ(log₂ n)','Requires sorted data and random access for the usual array implementation.'),
  F('Merge sort','T(n) = Θ(n log₂ n)','Auxiliary space is Θ(n) for the standard array implementation.'),
  F('Binary-tree node count','N = 2^(h+1) − 1','Maximum nodes in a full binary tree of height h, with root at height 0.')])
], 'A programming course has relatively few fixed engineering equations; this section records useful complexity and memory relations.')

S('5EC104PC','Electronic Devices and Circuits',1,'Semester I','ECE Core',[
 U('Semiconductor physics and PN junction','Carrier concentration, drift/diffusion, PN junction and diode current.',[
  F('Thermal voltage','V_T = kT/q','≈ 25.85 mV at 300 K.'),
  F('Diode equation','I_D = I_S [exp(V_D/(ηV_T)) − 1]','η is the ideality factor; forward-bias model.'),
  F('Conductivity','σ = q(nμₙ + pμₚ)','n,p carrier concentrations; μₙ,μₚ mobilities.')]),
 U('Diode circuits and rectifiers','Ideal/practical diode models, clippers, clampers, rectifiers and filters.',[
  F('Half-wave rectifier average output','V_DC = V_m/π','Ideal diode, sinusoidal input, no filter.'),
  F('Full-wave rectifier average output','V_DC = 2V_m/π','Ideal full-wave rectifier; V_m is peak load voltage.'),
  F('Capacitor-filter ripple approximation','V_r(pp) ≈ I_L/(f_r C)','Small ripple approximation; f_r is ripple frequency (f for half-wave, 2f for full-wave).'),
  F('Rectifier efficiency','η_rect = P_DC/P_AC × 100%','Power delivered to the load divided by AC input power.')]),
 U('BJT characteristics and biasing','BJT current relations, operating point and bias stability.',[
  F('BJT current gain','β = I_C/I_B;  α = I_C/I_E','In forward-active operation, β = α/(1−α).'),
  F('Emitter current','I_E = I_C + I_B','Neglect leakage current in the usual approximation.'),
  F('Collector current in active region','I_C ≈ βI_B','Valid in forward-active operation, not saturation.'),
  F('Voltage-divider bias approximation','V_E ≈ V_B − V_BE;  I_E ≈ V_E/R_E','Assumes the divider is stiff relative to base current.')]),
 U('FET and MOSFET characteristics','JFET, MOSFET regions, transconductance and small-signal parameters.',[
  F('JFET Shockley equation','I_D = I_DSS(1 − V_GS/V_P)²','Valid in the JFET saturation region under the Shockley model.'),
  F('Long-channel MOSFET saturation current','I_D = (1/2)μC_ox(W/L)(V_GS−V_TH)²','Long-channel model; V_DS ≥ V_GS−V_TH; channel-length modulation neglected.'),
  F('MOSFET transconductance','g_m = 2I_D/V_OV','Long-channel saturation; V_OV = V_GS−V_TH.'),
  F('Small-signal voltage gain','A_v ≈ −g_m(R_D ∥ r_o)','Common-source stage, midband small-signal model.')]),
 U('Special semiconductor devices','Zener diode, LED, photodiode, SCR and optoelectronic device relations.',[
  F('Zener shunt current','I_Z = (V_S−V_Z)/R_S − I_L','Regulation requires I_Z to remain within specified limits.'),
  F('LED electrical power','P_LED = V_F I_F','Electrical input power; optical output is lower.'),
  F('Photodiode responsivity','R_λ = I_ph/P_opt','A/W at a specified wavelength and operating condition.'),
  F('SCR average current – half-wave controlled','I_avg = (V_m/(2πR))(1 + cos α)','Resistive load, ideal SCR, firing angle α; current conducts from α to π.')])
])

S('5EC105ES','Introduction to Electrical Engineering',1,'Semester I','Foundation',[
 U('DC circuits and network laws','Ohm’s law, KCL, KVL, series/parallel resistors and power.',[
  F('Ohm’s law','V = IR','Passive sign convention.'), F('Electrical power','P = VI = I²R = V²/R','For a resistor under DC conditions.'),
  F('KCL','ΣI_in = ΣI_out','Algebraic sum of currents at a node is zero.'), F('KVL','Σv_k = 0','Algebraic sum of voltages around a closed loop is zero.')]),
 U('AC fundamentals','Sinusoidal quantities, phase, RMS and average values.',[
  F('Sinusoidal voltage','v(t) = V_m sin(ωt + φ)','ω = 2πf.'), F('RMS value','V_rms = V_m/√2','Pure sinusoid.'),
  F('Average power','P = V_rms I_rms cosφ','Single-phase sinusoidal steady state.'), F('Power factor','pf = cosφ = P/S','For sinusoidal voltage and current.')]),
 U('Single-phase and three-phase systems','Balanced three-phase star/delta connections and power.',[
  F('Three-phase active power','P = √3 V_L I_L cosφ','Balanced system; V_L and I_L are line values.'),
  F('Star connection','V_L = √3 V_ph; I_L = I_ph','Balanced star load.'),
  F('Delta connection','V_L = V_ph; I_L = √3 I_ph','Balanced delta load.')]),
 U('Magnetic circuits and transformers','Magnetic flux, reluctance, induced emf and transformer ratios.',[
  F('Magnetic circuit','ℱ = NI = Φℜ','ℜ = l/(μA), uniform-core approximation.'),
  F('Faraday’s law','e = −N dΦ/dt','Negative sign represents Lenz’s law.'),
  F('Ideal transformer ratio','V₁/V₂ = N₁/N₂ = I₂/I₁','Ideal transformer; current ratio is inverse of turns ratio.')]),
 U('Electrical machines and energy conversion','Electromechanical power, efficiency and basic machine relations.',[
  F('Efficiency','η = P_out/P_in × 100%','For a machine or energy converter.'),
  F('Synchronous speed','N_s = 120f/P','rpm; f in Hz; P is number of poles.'),
  F('Slip','s = (N_s−N_r)/N_s','Induction motor; multiply by 100 for percent slip.')])
])

S('5MA201BS','Ordinary Differential Equations and Vector Calculus',1,'Semester II','Foundation',[
 U('First-order differential equations','Separable, linear and exact differential equations.',[
  F('First-order linear ODE','dy/dx + P(x)y = Q(x)','Integrating factor IF = e^(∫P(x)dx).'),
  F('Solution using integrating factor','y·IF = ∫Q·IF dx + C','For a linear first-order ODE.'),
  F('Separable equation','dy/g(y) = f(x) dx','Integrate both sides where separation is valid.')]),
 U('Higher-order linear differential equations','Constant-coefficient equations, complementary function and particular integral.',[
  F('Auxiliary equation','a_m r^m + a_(m−1)r^(m−1)+…+a₀ = 0','For a_m y⁽ᵐ⁾+…+a₀y = 0.'),
  F('Repeated root r','y_c = (C₁ + C₂x + … + Cₖx^(k−1))e^(rx)','For a root r of multiplicity k.'),
  F('Underdamped second-order response','y_c = e^(−αx)[C₁cos(βx)+C₂sin(βx)]','For characteristic roots α ± jβ.')]),
 U('Laplace transform methods','Laplace transforms, inverse transforms, shifting and convolution.',[
  F('Laplace transform','F(s) = ∫₀∞ f(t)e^(−st)dt','One-sided transform for t ≥ 0.'),
  F('Derivative transform','L{f′(t)} = sF(s) − f(0⁺)','For a function with suitable growth.'),
  F('Convolution theorem','L{f*g} = F(s)G(s)','(f*g)(t)=∫₀ᵗ f(τ)g(t−τ)dτ.')]),
 U('Vector differentiation','Gradient, divergence, curl and directional derivatives.',[
  F('Gradient','∇φ = x̂ ∂φ/∂x + ŷ ∂φ/∂y + ẑ ∂φ/∂z','Scalar field φ.'),
  F('Divergence','∇·A = ∂Aₓ/∂x + ∂Aᵧ/∂y + ∂A_z/∂z','Vector field A.'),
  F('Curl','∇×A = det[x̂,ŷ,ẑ; ∂x,∂y,∂z; Aₓ,Aᵧ,A_z]','Cartesian coordinates.')]),
 U('Vector integration theorems','Line, surface and volume integrals; Green, Stokes and divergence theorems.',[
  F('Line integral','∫_C A·dl','Work/circulation along curve C.'),
  F('Divergence theorem','∯_S A·dS = ∭_V (∇·A)dV','S is a closed outward-oriented surface bounding V.'),
  F('Stokes theorem','∮_C A·dl = ∬_S (∇×A)·dS','C is positively oriented boundary of S.')])
])

S('5PH202BS','Applied Physics',1,'Semester II','Foundation',[
 U('Wave optics and interference','Interference, diffraction, polarization and optical path difference.',[
  F('Constructive interference','Δ = mλ','Path difference; integer m.'), F('Destructive interference','Δ = (m+1/2)λ','For two coherent waves of equal/appropriate amplitudes.'),
  F('Single-slit minima','a sinθ = mλ,  m = ±1, ±2,…','Slit width a.'), F('Malus law','I = I₀ cos²θ','Ideal linear polarizer/analyzer.')]),
 U('Quantum mechanics','Photon energy, de Broglie wavelength and uncertainty principle.',[
  F('Photon energy','E = hν = hc/λ','Photon in vacuum.'), F('de Broglie wavelength','λ = h/p','For a particle with momentum p.'),
  F('Heisenberg uncertainty','Δx Δp ≥ ħ/2','Position and momentum standard deviations.'),
  F('1D infinite-well energy','Eₙ = n²h²/(8mL²)','Particle in a one-dimensional infinite potential well.')]),
 U('Semiconductor physics','Carrier statistics, conductivity, Hall effect and band concepts.',[
  F('Intrinsic carrier concentration','n_i² = np','At thermal equilibrium.'), F('Conductivity','σ = q(nμₙ + pμₚ)','Non-degenerate semiconductor approximation.'),
  F('Hall coefficient – n-type','R_H ≈ −1/(qn)','Single dominant electron carrier.'), F('Drift current density','J_drift = q(nμₙ + pμₚ)E','Magnitude for electron and hole contributions.')]),
 U('Dielectric and magnetic materials','Polarization, permittivity, susceptibility and magnetic quantities.',[
  F('Electric displacement','D = ε₀E + P = εE','Linear isotropic dielectric: P = ε₀χₑE.'),
  F('Relative permittivity','ε_r = 1 + χₑ','Linear isotropic material.'),
  F('Magnetic flux density','B = μH','Linear isotropic medium.'),
  F('Magnetic susceptibility','M = χ_m H','Linear isotropic material.')]),
 U('Lasers and fibre optics','Einstein coefficients, numerical aperture, acceptance angle and attenuation.',[
  F('Photon energy','E = hν','Laser transition energy.'),
  F('Numerical aperture','NA = √(n₁²−n₂²)','Step-index fibre with n₁ > n₂, external medium n₀ = 1.'),
  F('Acceptance angle','sinθ_a = NA/n₀','For launch medium refractive index n₀.'),
  F('Fibre attenuation','α(dB/km) = (10/L) log₁₀(P_in/P_out)','L in km; connector/splice losses included if measured.')])
])

S('5EE204ES','Network Analysis and Synthesis',1,'Semester II','ECE Core',[
 U('Network topology and coupled circuits','Trees, links, tie sets, cut sets, magnetic circuits and ideal transformers.',[
  F('Mutual inductance','M = k√(L₁L₂)','0 ≤ k ≤ 1 for coupled coils.'), F('Coupled-coil voltages','v₁ = L₁ di₁/dt ± M di₂/dt','Sign depends on dot convention.'),
  F('Magnetic reluctance','ℜ = l/(μA)','Uniform magnetic path approximation.'), F('Ideal transformer impedance reflection','Z_in = (N₁/N₂)² Z_L','Load Z_L referred to primary.')]),
 U('Transient and steady-state analysis','RC, RL and RLC step/sinusoidal responses.',[
  F('RC time constant','τ = RC','Series RC circuit.'), F('RL time constant','τ = L/R','Series RL circuit.'),
  F('Series RLC natural frequency','ω₀ = 1/√(LC)','Undamped natural angular frequency.'),
  F('Damping ratio','ζ = (R/2)√(C/L)','Series RLC circuit.')]),
 U('Network theorems and two-port networks','Thevenin, Norton, superposition, reciprocity and two-port parameters.',[
  F('Thevenin equivalent','V_TH = V_oc;  R_TH = V_oc/I_sc','Linear two-terminal network; dependent sources require a test source for resistance.'),
  F('Norton equivalent','I_N = I_sc;  R_N = R_TH','Same terminal behavior as Thevenin form.'),
  F('ABCD cascade','[A B; C D]_total = [A B; C D]_1 [A B; C D]_2','With a consistent two-port sign convention.'),
  F('Z-parameter form','V₁ = z₁₁I₁ + z₁₂I₂;  V₂ = z₂₁I₁ + z₂₂I₂','Currents are defined entering both ports.')]),
 U('Filters, attenuators and equalizers','Low/high/band-pass and band-stop filters; characteristic impedance and attenuation.',[
  F('RC low-pass cutoff','f_c = 1/(2πRC)','First-order passive RC filter.'),
  F('RC high-pass cutoff','f_c = 1/(2πRC)','First-order passive RC filter.'),
  F('Resonant frequency','f₀ = 1/(2π√(LC))','Ideal LC resonance.'),
  F('Voltage gain in dB','G_v(dB) = 20log₁₀|V_out/V_in|','Use 10log for power ratios.')]),
 U('Network synthesis','Positive-real functions, driving-point functions and Foster/Cauer forms.',[
  F('Positive-real condition','Re[Z(s)] ≥ 0 for Re(s) > 0','For a passive driving-point impedance with real coefficients.'),
  F('Series resonance impedance','Z = R + j(ωL − 1/(ωC))','Ideal series RLC.'),
  F('Parallel resonance (ideal LC)','ω₀ = 1/√(LC)','Losses modify the exact resonant frequency and impedance peak.')])
])

# --------------------------- YEAR 2 ---------------------------------
S('5EC301PC','Probability Theory and Stochastic Processes',2,'Semester I','ECE Core',[
 U('Probability fundamentals','Events, conditional probability, independence and Bayes theorem.',[
  F('Conditional probability','P(A|B) = P(A∩B)/P(B)','P(B) > 0.'),
  F('Bayes theorem','P(Aᵢ|B) = P(B|Aᵢ)P(Aᵢ) / ΣⱼP(B|Aⱼ)P(Aⱼ)','{Aᵢ} is a partition of the sample space.'),
  F('Total probability','P(B) = Σᵢ P(B|Aᵢ)P(Aᵢ)','For a partition {Aᵢ}.')]),
 U('Single random variables','PMF, PDF, CDF, expectation, variance and standard distributions.',[
  F('Expected value','E[X] = Σₓ x p_X(x)  or  ∫x f_X(x)dx','Use sum for discrete, integral for continuous variables.'),
  F('Variance','Var(X) = E[X²] − (E[X])²','Finite second moment.'),
  F('Gaussian PDF','f_X(x)=1/(σ√(2π)) exp(−(x−μ)²/(2σ²))','Mean μ and variance σ².'),
  F('Poisson PMF','P(X=k)=e^(−λ)λᵏ/k!','k=0,1,…; λ>0.')]),
 U('Multiple random variables','Joint/marginal distributions, independence, covariance and conditional expectation.',[
  F('Covariance','Cov(X,Y)=E[XY]−E[X]E[Y]','Finite second moments.'),
  F('Correlation coefficient','ρ_XY = Cov(X,Y)/(σ_Xσ_Y)','σ_X,σ_Y > 0; −1 ≤ ρ ≤ 1.'),
  F('Sum of independent variables','E[X+Y]=E[X]+E[Y]; Var(X+Y)=Var(X)+Var(Y)','Variance identity requires independence or zero covariance.')]),
 U('Random processes and correlation','Stationarity, ergodicity, autocorrelation and cross-correlation.',[
  F('Autocorrelation','R_X(τ)=E[X(t)X(t+τ)]','For a wide-sense stationary real process.'),
  F('Variance from autocorrelation','σ_X²=R_X(0)−μ_X²','WSS process.'),
  F('Cross-correlation','R_XY(τ)=E[X(t)Y(t+τ)]','Convention shown; some texts reverse the lag sign.')]),
 U('Power spectra and noise','Power spectral density, Wiener–Khinchin relation, white noise and noise figure.',[
  F('Wiener–Khinchin relation','S_X(f)=∫₋∞∞ R_X(τ)e^(−j2πfτ)dτ','Two-sided PSD convention.'),
  F('Noise power in bandwidth','N = kTB','Available thermal-noise power; matched system, absolute temperature T.'),
  F('Noise figure','F = SNR_in/SNR_out','Linear ratio; NF(dB)=10log₁₀F.'),
  F('Thermal noise voltage','v_n,rms = √(4kTRB)','Resistor R over bandwidth B, classical approximation.')])
])

S('5EC302PC','Signals and Systems',2,'Semester I','ECE Core',[
 U('Signal classification and basic operations','Continuous/discrete signals, energy, power, periodicity and transformations.',[
  F('Signal energy (CT)','E = ∫₋∞∞ |x(t)|²dt','Finite-energy signal.'),
  F('Average power (CT)','P = lim(T→∞) (1/2T)∫₋Tᵀ |x(t)|²dt','For signals for which the limit exists.'),
  F('Discrete-time energy','E = Σₙ₌₋∞∞ |x[n]|²','Finite-energy sequence.'),
  F('CT periodicity','x(t+T₀)=x(t)','T₀ is the smallest positive period.')]),
 U('LTI systems and convolution','Impulse response, convolution, causality and stability.',[
  F('Continuous-time convolution','y(t)=∫₋∞∞ x(τ)h(t−τ)dτ','For an LTI system.'),
  F('Discrete-time convolution','y[n]=Σₖ₌₋∞∞ x[k]h[n−k]','For an LTI system.'),
  F('BIBO stability condition','∫₋∞∞ |h(t)|dt < ∞','CT LTI system.'),
  F('BIBO stability condition','Σₙ₌₋∞∞ |h[n]| < ∞','DT LTI system.')]),
 U('Fourier series and Fourier transform','Trigonometric/exponential Fourier series and continuous-time Fourier transform.',[
  F('CT Fourier series coefficient','C_k=(1/T₀)∫_{T₀}x(t)e^(−jkω₀t)dt','Integral over any one period; ω₀=2π/T₀.'),
  F('CT Fourier transform','X(ω)=∫₋∞∞ x(t)e^(−jωt)dt','Angular-frequency convention.'),
  F('Inverse CTFT','x(t)=(1/2π)∫₋∞∞ X(ω)e^(jωt)dω','Matching transform convention.'),
  F('Parseval relation','∫|x(t)|²dt=(1/2π)∫|X(ω)|²dω','For finite-energy signals.')]),
 U('Laplace transform and system analysis','ROC, poles/zeros, transfer functions and system response.',[
  F('Laplace transform','X(s)=∫₀∞ x(t)e^(−st)dt','Unilateral transform; bilateral form integrates from −∞ to ∞.'),
  F('Derivative property','L{x′(t)}=sX(s)−x(0⁻)','Unilateral transform.'),
  F('Transfer function','H(s)=Y(s)/X(s)','Zero initial conditions.'),
  F('Convolution property','L{x(t)*h(t)}=X(s)H(s)','For compatible signals and ROC.')]),
 U('Sampling and Z-transform','Impulse/natural sampling, aliasing, reconstruction and discrete-time transforms.',[
  F('Nyquist sampling condition','f_s > 2f_max','Ideal bandlimited signal; practical anti-alias filtering is required.'),
  F('Z-transform','X(z)=Σₙ₌₋∞∞ x[n]z^(−n)','Bilateral Z-transform.'),
  F('Inverse Z-transform pair','x[n]=(1/2πj)∮ X(z)z^(n−1)dz','Contour lies in the ROC.'),
  F('Discrete-time frequency response','H(e^jω)=H(z)|_(z=e^jω)','Unit-circle substitution is valid when the unit circle is in the ROC.')])
])

S('5EC303PC','Electronic Circuit Analysis',2,'Semester I','ECE Core',[
 U('Multistage and high-frequency amplifiers','Cascaded stages, coupling, hybrid-π model and frequency response.',[
  F('Cascaded voltage gain','A_v,total = A_v1 × A_v2 × … × A_vn','Voltage gains are signed; loading must be included.'),
  F('Gain in decibels','A_v(dB)=20log₁₀|A_v|','Voltage ratio with equal impedance basis.'),
  F('Bandwidth','BW = f_H − f_L','Lower and upper −3 dB frequencies.'),
  F('Gain-bandwidth product','GBW ≈ |A_v| × BW','Approximation for a dominant-pole amplifier over the applicable region.')]),
 U('Feedback amplifiers','Positive/negative feedback, gain, sensitivity, bandwidth and distortion.',[
  F('Negative-feedback gain','A_f = A/(1 + Aβ)','Aβ is loop gain; standard negative-feedback topology.'),
  F('Sensitivity','S = 1/(1 + Aβ)','Sensitivity of closed-loop gain to open-loop gain changes.'),
  F('Bandwidth approximation','BW_f ≈ BW(1 + Aβ)','For a single-pole amplifier with negative feedback.'),
  F('Distortion reduction','D_f ≈ D/(1 + Aβ)','Small-signal feedback approximation.')]),
 U('Sinusoidal oscillators','Barkhausen criterion, RC phase shift, Wien bridge, LC and crystal oscillators.',[
  F('Barkhausen magnitude condition','|Aβ| = 1','At oscillation frequency; total loop phase is 0° modulo 360°.'),
  F('Wien bridge frequency','f₀ = 1/(2πRC)','For equal R and equal C arms.'),
  F('Hartley oscillator','f₀ = 1/(2π√(C(L₁+L₂+2M)))','Series-aiding coupled inductors; mutual inductance M.'),
  F('Colpitts oscillator','f₀ = 1/(2π√(L C_eq)); C_eq=C₁C₂/(C₁+C₂)','Ideal resonant tank approximation.')]),
 U('Power amplifiers','Class A/B/AB/C operation, efficiency and push-pull stages.',[
  F('Efficiency','η = P_out(ac)/P_in(dc)','Power-amplifier efficiency.'),
  F('Class B maximum efficiency','η_max = π/4 ≈ 78.5%','Ideal complementary push-pull class-B stage.'),
  F('Transistor dissipation','P_D = V_CE I_C','Instantaneous product; average over a cycle for average dissipation.'),
  F('Conduction angle','θ = interval of conduction in degrees','Class A: 360°; class B: 180° per device; class C: less than 180°.')]),
 U('Multivibrators and time-base circuits','Astable/monostable circuits, pulse shaping and sweep generation.',[
  F('555 monostable pulse width','T ≈ 1.1RC','Standard 555 monostable configuration.'),
  F('555 astable frequency','f ≈ 1.44/[(R_A+2R_B)C]','Standard 555 astable circuit.'),
  F('555 astable duty cycle','D = (R_A+R_B)/(R_A+2R_B)','Standard 555 astable; duty cycle exceeds 50% for positive resistors.')])
])

S('5EC304PC','Digital Logic Design',2,'Semester I','ECE Core',[
 U('Number systems, codes and Boolean algebra','Base conversions, signed arithmetic, parity/Hamming codes and logic identities.',[
  F('Unsigned n-bit range','0 to 2ⁿ−1','n-bit binary number.'),
  F('Two’s-complement range','−2ⁿ⁻¹ to 2ⁿ⁻¹−1','n-bit signed representation.'),
  F('Hamming parity-bit condition','2ʳ ≥ m + r + 1','m data bits and r Hamming check bits for single-error correction.'),
  F('De Morgan identities','(A+B)′=A′B′;  (AB)′=A′+B′','Boolean variables.')]),
 U('Boolean minimization and combinational logic','K-maps, SOP/POS, adders, comparators, encoders, decoders and multiplexers.',[
  F('Half adder','S=A⊕B;  C_out=AB','One-bit addition.'),
  F('Full adder','S=A⊕B⊕C_in;  C_out=AB+AC_in+BC_in','One-bit addition.'),
  F('n:1 multiplexer select lines','s = ⌈log₂ n⌉','For n inputs, assuming a power-of-two implementation when fully populated.'),
  F('Decoder outputs','2ⁿ output lines for n input bits','One active output per input code in a standard one-hot decoder.')]),
 U('Sequential circuits and flip-flops','Latches, SR/JK/D/T flip-flops, timing and state equations.',[
  F('D flip-flop characteristic','Q⁺ = D','At the active clock edge.'),
  F('T flip-flop characteristic','Q⁺ = T⊕Q','T=1 toggles; T=0 holds.'),
  F('JK flip-flop characteristic','Q⁺ = JQ′ + K′Q','At the active clock edge.'),
  F('Toggle frequency for divide-by-N counter','f_out = f_clk/N','For a counter that produces one output cycle every N clock pulses.')]),
 U('Counters and registers','Synchronous/asynchronous counters, shift registers and sequence generators.',[
  F('Modulus and flip-flops','N ≤ 2ⁿ;  n = ⌈log₂N⌉','Minimum n flip-flops for a mod-N counter.'),
  F('Ring counter states','N_states = n','n-stage one-hot ring counter, excluding lock-up states.'),
  F('Johnson counter states','N_states = 2n','n-stage twisted-ring counter.'),
  F('Register storage','Capacity = n bits','n one-bit storage elements.')]),
 U('Programmable logic and timing','PLDs, propagation delay, setup/hold constraints and HDL timing.',[
  F('Clock period constraint','T_clk ≥ t_clk→Q + t_comb + t_setup + t_skew','Synchronous register-to-register path; include uncertainty as required.'),
  F('Maximum clock frequency','f_max ≤ 1/T_min','T_min is the worst-case legal clock period.'),
  F('Dynamic CMOS power','P_dyn = α C_L V_DD² f','α is activity factor; ideal first-order switching-power model.')])
])

S('5EC305PC','Control Systems Engineering',2,'Semester I','ECE Core',[
 U('System modelling and block diagrams','Differential-equation models, transfer functions, block reduction and signal-flow graphs.',[
  F('Transfer function','G(s)=Y(s)/R(s)','Zero initial conditions.'),
  F('Unity-feedback closed-loop transfer','T(s)=G(s)/(1+G(s))','Negative unity feedback.'),
  F('Non-unity feedback','T(s)=G(s)/(1+G(s)H(s))','Negative feedback.'),
  F('Mason gain formula','T = Σ_k P_kΔ_k/Δ','Signal-flow graph; Δ and Δ_k are Mason cofactors.')]),
 U('Time response and performance','First/second-order response, transient specifications and steady-state error.',[
  F('Standard second-order denominator','s²+2ζωₙs+ωₙ²','Natural frequency ωₙ and damping ratio ζ.'),
  F('Peak time','T_p = π/[ωₙ√(1−ζ²)]','Underdamped system, 0<ζ<1.'),
  F('Percent overshoot','M_p(%)=100 exp[−πζ/√(1−ζ²)]','Underdamped standard second-order system.'),
  F('Settling time (2% approx.)','T_s ≈ 4/(ζωₙ)','Standard second-order approximation.')]),
 U('Stability and root locus','Routh–Hurwitz criterion, root-locus rules and pole locations.',[
  F('Characteristic equation','1+K G(s)H(s)=0','Negative-feedback loop.'),
  F('Routh stability condition','All first-column entries have the same nonzero sign','For no right-half-plane roots; special zero-row/zero-element cases require auxiliary procedures.'),
  F('Root-locus angle condition','∠G(s)H(s)=(2k+1)180°','For real positive gain K.'),
  F('Root-locus magnitude condition','K=1/|G(s)H(s)|','At a point satisfying the angle condition.')]),
 U('Frequency response','Bode, polar and Nyquist plots; gain/phase margins.',[
  F('Magnitude in dB','M(dB)=20log₁₀|G(jω)|','Voltage/amplitude transfer ratio.'),
  F('Phase margin','PM=180°+∠G(jω_gc)','At gain-crossover frequency ω_gc where |G|=1.'),
  F('Gain margin','GM=1/|G(jω_pc)|','At phase-crossover frequency ω_pc; dB form is −20log₁₀|G|.'),
  F('Resonant peak (2nd order)','M_r=1/[2ζ√(1−ζ²)]','For 0<ζ<1/√2.')]),
 U('State-space analysis','State models, controllability, observability and state transition matrix.',[
  F('State equation','ẋ=Ax+Bu;  y=Cx+Du','Linear time-invariant state-space model.'),
  F('Controllability matrix','𝒞=[B AB A²B … Aⁿ⁻¹B]','Completely controllable iff rank(𝒞)=n.'),
  F('Observability matrix','𝒪=[C; CA; CA²; …; CAⁿ⁻¹]','Completely observable iff rank(𝒪)=n.'),
  F('State transition matrix','Φ(t)=e^(At)','For a time-invariant system.')])
])

S('5MA401BS','Numerical Methods and Complex Variables',2,'Semester II','Foundation',[
 U('Roots of equations','Bisection, Regula Falsi, Newton–Raphson and convergence.',[
  F('Newton–Raphson iteration','xₙ₊₁=xₙ−f(xₙ)/f′(xₙ)','Requires f′(xₙ) ≠ 0 and a suitable initial guess.'),
  F('Bisection midpoint','x_m=(a+b)/2','f(a)f(b)<0 and f continuous on [a,b].'),
  F('Bisection error bound','|x_m−r| ≤ (b₀−a₀)/2^(n+1)','After n bisection steps, with initial width b₀−a₀.')]),
 U('Interpolation and curve fitting','Newton forward/backward, Lagrange and least-squares fitting.',[
  F('Lagrange interpolation','P_n(x)=Σᵢ yᵢ Πⱼ≠ᵢ[(x−xⱼ)/(xᵢ−xⱼ)]','Distinct interpolation nodes.'),
  F('Newton forward interpolation','y(x)=y₀+uΔy₀+u(u−1)Δ²y₀/2!+…','Equal spacing; u=(x−x₀)/h.'),
  F('Least-squares line','y=a+bx;  b=Σ(x−x̄)(y−ȳ)/Σ(x−x̄)²','For data pairs with nonzero x variance.')]),
 U('Numerical differentiation and integration','Finite differences, trapezoidal and Simpson rules.',[
  F('Central difference derivative','f′(x)≈[f(x+h)−f(x−h)]/(2h)','Second-order accurate for smooth f.'),
  F('Trapezoidal rule','∫ₐᵇf(x)dx≈(h/2)[y₀+yₙ+2Σᵢ₌₁ⁿ⁻¹yᵢ]','n equal subintervals, h=(b−a)/n.'),
  F('Simpson 1/3 rule','∫ₐᵇf(x)dx≈(h/3)[y₀+yₙ+4Σ_odd yᵢ+2Σ_even yᵢ','n must be even; equally spaced samples.')]),
 U('Complex variables and analytic functions','Cauchy–Riemann equations, analytic functions and complex differentiation.',[
  F('Cauchy–Riemann equations','uₓ=vᵧ;  uᵧ=−vₓ','For f(z)=u(x,y)+jv(x,y), with appropriate differentiability.'),
  F('Complex derivative','f′(z)=lim_(Δz→0)[f(z+Δz)−f(z)]/Δz','Limit must be direction-independent.'),
  F('Polar Cauchy–Riemann','u_r=(1/r)v_θ;  v_r=−(1/r)u_θ','For r>0.')]),
 U('Complex integration and transforms','Contour integrals, Cauchy theorem, residues and conformal maps.',[
  F('Cauchy integral formula','f(a)=(1/2πj)∮_C f(z)/(z−a) dz','f analytic on and inside a positively oriented simple contour C.'),
  F('Residue theorem','∮_C f(z)dz=2πj Σ Res(f,z_k)','Sum residues at isolated singularities inside C.'),
  F('Residue at a simple pole','Res(f,a)=lim_(z→a)(z−a)f(z)','Simple pole at a.')])
])

S('5EC402PC','Electromagnetic Fields and Transmission Lines',2,'Semester II','ECE Core',[
 U('Electrostatics','Coulomb law, electric flux density, Gauss law, potential and capacitance.',[
  F('Coulomb force','F=(1/(4πε))(q₁q₂/r²) r̂','Point charges in a homogeneous medium.'),
  F('Electric field of a point charge','E=(q/(4πεr²))r̂','Homogeneous isotropic medium.'),
  F('Gauss law','∯_S D·dS=Q_enclosed','Closed surface.'),
  F('Capacitance','C=Q/V','Two-terminal capacitor under electrostatic conditions.')]),
 U('Magnetostatics','Biot–Savart law, Ampere law, magnetic vector potential and inductance.',[
  F('Ampere’s circuital law','∮_C H·dl=I_enclosed','Steady currents.'),
  F('Magnetic flux density','B=μH','Linear isotropic medium.'),
  F('Inductance','L=NΦ/I','Flux linkage per current; linear magnetic circuit.'),
  F('Energy in an inductor','W_m=(1/2)LI²','Linear inductor.')]),
 U('Time-varying fields and Maxwell equations','Faraday law, displacement current, Maxwell equations and boundary conditions.',[
  F('Faraday law','∇×E=−∂B/∂t','Differential form.'),
  F('Ampere–Maxwell law','∇×H=J+∂D/∂t','Differential form.'),
  F('Gauss law for magnetism','∇·B=0','No magnetic monopoles in classical Maxwell theory.'),
  F('Gauss law for electricity','∇·D=ρ_v','Differential form.')]),
 U('Uniform plane waves','Wave equation, intrinsic impedance, propagation constant and Poynting vector.',[
  F('Free-space wave impedance','η₀=√(μ₀/ε₀)≈376.73 Ω','Plane wave in free space.'),
  F('Propagation constant','γ=α+jβ=√[(R+jωL)(G+jωC)]','General uniform transmission line.'),
  F('Lossless-medium phase constant','β=ω√(με)','Lossless homogeneous medium.'),
  F('Poynting vector','S=E×H','Instantaneous power-flow density, W/m².')]),
 U('Transmission lines','Reflection, standing waves, impedance transformation and Smith chart.',[
  F('Characteristic impedance','Z₀=√[(R+jωL)/(G+jωC)]','General uniform line.'),
  F('Reflection coefficient','Γ_L=(Z_L−Z₀)/(Z_L+Z₀)','At the load.'),
  F('VSWR','S=(1+|Γ|)/(1−|Γ|)','For |Γ|<1.'),
  F('Input impedance – lossless line','Z_in=Z₀ (Z_L+jZ₀tanβl)/(Z₀+jZ_Ltanβl)','Line length l measured toward the generator.')])
])

S('5EC403PC','Analog and Digital Communications',2,'Semester II','ECE Core',[
 U('Amplitude modulation','AM, DSB-SC, SSB, VSB and coherent/envelope detection.',[
  F('Conventional AM signal','s(t)=A_c[1+m cos(ω_m t)]cos(ω_c t)','Single-tone modulation; 0≤m≤1 avoids envelope overmodulation.'),
  F('AM modulation index','m=(A_max−A_min)/(A_max+A_min)','Measured from an undistorted AM envelope.'),
  F('AM total power','P_T=P_C(1+m²/2)','Single-tone conventional AM.'),
  F('AM bandwidth','BW=2f_m','Single-tone message; highest message frequency f_m for general message gives 2f_max.')]),
 U('Angle modulation and transmitters/receivers','FM/PM, Carson rule, PLL, superheterodyne receiver and noise.',[
  F('FM modulation index','β=Δf/f_m','Single-tone modulation.'),
  F('Carson bandwidth rule','BW≈2(Δf+f_m)','Approximate FM bandwidth; Δf peak frequency deviation.'),
  F('Superheterodyne IF','f_IF=|f_RF−f_LO|','Mixer selects the desired difference-frequency product.'),
  F('Thermal noise power','N=kTB','Matched input, bandwidth B.')]),
 U('Pulse modulation','PAM, PWM, PPM, PCM and delta modulation.',[
  F('PCM bit rate','R_b=n f_s','n bits/sample and sampling rate f_s.'),
  F('Quantization step','Δ= (V_max−V_min)/2ⁿ','Uniform n-bit quantizer across the specified full-scale range.'),
  F('Ideal PCM SQNR','SQNR_dB≈6.02n+1.76 dB','Uniform quantizer, full-scale sinusoidal input, high-resolution approximation.'),
  F('Nyquist sampling','f_s>2f_max','Bandlimited baseband signal.')]),
 U('Digital modulation','ASK, FSK, PSK, QPSK and coherent/non-coherent detection.',[
  F('Symbol rate','R_s=R_b/log₂M','M-ary modulation with log₂M bits per symbol.'),
  F('BPSK bit error probability','P_b=Q(√(2E_b/N₀))','Coherent BPSK in AWGN.'),
  F('QPSK bit error probability','P_b=Q(√(2E_b/N₀))','Gray-coded coherent QPSK in AWGN, per bit.'),
  F('Q-function','Q(x)=(1/√(2π))∫ₓ∞e^(−u²/2)du','Standard normal tail probability.')]),
 U('Baseband transmission and information theory','Line coding, ISI, matched filters, entropy and channel capacity.',[
  F('Shannon capacity','C=B log₂(1+S/N)','AWGN channel; S/N is linear power ratio.'),
  F('Nyquist zero-ISI bit rate','R_b≤2B log₂M','Ideal noiseless bandlimited channel with M signal levels.'),
  F('Entropy','H(X)=−Σᵢpᵢlog₂pᵢ','Bits per source symbol.'),
  F('Raised-cosine bandwidth','B=(1+α)R_s/2','One-sided baseband bandwidth; roll-off 0≤α≤1.')])
])

S('5EC404PC','RISC and Microcontroller Architectures',2,'Semester II','ECE Core',[
 U('8086 and 8051 architecture','Register organization, memory segmentation, internal memory and I/O.',[
  F('8086 physical address','Physical address = Segment × 16 + Offset','20-bit address formation.'),
  F('8086 address space','2²⁰ bytes = 1 MiB','20-bit physical address bus.'),
  F('8051 internal data memory','128 bytes (classic 8051)','Classic 8051 baseline; variants differ.')]),
 U('Timers, counters and serial I/O','Timer modes, reload values, baud rate and serial communication.',[
  F('Timer overflow interval','T_overflow = (N−count_initial) × T_machine','Timer increments once per timer tick; machine-cycle definition depends on MCU clock/divider.'),
  F('Classic 8051 machine-cycle time','T_machine = 12/f_osc','Classic 12-clock 8051 core; modern derivatives may use fewer clocks.'),
  F('UART frame time','T_frame = bits_per_frame / baud','Include start, data, parity (if used) and stop bits.'),
  F('Baud-rate relation (generic)','baud = 1/T_bit','Specific 8051 reload formulas depend on timer mode and oscillator frequency.')]),
 U('ARM architecture and instruction set','RISC principles, registers, pipeline, addressing and instruction formats.',[
  F('Instruction throughput (ideal pipeline)','Throughput ≈ 1 instruction/clock','Ideal steady-state single-issue pipeline; stalls and branches reduce throughput.'),
  F('CPI','CPI = total clock cycles / retired instructions','Average cycles per instruction.'),
  F('CPU execution time','T_CPU = Instruction Count × CPI × T_clock','Equivalently IC × CPI / clock frequency.')]),
 U('Cortex-M architecture and exceptions','NVIC, exception entry, stack, interrupt latency and memory map.',[
  F('Interrupt latency budget','T_latency = T_entry + T_blocking + T_higher-priority','Simplified fixed-priority response-time model; implementation-specific.'),
  F('Memory-mapped register address','address = peripheral_base + register_offset','Use the device reference manual for exact addresses.'),
  F('Bit-band alias (where supported)','alias = alias_base + (byte_offset×32) + (bit_number×4)','ARMv7-M bit-band regions only; not present on all Cortex-M devices.')]),
 U('Memory and peripheral interfacing','Address decoding, ADC/DAC, bus timing and serial interfaces.',[
  F('ADC resolution','LSB ≈ V_range/2ⁿ','n-bit unipolar ADC; exact code transition convention may use 2ⁿ or 2ⁿ−1.'),
  F('DAC output – ideal unipolar','V_out ≈ code × V_ref/2ⁿ','n-bit straight-binary DAC; device scaling conventions vary.'),
  F('Addressable memory','Capacity = 2ⁿ bytes','n address bits when each address selects one byte.')])
])

S('5EC405PC','Linear and Digital IC Applications',2,'Semester II','ECE Core',[
 U('Operational amplifier fundamentals','Ideal/practical op-amp, inverting, non-inverting, differential and instrumentation amplifiers.',[
  F('Inverting amplifier','A_v=−R_f/R_in','Ideal op-amp, linear closed-loop operation.'),
  F('Non-inverting amplifier','A_v=1+R_f/R_1','Ideal op-amp, linear closed-loop operation.'),
  F('Difference amplifier','V_out=(R₂/R₁)(V₂−V₁)','Matched resistor ratios: R₂/R₁=R₄/R₃.'),
  F('Slew-rate limit','SR = max|dV_out/dt|','V/µs; large-signal dynamic limit.')]),
 U('Active filters, waveform generators and timers','Butterworth filters, integrators, differentiators, 555 timer and PLL.',[
  F('First-order LPF cutoff','f_c=1/(2πRC)','Single-pole RC active/passive filter.'),
  F('Ideal inverting integrator','V_out(t)=−(1/RC)∫V_in(t)dt','Ideal op-amp; practical integrators add a parallel resistor.'),
  F('Ideal differentiator','V_out(t)=−RC dV_in/dt','Ideal op-amp; practical differentiators are bandwidth-limited.'),
  F('555 monostable width','T≈1.1RC','Standard monostable configuration.')]),
 U('Data converters','Weighted-resistor/R-2R DAC, ADC architectures and conversion specifications.',[
  F('n-bit quantization levels','L=2ⁿ','Unipolar binary converter.'),
  F('ADC quantization error','|e_q|≤Δ/2','Ideal uniform mid-tread quantizer.'),
  F('Ideal DAC output','V_out=V_ref(D/2ⁿ)','Straight-binary unipolar convention; D is integer code.'),
  F('Conversion rate','f_conv=1/T_conv','T_conv is conversion time.')]),
 U('Digital ICs and memories','Logic families, memory capacity, RAM/ROM and programmable logic.',[
  F('Memory capacity','Capacity = (number of words) × (bits per word)','Convert bits to bytes by dividing by 8.'),
  F('Address lines','n = log₂(number of addressable words)','Assumes a power-of-two number of words.'),
  F('Fan-out','FO = maximum number of standard inputs driven','Use actual IOH/IOL and IIH/IIL specs for a numeric value.')]),
 U('Sequential IC applications','Counters, registers, shift registers, PLL blocks and digital timing.',[
  F('Counter modulus','MOD = 2ⁿ','For an n-stage binary counter.'),
  F('Divide-by-2 stage','f_out=f_clk/2','Toggle flip-flop or equivalent stage.'),
  F('PLL phase error (small signal)','V_d ≈ K_d φ_e','K_d is phase-detector gain; φ_e in radians for this gain convention.')])
])

# --------------------------- YEAR 3 ---------------------------------
S('5EC501PC','Digital Signal Processing',3,'Semester I','ECE Core',[
 U('Discrete-time signals and LTI systems','Sequences, difference equations, impulse response and DTFT.',[
  F('Discrete-time convolution','y[n]=Σₖ x[k]h[n−k]','LTI input-output relation.'),
  F('DTFT','X(e^jω)=Σₙ₌₋∞∞x[n]e^(−jωn)','2π-periodic in ω.'),
  F('Parseval relation','Σₙ|x[n]|²=(1/2π)∫₋ππ|X(e^jω)|²dω','For finite-energy sequences.')]),
 U('DFT and FFT','DFT, IDFT, circular convolution and radix-2 FFT.',[
  F('N-point DFT','X[k]=Σₙ₌₀ᴺ⁻¹ x[n]e^(−j2πkn/N)','k=0,…,N−1.'),
  F('IDFT','x[n]=(1/N)Σₖ₌₀ᴺ⁻¹X[k]e^(j2πkn/N)','Same transform convention.'),
  F('Radix-2 FFT complexity','O(N log₂N)','For N a power of two.'),
  F('Circular convolution','y[n]=Σₘ₌₀ᴺ⁻¹x[m]h[(n−m) mod N]','N-point circular convolution.')]),
 U('Z-transform and digital filter structures','ROC, pole-zero analysis, direct/cascade/parallel forms.',[
  F('Z-transform','X(z)=Σₙ₌₋∞∞x[n]z^(−n)','Bilateral transform.'),
  F('Difference equation','y[n]+Σₖ₌₁ᴺaₖy[n−k]=Σₖ₌₀ᴹbₖx[n−k]','General causal rational IIR form.'),
  F('Transfer function','H(z)=(Σₖ₌₀ᴹbₖz^(−k))/(1+Σₖ₌₁ᴺaₖz^(−k))','Zero initial conditions.')]),
 U('IIR filter design','Butterworth/Chebyshev prototypes and bilinear transformation.',[
  F('Bilinear transformation','s=(2/T)(1−z⁻¹)/(1+z⁻¹)','T is the sampling period; frequency warping occurs.'),
  F('Butterworth magnitude-squared','|H(jΩ)|²=1/[1+(Ω/Ω_c)^(2N)]','Nth-order normalized low-pass prototype.'),
  F('Frequency prewarping','Ω=(2/T)tan(ω/2)','Bilinear transform prewarping; ω in rad/sample.')]),
 U('FIR filter design','Linear phase, window method and frequency-sampling method.',[
  F('FIR output','y[n]=Σₖ₌₀ᴹh[k]x[n−k]','Length M+1.'),
  F('Linear-phase symmetry','h[n]=h[M−n]','Symmetric FIR impulse response.'),
  F('FIR group delay','τ_g=M/2 samples','Symmetric/antisymmetric linear-phase FIR of order M.'),
  F('Windowed impulse response','h[n]=h_d[n]w[n]','Ideal impulse response h_d truncated/tapered by window w[n].')])
])

S('5EC502PC','IoT Architectures and Protocols',3,'Semester I','ECE Core',[
 U('IoT sensing and device layer','Sensors, actuators, signal conditioning, ADC and embedded node power.',[
  F('ADC quantization step','Δ≈V_FS/2ⁿ','n-bit ADC; full-scale input span V_FS.'),
  F('Sensor sensitivity','S=Δ(output)/Δ(input)','Local slope of the sensor transfer characteristic.'),
  F('Battery lifetime estimate','t≈Capacity(Ah)/I_avg(A)','Ideal constant-average-current estimate; real usable capacity depends on load and cutoff.')]),
 U('Connectivity and link budgets','Wireless links, path loss, antenna gains and received power.',[
  F('Free-space path loss','FSPL(dB)=32.44+20log₁₀(f_MHz)+20log₁₀(d_km)','Frequency in MHz and distance in km.'),
  F('Link budget','P_R=P_T+G_T+G_R−L_total','All quantities in dB/dBm with consistent reference.'),
  F('Received SNR','SNR(dB)=P_signal(dBm)−P_noise(dBm)','Signal and noise measured over the same bandwidth.')]),
 U('Network and application protocols','IPv4 addressing, throughput, latency, MQTT and CoAP messaging.',[
  F('IPv4 address count','2^h addresses','h host bits; usable host count depends on subnet reservation and special-purpose ranges.'),
  F('Goodput','Goodput = useful payload bits / elapsed time','Excludes retransmissions and protocol overhead.'),
  F('End-to-end latency','T_total = T_processing + T_queue + T_transmission + T_propagation','Per-hop terms sum across the path.')]),
 U('IoT data processing and cloud/edge','Sampling, storage sizing, reliability and edge/cloud distribution.',[
  F('Raw data rate','R = sample_rate × bits_per_sample × channels','Before framing/compression/overhead.'),
  F('Storage estimate','Storage = R × duration / 8','R in bit/s; result in bytes.'),
  F('Series reliability','R_total=ΠᵢRᵢ','Independent components in series; all must work.')]),
 U('Security, energy and deployment','Authentication, cryptographic overhead, duty cycle and energy budget.',[
  F('Duty cycle','D=t_on/(t_on+t_sleep)','For periodic operation.'),
  F('Average current','I_avg=D I_on+(1−D)I_sleep','Two-state approximation.'),
  F('Energy per event','E_event=V×I×t','Constant voltage/current approximation.')])
])

S('5EC503PC','CMOS VLSI Design',3,'Semester I','ECE Core',[
 U('MOS capacitor and MOSFET fundamentals','Threshold voltage, channel formation, regions and I–V behaviour.',[
  F('Long-channel NMOS saturation','I_D=(1/2)μ_nC_ox(W/L)(V_GS−V_TH)²','V_DS≥V_GS−V_TH; neglect channel-length modulation.'),
  F('Overdrive voltage','V_OV=V_GS−V_TH','For an enhanced MOSFET.'),
  F('Gate oxide capacitance','C_ox=ε_ox/t_ox','Capacitance per unit area.')]),
 U('CMOS inverter and logic gates','Voltage transfer characteristic, noise margins and static CMOS gates.',[
  F('Noise margins','NM_H=V_OH−V_IH;  NM_L=V_IL−V_OL','From specified input/output logic levels.'),
  F('CMOS static power (ideal)','P_static≈0','In steady logic states, excluding leakage and short-circuit current.'),
  F('Switching energy','E_switch≈C_LV_DD²','Approximate energy drawn from supply for a 0→1 charging event; convention-dependent factor for a full cycle.')]),
 U('CMOS circuit characteristics','Propagation delay, logical effort, fan-out and power dissipation.',[
  F('Dynamic power','P_dyn=αC_LV_DD²f','α activity factor; C_L effective switched capacitance.'),
  F('RC delay approximation','t_p≈0.69R_eqC_L','First-order single-pole model.'),
  F('Average propagation delay','t_p=(t_PLH+t_PHL)/2','Rise/fall propagation delays.'),
  F('Logical effort path delay','D=Σ(g_i h_i + p_i)','Logical-effort model; path effort and parasitics.')]),
 U('VLSI design and layout','Stick diagrams, design rules, scaling and interconnect.',[
  F('Area scaling','A ∝ L²','Ideal geometric scaling by linear scale factor L.'),
  F('Interconnect RC delay','t_RC≈R_wire C_wire','Lumped first-order estimate; distributed wires need Elmore/distributed models.'),
  F('Wire resistance','R=ρL/(wt)','Uniform rectangular conductor.')]),
 U('Semiconductor memories and testing','SRAM/DRAM cells, memory timing, yield and test concepts.',[
  F('Memory capacity','Capacity = 2ⁿ × w bits','n address bits and w data bits per word.'),
  F('Chip yield (simple model)','Y=e^(−D₀A)','Poisson defect-density model; D₀ defects/area and A die area.'),
  F('Defect-limited cost per good die','Cost_good≈Cost_die/Y','Simplified yield-only cost model.')])
])

S('5EC601PC','Antenna and Wave Propagation',3,'Semester II','ECE Core',[
 U('Radiation fundamentals','Radiation fields, power density, radiation intensity and pattern.',[
  F('Radiation intensity','U(θ,φ)=r²S_r','Far-field radial power density.'),
  F('Radiated power','P_rad=∫₀²π∫₀π U(θ,φ)sinθ dθ dφ','Integrate over full sphere.'),
  F('Directivity','D=4πU_max/P_rad','U_max is maximum radiation intensity.'),
  F('Gain','G=η_rad D','η_rad is radiation efficiency; excludes mismatch unless realized gain is specified.')]),
 U('Antenna parameters','Aperture, efficiency, polarization, impedance and bandwidth.',[
  F('Effective aperture','A_e=λ²G/(4π)','For a receiving antenna in the same direction/polarization.'),
  F('Friis transmission equation','P_R/P_T=G_TG_R(λ/(4πR))²','Far-field, free-space, matched and polarization-aligned antennas.'),
  F('Antenna efficiency','η= P_rad/P_in','Radiation efficiency; mismatch may be separately included.'),
  F('Half-power beamwidth','HPBW = angular width between −3 dB points','Measured from the radiation pattern.')]),
 U('Antenna arrays','Array factor, uniform linear arrays and beam steering.',[
  F('Uniform linear array factor','AF(θ)=Σₙ₌₀ᴺ⁻¹ Iₙe^(jnψ)','ψ=kd cosθ+β for one common endfire/broadside convention.'),
  F('Progressive phase for steering','β=−kd cosθ₀','For steering maximum toward θ₀ under the stated AF convention.'),
  F('Half-wave dipole length','L≈λ/2','Thin, center-fed resonant dipole approximation.')]),
 U('Radio-wave propagation','Ground, sky and space waves; reflection, diffraction and path loss.',[
  F('Wavelength','λ=c/f','In free space.'),
  F('Free-space path loss','L_FS(dB)=20log₁₀(4πR/λ)','R and λ use the same length unit.'),
  F('Friis received power','P_R=P_TG_TG_R(λ/(4πR))²','Same ideal free-space assumptions as the Friis equation.')]),
 U('Link engineering and propagation models','Fresnel zones, line-of-sight, link budgets and fading margins.',[
  F('First Fresnel-zone radius','r₁=√(λd₁d₂/(d₁+d₂))','At a point along a path; d₁,d₂ are distances to endpoints.'),
  F('Received power in dB','P_R(dBm)=P_T+G_T+G_R−L_path−L_misc','All gains/losses in dB and P_T in dBm.'),
  F('Doppler shift','f_D=(v/λ)cosθ','θ angle between motion direction and propagation direction.')])
])

S('5EC602PC','Wireless Communications',3,'Semester II','ECE Core',[
 U('Wireless channel and propagation','Large-scale path loss, shadowing, multipath and coherence.',[
  F('Log-distance path loss','PL(d)=PL(d₀)+10nlog₁₀(d/d₀)+X_σ','X_σ is zero-mean Gaussian in dB for log-normal shadowing.'),
  F('Doppler spread (maximum)','f_m=v/λ','Maximum magnitude when motion aligns with arrival direction.'),
  F('Coherence time approximation','T_c≈0.423/f_m','Common approximate definition; exact value depends on correlation threshold.')]),
 U('Fading and diversity','Rayleigh/Rician fading, outage, diversity and combining.',[
  F('Rayleigh envelope PDF','f_R(r)=(r/σ²)e^(−r²/(2σ²)), r≥0','Rayleigh fading amplitude; E[R²]=2σ².'),
  F('Diversity order','P_out ∝ SNR^(−L)','High-SNR asymptotic for L independent diversity branches under ideal combining.'),
  F('Selection combining output SNR','γ_SC=max(γ₁,…,γ_L)','Independent branches; select branch with largest instantaneous SNR.')]),
 U('Cellular systems and multiple access','Frequency reuse, handoff, FDMA/TDMA/CDMA and OFDMA basics.',[
  F('Hexagonal cluster size','N=i²+ij+j²','Co-channel cell spacing indices i,j are non-negative integers.'),
  F('Reuse ratio','Q=D/R=√(3N)','Ideal hexagonal cellular layout.'),
  F('Processing gain (spread spectrum)','G_p≈R_c/R_b','Chip rate R_c divided by bit rate R_b.')]),
 U('Wireless capacity and error performance','Shannon capacity, link adaptation, BER and coding gain.',[
  F('Shannon capacity','C=B log₂(1+SNR)','SNR is linear.'),
  F('BPSK in AWGN','P_b=Q(√(2E_b/N₀))','Coherent detection.'),
  F('FSPL','L_FS(dB)=20log₁₀(4πdf/c)','d in metres, f in Hz, c in m/s.')]),
 U('MIMO and modern wireless systems','MIMO channel, spatial multiplexing, OFDM and link budget.',[
  F('MIMO channel','y=Hx+n','Complex baseband narrowband model.'),
  F('MIMO spatial degrees of freedom','DoF≤min(N_T,N_R)','N_T transmit and N_R receive antennas.'),
  F('OFDM subcarrier spacing','Δf=1/T_u','Useful symbol duration T_u; cyclic prefix excluded.'),
  F('OFDM total symbol time','T_s=T_u+T_CP','Cyclic-prefix duration T_CP.')])
])

# --------------------------- YEAR 4 ---------------------------------
S('5EC701PC','Microwave and Optical Communications',4,'Semester I','ECE Core',[
 U('Microwave fundamentals and waveguides','Microwave bands, rectangular waveguide modes, cutoff and guide wavelength.',[
  F('Rectangular-waveguide cutoff','f_c=(c/(2√ε_rμ_r))√[(m/a)²+(n/b)²]','TE_mn/TM_mn mode; a is broad dimension and b narrow dimension.'),
  F('Guide wavelength','λ_g=λ₀/√(1−(f_c/f)²)','Propagating mode where f>f_c.'),
  F('Phase velocity in guide','v_p=c/√ε_rμ_r · 1/√(1−(f_c/f)²)','Ideal lossless guide.'),
  F('Microwave power density','S_avg=|E₀|²/(2η)','Peak phasor electric-field magnitude in a uniform plane wave.')]),
 U('Microwave components and sources','S-parameters, couplers, isolators, klystron and magnetron terms.',[
  F('S-parameter relation','b=S a','Power-wave vectors under the selected normalization.'),
  F('Return loss','RL=−20log₁₀|Γ| dB','Positive return-loss convention.'),
  F('Insertion loss','IL=−20log₁₀|S₂₁| dB','For a passive two-port with matched ports.'),
  F('VSWR','S=(1+|Γ|)/(1−|Γ|)','Reflection magnitude |Γ|<1.')]),
 U('Optical fibre fundamentals','Fibre types, acceptance cone, numerical aperture and dispersion.',[
  F('Numerical aperture','NA=√(n₁²−n₂²)','Step-index fibre, launch from air.'),
  F('Relative index difference','Δ=(n₁−n₂)/n₁','Weakly guiding approximation.'),
  F('Normalized frequency','V=(2πa/λ)NA','Core radius a; single-mode step-index cutoff V≈2.405.'),
  F('Attenuation coefficient','α(dB/km)=(10/L)log₁₀(P_in/P_out)','L in km.')]),
 U('Optical sources and detectors','LED/laser characteristics, photodiode responsivity and quantum efficiency.',[
  F('Photon energy','E=hν=hc/λ','Vacuum wavelength.'),
  F('Photodiode responsivity','R=ηq/(hν)=ηqλ/(hc)','Ideal external quantum efficiency η.'),
  F('Photocurrent','I_ph=R P_opt','At specified wavelength and optical power.'),
  F('Shot-noise current','i_n,rms=√(2qI B)','Poisson shot-noise model; one-sided bandwidth B convention.')]),
 U('Optical communication link design','Power budget, rise-time budget and receiver sensitivity.',[
  F('Received optical power (dB)','P_R(dBm)=P_T(dBm)−ΣL_i(dB)+ΣG_i(dB)','Include fibre, connector, splice and system margins.'),
  F('Power margin','M=P_R−P_sensitivity','Both in dBm; margin in dB.'),
  F('Rise-time budget','t_sys=√(t_tx²+t_fibre²+t_rx²)','Independent Gaussian-like broadening approximation.'),
  F('Bit rate from bit period','R_b=1/T_b','Binary signalling convention.')])
])

S('5EC702PC','Embedded System Design',4,'Semester I','ECE Core',[
 U('Embedded architecture and processors','CPU timing, memory maps, instruction execution and performance.',[
  F('CPU time','T_CPU=IC×CPI/f_clk','Instruction count IC and average CPI.'),
  F('Throughput','Throughput=completed tasks/time interval','Specify task unit and interval.'),
  F('Memory capacity','Capacity=2ⁿ×w bits','n address bits and w bits per word.')]),
 U('Real-time systems and scheduling','Task periods, utilization, deadlines and response-time concepts.',[
  F('CPU utilization','U=Σ(Cᵢ/Tᵢ)','Periodic independent tasks; Cᵢ execution time, Tᵢ period.'),
  F('Rate-monotonic utilization bound','U≤n(2^(1/n)−1)','Sufficient schedulability bound for n independent periodic tasks with deadlines equal to periods.'),
  F('Response time (fixed priority)','Rᵢ=Cᵢ+Bᵢ+Σ_{j∈hp(i)}⌈Rᵢ/Tⱼ⌉Cⱼ','Classic iterative response-time model; assumptions of fixed-priority preemptive scheduling.')]),
 U('Interrupts, timers and communication','Timer calculations, UART/SPI/I²C bit rate and interrupt timing.',[
  F('Timer tick','T_tick=prescaler/f_clk','For a timer whose counter clock is f_clk/prescaler.'),
  F('Timer period','T=(N−count_initial)T_tick','Overflow after the required number of timer increments.'),
  F('UART payload rate','R_payload=baud×data_bits/(bits_per_frame)','Framing overhead included in bits_per_frame.')]),
 U('Memory and peripheral interfacing','ADC/DAC scaling, GPIO, DMA and sensor/actuator interfacing.',[
  F('ADC ideal LSB','LSB=V_FS/2ⁿ','n-bit unipolar ADC.'),
  F('PWM duty cycle','D=t_on/T','0≤D≤1.'),
  F('Average PWM output','V_avg≈D V_high+(1−D)V_low','Ideal low-pass averaging of a two-level PWM waveform.')]),
 U('Low-power and embedded design','Energy, battery lifetime, power modes and reliability.',[
  F('Energy','E=VIt','Constant V and I over time t.'),
  F('Average power','P_avg=ΣᵢPᵢtᵢ/Σᵢtᵢ','For multiple operating states.'),
  F('Battery life estimate','t_life≈Capacity(Ah)/I_avg(A)','Ideal estimate; derating, self-discharge and cutoff reduce actual life.')])
])

# Professional electives and open electives from the JNTUH R25 subject list.
# Unit titles are concise syllabus-topic groupings; formulas are standard course relations.
electives = [
 ('5EC511PE','Computer Organization and Operating Systems',3,'Semester I','Elective I',[
  ('Computer arithmetic and representation',[F('Unsigned n-bit range','0 to 2ⁿ−1'),F('Two’s-complement range','−2ⁿ⁻¹ to 2ⁿ⁻¹−1')]),
  ('Processor performance',[F('CPU time','T=IC×CPI/f_clk'),F('Speedup','S=T_old/T_new'),F('Amdahl’s law','S=1/[(1−p)+p/s]','p is parallelizable fraction; s is speedup of that fraction.')]),
  ('Memory hierarchy',[F('Average memory access time','AMAT=Hit time + Miss rate × Miss penalty'),F('Cache hit ratio','h=hits/(hits+misses)')]),
  ('Pipelining and parallelism',[F('Ideal pipeline speedup','S≈k','k stages; long instruction stream and balanced stages.'),F('Pipeline throughput','≈1 cycle per instruction','Ideal fully occupied pipeline.')]),
  ('Operating-system scheduling',[F('Turnaround time','TAT=completion time−arrival time'),F('Waiting time','WT=TAT−CPU burst time'),F('CPU utilization','U=busy time/total time')])]),
 ('5EC512PE','Electronic Measurements and Instrumentation',3,'Semester I','Elective I',[
  ('Measurement errors and statistics',[F('Absolute error','e=x_measured−x_true'),F('Percentage error','e_r(%)=|e|/|x_true|×100'),F('Mean','x̄=Σxᵢ/n')]),
  ('Bridge measurements',[F('Wheatstone balance','R₁/R₂=R₃/R₄'),F('Unknown resistance','R_x=R₂R₃/R₄','For one common Wheatstone bridge arm assignment.')]),
  ('Transducers and sensors',[F('Sensitivity','S=Δoutput/Δinput'),F('Strain','ε=ΔL/L'),F('Gauge factor','GF=(ΔR/R)/ε')]),
  ('Digital instruments',[F('ADC resolution','LSB≈V_FS/2ⁿ'),F('Quantization error','|e_q|≤LSB/2')]),
  ('Signal conditioning and calibration',[F('Instrument accuracy class','Maximum permissible error (% of full scale)'),F('Loading error','e_L=(V_loaded−V_open)/V_open×100%')])]),
 ('5EC513PE','CMOS Fabrication Technology',3,'Semester I','Elective I',[
  ('Wafer and oxidation',[F('Oxide capacitance density','C_ox/A=ε_ox/t_ox'),F('Oxidation Deal–Grove form','x_ox²+A x_ox=B(t+τ)','Model constants depend on temperature and process.')]),
  ('Diffusion and ion implantation',[F('Fick’s first law','J=−D∂C/∂x'),F('Diffusion length','L_D=√(2Dt)','One-dimensional RMS diffusion distance convention.')]),
  ('Lithography and etching',[F('Resolution (Rayleigh)','CD=k₁λ/NA','Optical lithography approximation.'),F('Depth-to-width aspect ratio','AR=etch depth/feature width')]),
  ('Doping and junction formation',[F('Einstein relation','D/μ=kT/q'),F('Abrupt-junction depletion width','W=√[(2ε_s/q)(1/N_A+1/N_D)(V_bi−V_a)]','One-sided sign convention: V_a is forward bias; reverse bias increases depletion width.')]),
  ('Process integration and yield',[F('Defect-limited yield','Y≈e^(−D₀A)','Simple Poisson defect model.'),F('Sheet resistance','R_s=ρ/t','Uniform film of thickness t.')])]),
 ('5EC514PE','Sustainability for Electronics',3,'Semester I','Elective I',[
  ('Energy and power in electronics',[F('Electrical energy','E=Pt'),F('Power efficiency','η=P_out/P_in×100%'),F('Energy per bit','E_b=P/R_b')]),
  ('Life-cycle assessment',[F('Carbon intensity','CI=CO₂e/functional unit'),F('Embodied energy total','E_LCA=Σ stage energy')]),
  ('Thermal management',[F('Thermal resistance','R_θ=ΔT/P'),F('Junction temperature','T_j=T_a+P R_θJA')]),
  ('Battery and resource efficiency',[F('C-rate','C-rate=I/capacity(Ah)'),F('State of charge','SoC=remaining capacity/usable capacity×100%')]),
  ('Reliability and e-waste',[F('Arrhenius acceleration factor','AF=exp[(E_a/k)(1/T_use−1/T_stress)]','Temperatures in kelvin; same failure mechanism assumed.'),F('Mean time between failures','MTBF≈1/λ','Constant failure-rate model.')])]),
 ('5EC621PE','Computer Networks and Protocols',3,'Semester II','Elective II',[
  ('Data communication fundamentals',[F('Bit rate','R_b=1/T_b'),F('Transmission delay','T_tx=L/R'),F('Propagation delay','T_prop=d/v')]),
  ('Data link and error control',[F('Stop-and-wait utilization','U≈1/(1+2a)','Neglect ACK time; a=propagation time/transmission time.'),F('CRC relation','T(x)=xⁿM(x)+R(x)','R(x) is remainder modulo generator polynomial G(x).')]),
  ('Network and IP addressing',[F('IPv4 addresses per subnet','2^h','h host bits; usable count depends on subnet type.'),F('CIDR prefix','host bits=32−prefix_length')]),
  ('Transport and congestion control',[F('Bandwidth-delay product','BDP=bandwidth×RTT','Data bits in flight to fill the path.'),F('Throughput bound','T≤min(link rate, receiver window/RTT)')]),
  ('Wireless and application protocols',[F('Goodput','useful payload bits/time'),F('Round-trip time','RTT=T_forward+T_processing+T_reverse')])]),
 ('5EC622PE','Artificial Neural Networks and Deep Learning',3,'Semester II','Elective II',[
  ('Neuron models and activation',[F('Neuron output','y=φ(wᵀx+b)'),F('Sigmoid','σ(z)=1/(1+e^(−z))'),F('ReLU','ReLU(z)=max(0,z)')]),
  ('Loss functions',[F('Mean squared error','MSE=(1/N)Σ(yᵢ−ŷᵢ)²'),F('Binary cross-entropy','L=−[y log p+(1−y)log(1−p)]')]),
  ('Backpropagation and optimization',[F('Gradient descent','w←w−η∇_wL'),F('Chain rule','∂L/∂w=(∂L/∂y)(∂y/∂w)')]),
  ('Convolutional and recurrent networks',[F('2D convolution output size','O=⌊(I+2P−K)/S⌋+1','Per spatial dimension; kernel K, padding P and stride S.'),F('LSTM cell update','c_t=f_t⊙c_(t−1)+i_t⊙g_t','Standard LSTM cell-state relation.')]),
  ('Generalization and evaluation',[F('Precision','TP/(TP+FP)'),F('Recall','TP/(TP+FN)'),F('F1 score','2×Precision×Recall/(Precision+Recall)')])]),
 ('5EC623PE','Digital Signal Processors and Architectures',3,'Semester II','Elective II',[
  ('DSP architecture and fixed point',[F('Quantization step','Δ=FSR/2ⁿ'),F('Quantization error bound','|e_q|≤Δ/2')]),
  ('MAC and execution time',[F('Execution time','T=cycles/f_clk'),F('MAC throughput','MAC/s=operations per cycle×f_clk')]),
  ('Circular buffers and addressing',[F('Circular index','i_new=(i+1) mod N'),F('Buffer memory','M=N×word_bits')]),
  ('Pipelining and parallel DSP',[F('Ideal pipeline speedup','S≈number of stages'),F('Throughput','≈1 result/clock after pipeline fill')]),
  ('Fixed-point numerical effects',[F('Q-format scale','x_real=x_integer/2^F'),F('Quantization SNR (approx.)','SQNR_dB≈6.02n+1.76 dB','Full-scale sinusoid and ideal uniform quantizer.')])]),
 ('5EC624PE','Analog IC Design',3,'Semester II','Elective II',[
  ('MOS differential pair',[F('Differential pair tail current','I_D1+I_D2≈I_tail'),F('Differential transconductance','g_md≈g_m','For ideal matched pair under small differential input, output convention matters.')]),
  ('Current mirrors and biasing',[F('Current mirror ratio','I_out/I_ref≈(W/L)_out/(W/L)_ref'),F('MOS saturation current','I_D≈(1/2)μC_ox(W/L)V_OV²')]),
  ('Gain stages',[F('Common-source gain','A_v≈−g_m(r_o∥R_D)'),F('Intrinsic gain','A_v0≈g_m r_o')]),
  ('Frequency response and compensation',[F('Dominant-pole bandwidth','f_−3dB≈1/(2πR_eqC_eq)'),F('Unity-gain frequency','f_T≈g_m/(2πC_in)')]),
  ('Op-amp stability and performance',[F('Gain-bandwidth product','GBW≈A_0 f_p'),F('Phase margin','PM=180°+∠Aβ at |Aβ|=1')])]),
 ('5EC731PE','Digital Image Processing',4,'Semester I','Elective III',[
  ('Image representation and sampling',[F('Image storage','bits=N_xN_yb'),F('2D sampling rate','samples/frame=N_x×N_y')]),
  ('Spatial enhancement and filtering',[F('2D convolution','g(x,y)=ΣₘΣₙh(m,n)f(x−m,y−n)'),F('Mean filter','g(x,y)=(1/MN)Σ_neighborhood f(s,t)')]),
  ('Frequency-domain processing',[F('2D DFT','F(u,v)=ΣₓΣ_y f(x,y)e^(−j2π(ux/M+vy/N))'),F('Gaussian low-pass','H(u,v)=e^(−D²(u,v)/(2D₀²))')]),
  ('Image restoration and compression',[F('MSE','MSE=(1/MN)ΣₓΣ_y[f−g]²'),F('PSNR','PSNR=10log₁₀(MAX²/MSE) dB')]),
  ('Segmentation and morphology',[F('Thresholding','g(x,y)=1 if f(x,y)≥T, else 0'),F('Jaccard index','J(A,B)=|A∩B|/|A∪B|')])]),
 ('5EC732PE','Network Security and Cryptography',4,'Semester I','Elective III',[
  ('Number theory and modular arithmetic',[F('Modular congruence','a≡b (mod n) iff n divides (a−b)'),F('Euler totient for prime p','φ(p)=p−1')]),
  ('Symmetric-key cryptography',[F('Block-cipher idealization','C=E_K(P);  P=D_K(C)'),F('CBC encryption','C_i=E_K(P_i⊕C_(i−1)); C₀=IV')]),
  ('Public-key cryptography',[F('RSA modulus','n=pq'),F('RSA public exponent','gcd(e,φ(n))=1'),F('RSA decryption exponent','ed≡1 (mod φ(n))')]),
  ('Hashing and authentication',[F('HMAC','HMAC_K(m)=H((K′⊕opad)||H((K′⊕ipad)||m))'),F('Birthday bound','collision work≈2^(n/2)','For an ideal n-bit hash output.')]),
  ('Network security protocols',[F('Probability of brute-force success','P≈q/2ⁿ','q independent guesses against an ideal n-bit key.'),F('Entropy of a uniform key','H=n bits','For a uniformly random n-bit key.')])]),
 ('5EC733PE','Test and Testability',4,'Semester I','Elective III',[
  ('Fault models and coverage',[F('Fault coverage','FC=detected faults/total modeled faults×100%'),F('Defect level','DL=defective parts shipped/total parts shipped')]),
  ('Combinational ATPG',[F('Test efficiency','TE=detected faults/testable faults×100%'),F('Vector count','N_tests = number of applied test patterns')]),
  ('Scan design',[F('Scan-chain length','N_scan=number of scan flip-flops'),F('Scan shift cycles','cycles≈N_scan per pattern load/unload')]),
  ('Built-in self-test',[F('LFSR state evolution','s_(k+1)=A s_k over GF(2)'),F('Alias probability (idealized)','P_alias≈2^(−m)','For an m-bit signature under ideal random-error assumptions.')]),
  ('Reliability and diagnosis',[F('Failure rate','λ=failures/operating time'),F('Reliability','R(t)=e^(−λt)','Constant failure-rate model.')])]),
 ('5EC734PE','Biomedical Instrumentation',4,'Semester I','Elective III',[
  ('Bioelectric signals',[F('Biopotential differential signal','V_d=V_+−V_−'),F('Common-mode rejection ratio','CMRR=A_d/A_cm; CMRR_dB=20log₁₀(CMRR)')]),
  ('Biopotential amplifiers',[F('Instrumentation amplifier gain','G=1+2R/R_G','Three-op-amp topology with matched input-stage resistors.'),F('Input impedance','Z_in=V_in/I_in')]),
  ('ECG, EEG and EMG measurements',[F('Heart rate','HR=60/RR_interval','RR interval in seconds.'),F('Sampling condition','f_s>2f_max','Ideal bandlimited signal; clinical systems use practical margins.')]),
  ('Medical sensors and transducers',[F('Sensor sensitivity','S=Δoutput/Δinput'),F('Thermistor beta model','R(T)=R₀ exp[B(1/T−1/T₀)]','T and T₀ in kelvin; empirical model over a limited range.')]),
  ('Safety and signal processing',[F('Electrical power','P=VI'),F('RC cutoff frequency','f_c=1/(2πRC)')])]),
 ('5EC741PE','5G and Beyond Communications',4,'Semester I','Elective IV',[
  ('5G NR numerology and OFDM',[F('Subcarrier spacing','Δf=15×2^μ kHz','NR numerology μ.'),F('Useful OFDM symbol duration','T_u=1/Δf'),F('Resource blocks','12 subcarriers per resource block')]),
  ('Massive MIMO and beamforming',[F('Array steering phase','β=−kd sinθ₀','ULA convention when angle is measured from broadside.'),F('Beamforming output','y=wᴴx'),F('Array gain (ideal)','G_array≈N','N coherent elements under ideal conditions.')]),
  ('Radio propagation and link budget',[F('Free-space path loss','FSPL=20log₁₀(4πdf/c)'),F('Shannon capacity','C=B log₂(1+SNR)')]),
  ('Coding and modulation',[F('Spectral efficiency','η=R_b/B'),F('Effective code rate','R_c=k/n','k information bits in n coded bits.')]),
  ('Network slicing and performance',[F('Latency budget','T_total=ΣT_i'),F('Reliability target','P_success=1−P_failure')])]),
 ('5EC742PE','Adhoc Wireless Networks',4,'Semester I','Elective IV',[
  ('Ad hoc network fundamentals',[F('Network degree','d_i=number of one-hop neighbors of node i'),F('Average degree','d̄=2E/V','Undirected graph with E edges and V vertices.')]),
  ('Routing and route discovery',[F('Path cost','C_path=Σ hop_cost_i'),F('End-to-end delay','D_path=Σ per-hop delays')]),
  ('Medium access and contention',[F('Throughput efficiency','S=successful payload time/total channel time'),F('ALOHA throughput','S=Ge^(−2G)','Pure ALOHA under the standard offered-load model.')]),
  ('Mobility and energy',[F('Node speed','v=distance/time'),F('Energy per bit','E_b=P/R_b'),F('Network lifetime estimate','T≈E_initial/P_avg','Simplified average-power estimate.')]),
  ('Security and QoS',[F('Packet delivery ratio','PDR=packets_received/packets_sent×100%'),F('Goodput','useful bits received/time')])]),
 ('5EC743PE','AI for Communications',4,'Semester I','Elective IV',[
  ('Learning foundations',[F('Neuron output','y=φ(wᵀx+b)'),F('Gradient descent','w←w−η∇L')]),
  ('Channel estimation and prediction',[F('Least-squares estimate','ĥ=(XᴴX)⁻¹Xᴴy','Full column rank X.'),F('MSE','MSE=(1/N)Σ|h−ĥ|²')]),
  ('Resource allocation',[F('Shannon rate','R=B log₂(1+P|h|²/N₀B)'),F('Water-filling power','P_k=(μ−N_k/|h_k|²)^+','For parallel Gaussian channels with total power constraint.')]),
  ('Classification and anomaly detection',[F('Cross-entropy loss','L=−Σᵢyᵢlog pᵢ'),F('Precision','TP/(TP+FP)'),F('Recall','TP/(TP+FN)')]),
  ('Model evaluation and deployment',[F('Inference latency','T_infer=t_end−t_start'),F('Model size','bytes≈parameter_count×bytes_per_parameter')])]),
 ('5EC744PE','Biomedical Signal Processing',4,'Semester I','Elective IV',[
  ('Biomedical signal fundamentals',[F('Sampling condition','f_s>2f_max'),F('Signal-to-noise ratio','SNR=10log₁₀(P_signal/P_noise) dB')]),
  ('Digital filtering',[F('FIR filter','y[n]=Σₖh[k]x[n−k]'),F('IIR difference equation','y[n]=−Σₖa_ky[n−k]+Σₖb_kx[n−k]')]),
  ('ECG signal analysis',[F('Heart rate','HR=60/RR(s)'),F('RR variability','SDNN=standard deviation of normal-to-normal intervals')]),
  ('Time-frequency analysis',[F('Short-time Fourier transform','STFT{ x }(m,ω)=Σₙx[n]w[n−mH]e^(−jωn)'),F('Spectrogram','S(m,ω)=|STFT(m,ω)|²')]),
  ('Classification and clinical metrics',[F('Sensitivity','TP/(TP+FN)'),F('Specificity','TN/(TN+FP)'),F('Accuracy','(TP+TN)/(TP+TN+FP+FN)')])]),
 ('5EC851PE','Radar Systems',4,'Semester II','Elective V',[
  ('Radar equation and detection',[F('Monostatic radar equation','P_r=P_tG²λ²σ/[(4π)³R⁴L]','Far-field monostatic radar; L is total loss factor.'),F('Maximum range scaling','R_max ∝ (P_tG²λ²σ/S_min)^(1/4)','From the monostatic radar equation.')]),
  ('Range and resolution',[F('Range','R=cτ/2','Pulse round-trip time τ.'),F('Range resolution','ΔR=c/(2B)','Pulse-compression bandwidth B.')]),
  ('Doppler and MTI',[F('Doppler frequency','f_D=2v_r/λ','Monostatic radar; radial velocity v_r.'),F('Unambiguous range','R_u=c/(2 PRF)','Simple pulsed radar.'),F('Unambiguous velocity','v_u=λ PRF/4','Monostatic pulsed Doppler radar.')]),
  ('Antenna and tracking',[F('Antenna gain','G=4πA_e/λ²'),F('Angular tracking error','e_θ=θ_target−θ_beam')]),
  ('Radar signal processing',[F('Matched-filter SNR (ideal)','SNR_out≈2E/N₀','Real-passband AWGN convention; complex-baseband conventions may differ by a factor of 2.'),F('Doppler resolution','Δf_D≈1/T_coherent','Coherent processing interval T_coherent.')])]),
 ('5EC852PE','Computer Vision and Machine Learning',4,'Semester II','Elective V',[
  ('Image geometry and camera model',[F('Pinhole camera','u=fX/Z+c_x; v=fY/Z+c_y','Coordinates aligned to camera axes; pixel pitch absorbed into focal-length units.'),F('Homography','x′∼Hx','Planar projective mapping.')]),
  ('Feature extraction and matching',[F('Euclidean distance','d(x,y)=√Σᵢ(xᵢ−yᵢ)²'),F('Intersection over union','IoU=|A∩B|/|A∪B|')]),
  ('Machine-learning models',[F('Linear model','ŷ=wᵀx+b'),F('Logistic function','p=1/(1+e^(−z))')]),
  ('Neural networks and CNNs',[F('Convolution output size','O=⌊(I+2P−K)/S⌋+1'),F('ReLU','max(0,x)')]),
  ('Evaluation and deployment',[F('Precision','TP/(TP+FP)'),F('Recall','TP/(TP+FN)'),F('F1 score','2PR/(P+R)')])]),
 ('5EC853PE','Broadband Access Technologies',4,'Semester II','Elective V',[
  ('Access network fundamentals',[F('Shannon capacity','C=B log₂(1+SNR)'),F('Spectral efficiency','η=R_b/B')]),
  ('Optical access and PON',[F('Optical power budget','P_rx=P_tx−Σlosses'),F('Splitter ideal loss','L_split=10log₁₀(N) dB','Ideal 1:N splitter; excess loss is additional.')]),
  ('DSL and cable access',[F('Attenuation in dB','A=10log₁₀(P_in/P_out)'),F('Nyquist limit','R≤2B log₂M','Ideal noiseless baseband channel.')]),
  ('Wireless broadband',[F('FSPL','L_FS=20log₁₀(4πdf/c)'),F('Link margin','M=P_rx−P_sensitivity')]),
  ('QoS and network planning',[F('Throughput','T=payload bits/time'),F('Packet loss rate','PLR=lost packets/sent packets×100%')])]),
 ('5EC854PE','RF Circuit Design',4,'Semester II','Elective V',[
  ('RF network parameters',[F('Reflection coefficient','Γ=(Z_L−Z₀)/(Z_L+Z₀)'),F('Return loss','RL=−20log₁₀|Γ|'),F('VSWR','(1+|Γ|)/(1−|Γ|)')]),
  ('Impedance matching',[F('Quarter-wave transformer','Z_t=√(Z₀Z_L)','Real positive load; line length λ/4 at design frequency.'),F('Smith-chart normalized impedance','z=Z/Z₀')]),
  ('RF amplifiers and stability',[F('Power gain','G=P_out/P_in'),F('Available gain in dB','G_dB=10log₁₀G'),F('Rollet stability factor','K=(1−|S₁₁|²−|S₂₂|²+|Δ|²)/(2|S₁₂S₂₁|)','Two-port unconditional stability when K>1 and |Δ|<1.')]),
  ('Oscillators and mixers',[F('Oscillation condition','|Aβ|=1; ∠Aβ=2πk'),F('Mixer products','f_out=|m f_RF±n f_LO|','Ideal nonlinear mixing products; m,n are integers.')]),
  ('RF layout and noise',[F('Noise figure','F=SNR_in/SNR_out'),F('Thermal noise power','N=kTB'),F('Skin depth','δ=√(2/(ωμσ))','Good conductor approximation.')])]),
 ('5EC861PE','Satellite Communications',4,'Semester II','Elective VI',[
  ('Satellite orbits and geometry',[F('Circular orbital speed','v=√(μ/r)'),F('Orbital period','T=2π√(r³/μ)','r is distance from central-body centre; μ=GM.'),F('Geostationary period','T≈sidereal day','Circular equatorial orbit.')]),
  ('Satellite link budget',[F('Free-space loss','L_FS=20log₁₀(4πR/λ)'),F('EIRP','EIRP=P_T+G_T−L_T','dB/dBm convention.'),F('Carrier-to-noise density','C/N₀=EIRP−L_path+G/T−k','Consistent decibel units; k Boltzmann constant in dBW/K/Hz.')]),
  ('Earth station and antennas',[F('Antenna gain','G=η(πD/λ)²','Circular aperture diameter D.'),F('Beamwidth approximation','θ_3dB≈70λ/D degrees','Approximate parabolic aperture, D and λ in same units.')]),
  ('Modulation and multiple access',[F('Symbol rate','R_s=R_b/log₂M'),F('Occupied bandwidth (raised cosine)','B≈(1+α)R_s','One-sided baseband bandwidth.')]),
  ('Propagation and performance',[F('Rain attenuation','A_r=γ_R L_eff','Specific attenuation γ_R and effective path length L_eff.'),F('Link margin','M=(C/N)_actual−(C/N)_required','Same dB metric.')])]),
 ('5EC862PE','Quantum Technologies',4,'Semester II','Elective VI',[
  ('Quantum states and measurement',[F('Born rule','P(a)=|⟨a|ψ⟩|²'),F('State normalization','⟨ψ|ψ⟩=1')]),
  ('Qubits and gates',[F('Qubit state','|ψ⟩=α|0⟩+β|1⟩; |α|²+|β|²=1'),F('Hadamard gate','H=(1/√2)[[1,1],[1,−1]]'),F('Pauli-X gate','X=[[0,1],[1,0]]')]),
  ('Quantum circuits and entanglement',[F('CNOT action','|a,b⟩→|a,a⊕b⟩'),F('Bell state','|Φ⁺⟩=(|00⟩+|11⟩)/√2')]),
  ('Quantum algorithms',[F('Quantum Fourier transform','QFT|x⟩=(1/√N)Σ_y e^(2πixy/N)|y⟩'),F('Grover ideal iteration count','≈(π/4)√N','For one marked item among N items, asymptotic estimate.')]),
  ('Quantum communication and hardware',[F('Photon energy','E=hν'),F('Decoherence time ratio','Q≈ωT₂','Quality-factor-like relation; exact definition depends on platform.')])]),
 ('5EC863PE','Global Navigation Satellite Systems',4,'Semester II','Elective VI',[
  ('GNSS positioning fundamentals',[F('Pseudorange','ρ=c(Δt)+clock/error terms'),F('Geometric range','r=√[(x−x_s)²+(y−y_s)²+(z−z_s)²]')]),
  ('Satellite geometry and DOP',[F('Position solution','Δρ=HΔx+ε'),F('Covariance','Q=(HᵀWH)⁻¹'),F('Position DOP','PDOP=√(Q_xx+Q_yy+Q_zz)','From the position covariance geometry matrix under the chosen convention.')]),
  ('GNSS signals and codes',[F('Code chip duration','T_c=1/R_c'),F('Wavelength','λ=c/f')]),
  ('Error sources and augmentation',[F('Ionospheric first-order delay','ΔL≈40.3 TEC/f²','TEC in electrons/m² and f in Hz; delay in metres.'),F('Tropospheric mapping','ΔL(e)=ZHD·m_h(e)+ZWD·m_w(e)','Hydrostatic/wet zenith delays and mapping functions.')]),
  ('Receiver tracking and performance',[F('Doppler shift','f_D=−(v_r/c)f_c'),F('Carrier-to-noise density','C/N₀=P_C/N₀','Linear ratio in Hz; express in dB-Hz after 10log₁₀.')])]),
 ('5EC864PE','System on Chip Architecture',4,'Semester II','Elective VI',[
  ('SoC architecture and interconnect',[F('Bus throughput','T=bus_width×clock_rate'),F('Amdahl’s law','S=1/[(1−p)+p/s]')]),
  ('Memory hierarchy and caches',[F('Average access time','AMAT=hit_time+miss_rate×miss_penalty'),F('Cache lines','lines=cache_size/block_size')]),
  ('Power and thermal design',[F('Dynamic power','P_dyn=αCV²f'),F('Junction temperature','T_j=T_a+P R_θJA')]),
  ('Hardware/software co-design',[F('Execution time','T=cycles/f_clk'),F('Speedup','S=T_before/T_after')]),
  ('Verification and reliability',[F('Reliability for series blocks','R_total=ΠR_i'),F('Failure rate','λ=1/MTBF','Constant failure-rate approximation.')])]),
 ('5EC511OE','C++ for Electronic Design Automation',3,'Semester I','Open Elective I',[
  ('Programming foundations',[F('Array index address','base+i×sizeof(T)'),F('Time complexity','O(1), O(log n), O(n), O(n log n), O(n²)','Asymptotic growth classes, not exact runtime equations.')]),
  ('Object-oriented design',[F('Object size','sizeof(object)≥sum of member sizes','Padding/alignment and virtual members may add overhead.')]),
  ('Algorithms and data structures',[F('Binary search','T(n)=O(log n)'),F('Merge sort','T(n)=O(n log n)')]),
  ('EDA data representation',[F('Net degree','degree(net)=number of connected terminals'),F('Grid coordinate mapping','index=y×N_x+x','Zero-based row-major grid.')]),
  ('Automation and optimization',[F('Relative error','e_r=|x−x_ref|/|x_ref|'),F('Cost function','J=Σᵢwᵢcᵢ','Weighted cost objective; units/weights must be consistent.')])]),
 ('5EC512OE','Digital Electronics for Engineers',3,'Semester I','Open Elective I',[
  ('Number systems and codes',[F('n-bit unsigned range','0…2ⁿ−1'),F('Two’s-complement range','−2ⁿ⁻¹…2ⁿ⁻¹−1')]),
  ('Boolean algebra',[F('De Morgan','(A+B)′=A′B′; (AB)′=A′+B′'),F('Consensus theorem','AB+A′C+BC=AB+A′C')]),
  ('Combinational blocks',[F('Full adder','S=A⊕B⊕C_in; C_out=AB+AC_in+BC_in'),F('Decoder lines','2ⁿ outputs for n inputs')]),
  ('Sequential blocks',[F('D flip-flop','Q⁺=D'),F('Mod-n counter flip-flops','n_ff=⌈log₂N⌉')]),
  ('Programmable logic and timing',[F('Clock constraint','T_clk≥t_CQ+t_comb+t_setup+t_skew'),F('Dynamic power','P=αCV²f')])]),
 ('5EC621OE','Principles of Communications',3,'Semester II','Open Elective II',[
  ('Communication fundamentals',[F('Wavelength','λ=c/f'),F('SNR','SNR=P_s/P_n'),F('Noise power','N=kTB')]),
  ('Analog modulation',[F('AM modulation index','m=A_m/A_c'),F('AM bandwidth','BW=2f_m'),F('FM index','β=Δf/f_m')]),
  ('Pulse and digital modulation',[F('PCM bit rate','R_b=nf_s'),F('Symbol rate','R_s=R_b/log₂M')]),
  ('Noise and detection',[F('BPSK BER','P_b=Q(√(2E_b/N₀))'),F('Q-function','Q(x)=1/√(2π)∫ₓ∞e^(−u²/2)du')]),
  ('Information theory',[F('Shannon capacity','C=B log₂(1+SNR)'),F('Entropy','H=−Σpᵢlog₂pᵢ')])]),
 ('5EC622OE','Electronics for Automated Testing',3,'Semester II','Open Elective II',[
  ('Test system fundamentals',[F('Measurement uncertainty','u_c=√Σuᵢ²','For independent standard uncertainties.'),F('Repeatability standard deviation','s=√[Σ(xᵢ−x̄)²/(n−1)]')]),
  ('Sensors and signal conditioning',[F('Voltage divider','V_out=V_in R₂/(R₁+R₂)'),F('Op-amp non-inverting gain','A_v=1+R_f/R_1')]),
  ('Data acquisition',[F('Nyquist sampling','f_s>2f_max'),F('ADC LSB','LSB≈V_FS/2ⁿ')]),
  ('Automated test and control',[F('Test time','T_test=N_patterns×T_pattern'),F('Fault coverage','detected faults/total modeled faults×100%')]),
  ('Statistics and reliability',[F('Mean','x̄=Σxᵢ/n'),F('Standard deviation','s=√[Σ(xᵢ−x̄)²/(n−1)]')])]),
 ('5EC731OE','Measuring Instruments',4,'Semester I','Open Elective III',[
  ('Analog instruments',[F('Deflecting torque','T_d∝I²','For a moving-iron instrument under standard assumptions.'),F('PMMC torque','T_d=N B A I')]),
  ('Bridges and impedance',[F('Wheatstone balance','R₁/R₂=R₃/R₄'),F('Quality factor','Q=f₀/BW')]),
  ('Oscilloscopes and waveform measurement',[F('Frequency','f=1/T'),F('Peak-to-peak voltage','V_pp=V_max−V_min'),F('RMS for sinusoid','V_rms=V_p/√2')]),
  ('Digital meters and counters',[F('Counter frequency','f=N/T_gate'),F('Resolution','Δf≈1/T_gate')]),
  ('Calibration and uncertainty',[F('Percentage error','|x_m−x_t|/|x_t|×100%'),F('Combined uncertainty','u_c=√Σuᵢ²')])]),
 ('5EC732OE','Hardware for IoT Applications',4,'Semester I','Open Elective III',[
  ('Sensors and microcontrollers',[F('ADC quantization','LSB≈V_FS/2ⁿ'),F('Sensor sensitivity','S=Δoutput/Δinput')]),
  ('Power and battery design',[F('Average power','P_avg=ΣPᵢtᵢ/Σtᵢ'),F('Battery runtime','t≈Ah/I_avg')]),
  ('Wired and wireless interfaces',[F('UART frame time','T_frame=bits_per_frame/baud'),F('I²C clock period','T_SCL≈1/f_SCL')]),
  ('RF and antenna basics',[F('Wavelength','λ=c/f'),F('Free-space path loss','FSPL=20log₁₀(4πdf/c)')]),
  ('Firmware and system integration',[F('Duty cycle','D=t_on/T'),F('Energy per event','E=VIt')])])
]

for code,name,year,sem,group,units in electives:
    S(code,name,year,sem,group,[U(t, 'Topics and standard relations used in this elective.', fs) for t,fs in units],
      'Elective option in the JNTUH R25 ECE course structure. Unit headings are a concise topic map; match the detailed elective syllabus issued by your college before exam use.')

# Remaining core theory courses from the R25 structure. Some are conceptual rather
# than equation-heavy, so their units intentionally have no fabricated formulas.
S('5ME203ES','Engineering Graphics and Computer Aided Drafting',1,'Semester II','Foundation',[
 U('Engineering drawing basics and scales','Drawing conventions, dimensioning, lettering and scale construction.',[
  F('Representative fraction','RF = drawing length / actual length','Use consistent units.'),
  F('Scale length','drawing length = RF × actual length','For a uniform scale.')]),
 U('Orthographic projections','Principles of projection, reference planes and views.',[
  F('True-length scale','projected length = true length × cosθ','For a straight line inclined by θ to the projection plane; use the appropriate view geometry.')]),
 U('Projection of solids','Prisms, pyramids, cylinders, cones and their positions.',[]),
 U('Sections and development of surfaces','Sectional views, true shape, and development of common solids.',[
  F('Cylinder lateral development','rectangle width = πD; height = cylinder length','For a right circular cylinder.'),
  F('Cone slant height','l = √(r²+h²)','Right circular cone.')]),
 U('Isometric and computer-aided drafting','Isometric projection, pictorial views and CAD construction.',[
  F('Isometric length','isometric length ≈ 0.8165 × true length','For standard isometric projection; isometric drawing convention may use true lengths.')])
], 'Primarily a graphical subject; only common scale and geometry relations are listed.')

S('5EN205HS','English for Skill Enhancement',1,'Semester II','Foundation',[
 U('Communication fundamentals','Communication process, verbal/non-verbal communication and listening.',[]),
 U('Language and grammar','Sentence structure, vocabulary, grammar and usage.',[]),
 U('Technical reading and writing','Technical passages, summaries, reports and professional correspondence.',[]),
 U('Speaking and presentations','Group discussions, presentations and public speaking.',[]),
 U('Employability communication','Interviews, workplace interaction, resumes and professional etiquette.',[])
], 'Communication-skills subject; no standard engineering formula set applies.')

S('5MS306HS','Innovation and Entrepreneurship',2,'Semester I','Foundation',[
 U('Innovation and entrepreneurial thinking','Idea generation, opportunity recognition and design thinking.',[]),
 U('Business models and market discovery','Customer segments, value propositions, channels and market sizing.',[
  F('Market share','Market share = firm sales / total market sales × 100%'),
  F('Conversion rate','Conversion rate = conversions / qualified visits × 100%')]),
 U('Business operations and marketing','Cost structure, pricing, operations and customer acquisition.',[
  F('Gross margin','Gross margin = (Revenue − COGS) / Revenue × 100%'),
  F('Customer acquisition cost','CAC = acquisition spend / new customers acquired')]),
 U('Entrepreneurial finance','Revenue, contribution, break-even analysis and cash-flow basics.',[
  F('Contribution per unit','Contribution = selling price − variable cost per unit'),
  F('Break-even quantity','Q_BE = fixed costs / contribution per unit','Assumes constant unit price and variable cost.'),
  F('Break-even sales value','Sales_BE = fixed costs / contribution margin ratio')]),
 U('Business planning and venture growth','Business plans, funding, risk and performance indicators.',[
  F('Return on investment','ROI = (net gain / investment cost) × 100%'),
  F('Simple payback period','Payback = initial investment / annual net cash inflow','Assumes equal annual cash inflows.')])
])

S('5VA300ES','Environmental Science',2,'Semester I','Foundation',[
 U('Ecosystems and ecological principles','Ecosystem structure, energy flow, food chains and productivity.',[
  F('Ecological efficiency','η = energy transferred to next trophic level / energy at current level × 100%')]),
 U('Natural resources and sustainability','Water, land, forests, energy resources and conservation.',[
  F('Per-capita resource use','per-capita use = total resource use / population'),
  F('Population growth (continuous model)','N(t) = N₀e^(rt)','Constant per-capita growth rate r.')]),
 U('Environmental pollution and monitoring','Air/water pollution, dissolved oxygen, BOD and environmental indicators.',[
  F('BOD₅','BOD₅ = (D₁ − D₂) / P','D₁ initial DO, D₂ final DO in mg/L, P decimal fraction of sample in diluted mixture; standard dilution correction.'),
  F('Pollutant concentration after dilution','C₂ = C₁V₁/(V₁+V₂)','Ideal mixing with no reaction or volume change.'),
  F('pH','pH = −log₁₀[H⁺]','[H⁺] in mol/L.')]),
 U('Waste management and treatment','Solid waste, wastewater treatment, recycling and hazardous waste.',[
  F('Waste generation rate','G = mass of waste / (population × time)'),
  F('Removal efficiency','η_removal = (C_in − C_out)/C_in × 100%','Concentrations measured on the same basis.')]),
 U('Climate, impact and environmental management','Climate change, carbon footprint, EIA and environmental standards.',[
  F('Carbon footprint','CO₂e = Σ(activity data × emission factor)'),
  F('Global warming potential total','GWP_total = Σ(mass of gas_i × GWP_i)','Use the assessment-horizon GWP factors specified by the reporting standard.')])
])

S('5MS603HS','Business Economics and Financial Analysis',3,'Semester II','Foundation',[
 U('Demand, supply and elasticity','Demand/supply functions, market equilibrium and elasticity.',[
  F('Price elasticity of demand','E_d = (% change in quantity demanded) / (% change in price)'),
  F('Linear demand curve','Q_d = a − bP','a,b are positive constants in the simple linear model.')]),
 U('Production, cost and revenue','Production functions, cost curves, average/marginal cost and revenue.',[
  F('Total cost','TC = TFC + TVC'),
  F('Average cost','AC = TC/Q'),
  F('Marginal cost','MC = ΔTC/ΔQ'),
  F('Profit','π = TR − TC')]),
 U('Markets and pricing','Perfect competition, monopoly, monopolistic competition and oligopoly.',[
  F('Total revenue','TR = P×Q'),
  F('Average revenue','AR = TR/Q'),
  F('Marginal revenue','MR = ΔTR/ΔQ')]),
 U('Accounting and financial statements','Accounting ratios, working capital, depreciation and financial analysis.',[
  F('Current ratio','Current ratio = current assets / current liabilities'),
  F('Working capital','Working capital = current assets − current liabilities'),
  F('Straight-line depreciation','Annual depreciation = (cost − salvage value) / useful life')]),
 U('Capital budgeting and investment decisions','Time value of money, NPV, IRR, payback and profitability.',[
  F('Present value','PV = FV/(1+r)ⁿ'),
  F('Net present value','NPV = Σₜ₌₀ᴺ CF_t/(1+r)ᵗ','CF₀ is usually the initial negative investment.'),
  F('Future value','FV = PV(1+r)ⁿ'),
  F('Profitability index','PI = present value of future cash inflows / initial investment')])
])

S('5VA500HS','Indian Knowledge System',3,'Semester I','Foundation',[
 U('Sources and foundations','Historical sources, knowledge traditions and methods of transmission.',[]),
 U('Science, mathematics and astronomy','Historical developments in mathematics, astronomy and scientific thought.',[]),
 U('Technology, materials and engineering','Traditional technologies, metallurgy, architecture and crafts.',[]),
 U('Health, ecology and society','Knowledge traditions related to health, environment and social organisation.',[]),
 U('Contemporary relevance','Applications, preservation, ethics and interdisciplinary connections.',[])
], 'Humanities/interdisciplinary course; no standard ECE equation set applies.')

S('5MS703HS','Fundamentals of Management for Engineers',4,'Semester I','Foundation',[
 U('Management principles and functions','Planning, organising, staffing, directing and controlling.',[
  F('Productivity','Productivity = output / input'),
  F('Management efficiency','Efficiency = actual output / standard output × 100%')]),
 U('Planning and decision-making','Goals, forecasting, resource planning and decision analysis.',[
  F('Expected monetary value','EMV = Σ pᵢ × payoffᵢ','Mutually exclusive outcomes with probabilities summing to 1.')]),
 U('People and organisational behaviour','Motivation, leadership, teams and organisational structures.',[]),
 U('Operations and quality management','Capacity, inventory, quality, process improvement and project scheduling.',[
  F('Economic order quantity','EOQ = √(2DS/H)','D demand/year, S ordering cost/order, H holding cost/unit/year; classic EOQ assumptions.'),
  F('Overall equipment effectiveness','OEE = Availability × Performance × Quality','Each factor expressed as a fraction.'),
  F('Critical path duration','Project duration = length of the critical path','Activity-on-node/project network convention.')]),
 U('Project and financial control','Project costs, budgeting, break-even analysis and performance monitoring.',[
  F('Break-even quantity','Q_BE = fixed cost / (selling price − variable cost per unit)'),
  F('Cost variance','CV = earned value − actual cost'),
  F('Schedule variance','SV = earned value − planned value')])
])

# Attach key model and convention limits so approximate equations are not read as universal.
assumption_notes = {
 'Resonant peak (2nd order)': 'A resonant peak exists only for 0 < ζ < 1/√2 in the standard second-order model.',
 'Wien bridge frequency': 'Assumes equal resistors and equal capacitors in the frequency-selective bridge.',
 'Positive-real condition': 'This is a core condition, not the complete test; also check real-rational form, analyticity and pole/residue restrictions.',
 'Difference amplifier': 'Assumes an ideal op amp and matched resistor ratios in the two input arms.',
 'FIR linear-phase symmetry': 'For symmetric FIR coefficients (Types I/II); antisymmetric linear-phase designs use h[n] = −h[M−n].',
 'FIR group delay': 'For a linear-phase FIR filter; M is the filter order.',
 'Ideal PCM SQNR': 'For an ideal uniform quantizer and a full-scale sinusoidal input; excludes overload and implementation noise.',
 'QPSK bit error probability': 'For coherent Gray-coded QPSK in AWGN; this is the per-bit error probability.',
 'Long-channel MOSFET saturation current': 'Long-channel square-law model; ignores channel-length modulation, mobility degradation and short-channel effects.',
 'Long-channel NMOS saturation': 'Long-channel square-law model; ignores channel-length modulation, mobility degradation and short-channel effects.',
 'Poynting vector': 'Instantaneous fields; for time-harmonic peak phasors, average power density is (1/2) Re{E × H*}.',
 'Numerical aperture': 'Assumes the external medium is air (n₀ ≈ 1); generally n₀ sin θₐ = √(n₁² − n₂²).',
 'Half-wave dipole length': 'Ideal thin resonant dipole; a practical resonant length is often slightly below 0.5λ due to end effects.',
 'AM bandwidth': 'For a single tone; for a message with maximum frequency fₘ,max, use BW = 2fₘ,max.',
 'Shannon capacity': 'S/N must be a linear power ratio, not a value in dB; assumes an AWGN channel.',
 'Nyquist zero-ISI bit rate': 'Ideal noiseless, band-limited baseband channel with bandwidth B.',
 'Thevenin equivalent': 'Vₒc/Iₛc gives R_TH for a linear network measured at the same pair of terminals.',
 'Transfer function': 'Assumes zero initial conditions; distinguish the transfer function from a response with stored initial energy.',
 'Ideal DAC output': 'Ideal unipolar straight-binary convention; code range is 0 through 2ⁿ−1.',
 'ADC ideal LSB': 'Assumes a uniform n-bit converter and V_FS is the full-scale input span.',
 'ADC resolution': 'Assumes an n-bit converter and V_range is the full-scale input span.',
}
for subject in subjects:
    for unit in subject['units']:
        for formula in unit['formulas']:
            note = assumption_notes.get(formula['name'])
            if note and note not in formula.get('note', ''):
                formula['note'] = (formula.get('note', '').rstrip() + (' ' if formula.get('note') else '') + note)

# Add source and editorial metadata.
data = {
 'meta': {
  'title': 'ECE Formula Vault',
  'curriculum': 'JNTUH R25 B.Tech Electronics and Communication Engineering (Constituent Colleges)',
  'effective': 'Academic Year 2025–26 batch',
  'source_name': 'JNTUH R25 B.Tech ECE Course Structure & Syllabus',
  'source_url': 'https://jntuhces.ac.in/web/notifications/153_R25%20B.Tech%20%20ECE%20%20Course%20Structure%20and%20Syllabus.pdf',
  'university_syllabus_url': 'https://jntuh.ac.in/syllabus',
  'model_curriculum_url': 'https://www.aicte.gov.in/sites/default/files/Final_ECE.pdf',
  'editorial_note': 'Theory-course names and semester placement follow the JNTUH R25 ECE course structure. Lab courses, workshops, internships, projects and activity-only entries are not shown as five-unit formula subjects. Formula cards are a curated study reference, not a substitute for the official syllabus, textbook derivations, device datasheets or faculty conventions. Elective unit titles are concise topic groupings; elective offerings and unit details can vary by college.'
 },
 'subjects': subjects
}
with open(OUT,'w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=2)
print(f'Wrote {OUT}: {len(subjects)} subjects, {sum(len(s["units"]) for s in subjects)} units, {sum(len(u["formulas"]) for s in subjects for u in s["units"])} formula cards')
# Keep the browser bundle synchronized with data.json; GitHub Pages needs no fetch/API call.
js_out = os.path.join(os.path.dirname(__file__), 'assets', 'js', 'catalog.js')
with open(js_out, 'w', encoding='utf-8') as f:
    f.write('window.ECE_DATA = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n')
