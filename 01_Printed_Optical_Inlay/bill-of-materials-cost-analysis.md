---
title: "Bill of Materials, Stoichiometric Mixing Ratios, Mass Balance & USD Cost Analysis — Printed a-Si:H Optical Waveguide Inlay Bridge"
author: "Emanuel Schaaf"
framework: "Open Origin Architecture"
status: "Manufacturing & Economic Specification"
tags:
  - bill-of-materials
  - mass-balance
  - mixing-ratios
  - cost-analysis
  - silicon-photonics
  - TPU-9
---

# Printed $\text{a-Si:H}$ Optical Waveguide Inlay Bridge
**Bill of Materials, Mass & Volume Balance, Chemical Mixing Ratios, and Complete USD Cost Breakdown**

* **Lead Architect:** Emanuel Schaaf
* **Framework:** Open Origin Architecture
* **Reference Geometry:** Full Die-Flank Bridge ($L = 5.0\text{ mm}$, $W = 15.0\text{ mm}$, Footprint Area $A = 75.0\text{ mm}^2 = 0.75\text{ cm}^2$, $3000$ Waveguides, $192.0\text{ TB/s}$ Bidirectional Throughput)
* **Production Batch Reference:** $1,000$ Full-Flank Bridges (incorporating a $1.25\times$ slot-die/inkjet dispensing overfill factor)

---

## 1. Geometric Volume & Net Structural Mass Derivation (Single Bridge)

To establish the exact physical weight added to an accelerator package by a full-flank optical inlay bridge ($L = 5.0\text{ mm} = 0.50\text{ cm}$, $W = 15.0\text{ mm} = 1.50\text{ cm}$, area $A_{\text{bridge}} = 0.75\text{ cm}^2 = 75.0\text{ mm}^2$), the cured volume $V_i$ and net dry mass $m_{i,\text{net}} = \rho_i \cdot V_i$ of each functional layer are derived from first principles.

### 1.1 Layer-by-Layer Mass Equations

1. **Layer 1 — Cured DVS-BCB Planarization Prime Coat ($t_{\text{BCB}} = 2.00\text{ }\mu\text{m}$, $\rho_{\text{BCB}} = 1.05\text{ g/cm}^3$):**

$$
V_{\text{BCB}} = A_{\text{bridge}} \cdot t_{\text{BCB}} = 0.75\text{ cm}^2 \times 2.00 \times 10^{-4}\text{ cm} = 1.50 \times 10^{-4}\text{ cm}^3 = 0.15000\text{ mm}^3
$$

$$
m_{\text{BCB,net}} = V_{\text{BCB}} \cdot \rho_{\text{BCB}} = 1.50 \times 10^{-4}\text{ cm}^3 \times 1.05\text{ g/cm}^3 = 1.575 \times 10^{-4}\text{ g} = 157.50\text{ }\mu\text{g}
$$

2. **Layer 2 — Siloxane Elastomer Shear-Buffer ($h_{\text{buf}} = 20.00\text{ }\mu\text{m}$, $\rho_{\text{buf}} = 1.08\text{ g/cm}^3$):**

$$
V_{\text{buf}} = A_{\text{bridge}} \cdot h_{\text{buf}} = 0.75\text{ cm}^2 \times 2.00 \times 10^{-3}\text{ cm} = 1.50 \times 10^{-3}\text{ cm}^3 = 1.50000\text{ mm}^3
$$

$$
m_{\text{buf,net}} = V_{\text{buf}} \cdot \rho_{\text{buf}} = 1.50 \times 10^{-3}\text{ cm}^3 \times 1.08\text{ g/cm}^3 = 1.620 \times 10^{-3}\text{ g} = 1620.00\text{ }\mu\text{g}
$$

3. **Layer 3 — Bottom VUV-$\text{SiO}_2$ Optical Cladding ($t_{\text{clad,bot}} = 1.50\text{ }\mu\text{m}$, $\rho_{\text{SiO}_2} = 2.20\text{ g/cm}^3$):**

$$
V_{\text{clad,bot}} = 0.75\text{ cm}^2 \times 1.50 \times 10^{-4}\text{ cm} = 1.125 \times 10^{-4}\text{ cm}^3 = 0.11250\text{ mm}^3
$$

$$
m_{\text{clad,bot,net}} = 1.125 \times 10^{-4}\text{ cm}^3 \times 2.20\text{ g/cm}^3 = 2.475 \times 10^{-4}\text{ g} = 247.50\text{ }\mu\text{g}
$$

4. **Layer 4 — Imprinted $\text{a-Si:H}$ Waveguide Cores ($3000$ Ribs + Imprint Slab, $t_{\text{eff}} = 0.050\text{ }\mu\text{m}$, $\rho_{\text{a-Si:H}} = 2.25\text{ g/cm}^3$):**
The $3000$ waveguide cores ($w = 450\text{ nm}$, $h = 220\text{ nm}$, $L = 0.50\text{ cm}$) occupy a rib volume of $V_{\text{ribs}} = 3000 \times (4.5 \times 10^{-5}\text{ cm}) \times (2.2 \times 10^{-5}\text{ cm}) \times 0.50\text{ cm} = 1.485 \times 10^{-6}\text{ cm}^3$, plus the residual nanoimprint stabilization slab outside the etched routing zones ($V_{\text{slab}} = 2.265 \times 10^{-6}\text{ cm}^3$):

$$
V_{\text{a-Si:H,net}} = V_{\text{ribs}} + V_{\text{slab}} = 3.75 \times 10^{-6}\text{ cm}^3 = 0.00375\text{ mm}^3
$$

$$
m_{\text{a-Si:H,net}} = 3.75 \times 10^{-6}\text{ cm}^3 \times 2.25\text{ g/cm}^3 = 8.4375 \times 10^{-6}\text{ g} \approx 8.44\text{ }\mu\text{g}
$$

5. **Layer 5 — Top VUV-$\text{SiO}_2$ Passivation Cladding ($t_{\text{clad,top}} = 1.28\text{ }\mu\text{m}$ average, $\rho_{\text{SiO}_2} = 2.20\text{ g/cm}^3$):**

$$
V_{\text{clad,top}} = 0.75\text{ cm}^2 \times 1.28 \times 10^{-4}\text{ cm} = 0.960 \times 10^{-4}\text{ cm}^3 = 0.09600\text{ mm}^3
$$

$$
m_{\text{clad,top,net}} = 0.960 \times 10^{-4}\text{ cm}^3 \times 2.20\text{ g/cm}^3 = 2.112 \times 10^{-4}\text{ g} = 211.20\text{ }\mu\text{g}
$$

6. **Layer 6 — Dual Index-Matched Silicone Socket Pads ($2 \times 0.15\text{ mm} \times 15.0\text{ mm}$, $t_{\text{pad}} = 2.00\text{ }\mu\text{m}$, $\rho_{\text{pad}} = 1.12\text{ g/cm}^3$):**
Total pad area $A_{\text{pads}} = 2 \times 0.015\text{ cm} \times 1.50\text{ cm} = 0.045\text{ cm}^2$:

$$
V_{\text{pads}} = 0.045\text{ cm}^2 \times 2.00 \times 10^{-4}\text{ cm} = 9.00 \times 10^{-6}\text{ cm}^3 = 0.00900\text{ mm}^3
$$

$$
m_{\text{pads,net}} = 9.00 \times 10^{-6}\text{ cm}^3 \times 1.12\text{ g/cm}^3 = 1.008 \times 10^{-5}\text{ g} = 10.08\text{ }\mu\text{g}
$$

### 1.2 Weight & Volume Table (Single $15\text{ mm} \times 5\text{ mm}$ Bridge)

| Structural Layer | Cured Material | Thickness | Net Volume | Net Dry Mass |
| :--- | :--- | :--- | :--- | :--- |
| **1. Base Planarizer** | Crosslinked DVS-BCB | $2.00\text{ }\mu\text{m}$ | $0.15000\text{ mm}^3$ | $157.50\text{ }\mu\text{g}$ |
| **2. Shear Buffer** | PDMS-PDPS Elastomer | $20.00\text{ }\mu\text{m}$ | $1.50000\text{ mm}^3$ | $1620.00\text{ }\mu\text{g}$ |
| **3. Bottom Cladding** | VUV-Derived $\text{SiO}_2$ | $1.50\text{ }\mu\text{m}$ | $0.11250\text{ mm}^3$ | $247.50\text{ }\mu\text{g}$ |
| **4. Waveguide Cores** | Passivated $\text{a-Si:H}$ | $0.22\text{ }\mu\text{m}$ | $0.00375\text{ mm}^3$ | $8.44\text{ }\mu\text{g}$ |
| **5. Top Cladding** | VUV-Derived $\text{SiO}_2$ | $1.28\text{ }\mu\text{m}$ | $0.09600\text{ mm}^3$ | $211.20\text{ }\mu\text{g}$ |
| **6. Socket Interface** | Phenyl-Methyl Silicone | $2.00\text{ }\mu\text{m}$ | $0.00900\text{ mm}^3$ | $10.08\text{ }\mu\text{g}$ |
| **Total Bridge Stack** | **Complete 6-Layer Inlay** | **$27.00\text{ }\mu\text{m}$** | **$1.87125\text{ mm}^3$** | **$2254.72\text{ }\mu\text{g}$** |

*Explanation of Structural Weight:* A complete $15.0\text{ mm}$ wide optical inlay bridge capable of transporting $192.0\text{ TB/s}$ bidirectionally adds a total dry weight of only **$2.255\text{ mg}$** ($2.255\text{ g}$ per $1,000$ bridges). Out of this total mass, $71.8\%$ ($1620.00\text{ }\mu\text{g}$) consists of the $20\text{ }\mu\text{m}$ compliant elastomer buffer, while the active optical $\text{SiO}_2/\text{a-Si:H}/\text{SiO}_2$ waveguide stack weighs just **$467.14\text{ }\mu\text{g}$**.

---

## 2. Exact Chemical Mixing Ratios & Stoichiometric Formulations

To achieve reproducible slot-die/inkjet rheology, zero crack formation during VUV curing, and the exact target mechanical and optical constants ($G_{\text{buf}} = 50\text{ MPa}$, $n_{\text{core}} = 3.48$, $n_{\text{clad}} = 1.444$, $n_{\text{pad}} = 1.500$), the seven process formulations must be prepared according to the following exact mixing ratios.

### 2.1 Formulation 1: Liquid Silicon Core Ink ($\text{Si}_5\text{H}_{10}$ in Anhydrous Cyclooctane)
Pure liquid cyclopentasilane ($\text{Si}_5\text{H}_{10}$, $\rho_{\text{CPS}} = 0.963\text{ g/cm}^3$, $M_{\text{CPS}} = 150.505\text{ g/mol}$) has a low surface tension and oxidizes spontaneously in air. To achieve a slot-die dynamic viscosity of $\eta = 8.0\text{ mPa}\cdot\text{s}$ and uniform $280\text{ nm}$ wet-film leveling, it is diluted in anhydrous, deoxygenated cyclooctane ($\text{C}_8\text{H}_{16}$, $\rho_{\text{CO}} = 0.834\text{ g/cm}^3$, $M_{\text{CO}} = 112.216\text{ g/mol}$).

* **Target Volume Ratio:** $35.0\text{ vol\% }\text{Si}_5\text{H}_{10}$ : $65.0\text{ vol\% }\text{C}_8\text{H}_{16}$
* **Derivation of Exact Weight Ratio ($\text{wt\%}$):**
  For a $100.0\text{ cm}^3$ batch of ink:

$$
m_{\text{CPS}} = 35.0\text{ cm}^3 \times 0.963\text{ g/cm}^3 = 33.705\text{ g}
$$

$$
m_{\text{CO}} = 65.0\text{ cm}^3 \times 0.834\text{ g/cm}^3 = 54.210\text{ g}
$$

$$
m_{\text{ink,total}} = 33.705\text{ g} + 54.210\text{ g} = 87.915\text{ g} \implies \rho_{\text{ink}} = 0.87915\text{ g/cm}^3
$$

$$
w_{\text{CPS}} = \frac{33.705\text{ g}}{87.915\text{ g}} = 0.38338 \quad (38.34\text{ wt\% }\text{Si}_5\text{H}_{10})
$$

$$
w_{\text{CO}} = \frac{54.210\text{ g}}{87.915\text{ g}} = 0.61662 \quad (61.66\text{ wt\% }\text{C}_8\text{H}_{16})
$$

* **Molar Ratio:** $n_{\text{CPS}} = \frac{33.705}{150.505} = 0.22395\text{ mol}$ to $n_{\text{CO}} = \frac{54.210}{112.216} = 0.48309\text{ mol}$, giving a molar ratio of **$1.000\text{ mol }\text{Si}_5\text{H}_{10} : 2.157\text{ mol }\text{C}_8\text{H}_{16}$** (Mass ratio $1.000 : 1.608$).

### 2.2 Formulation 2: VUV-Silica Cladding Ink (PHPS in Anhydrous Di-n-butyl Ether)
Perhydropolysilazane ($\text{-[SiH}_2\text{-NH]-}_n$, $\rho_{\text{PHPS}} = 1.30\text{ g/cm}^3$, $M_{\text{monomer}} = 45.116\text{ g/mol}$) is dissolved in anhydrous di-n-butyl ether ($\text{C}_8\text{H}_{18}\text{O}$, $\rho_{\text{DBE}} = 0.764\text{ g/cm}^3$, $M_{\text{DBE}} = 130.231\text{ g/mol}$).

* **Target Weight Ratio:** $20.00\text{ wt\%}$ PHPS polymer : $80.00\text{ wt\%}$ Di-n-butyl Ether (Mass ratio **$1.00 : 4.00$**).
* **Derivation of Volume Ratio and Wet Ink Requirement:**
  For $100.0\text{ g}$ of cladding ink ($20.0\text{ g}$ PHPS + $80.0\text{ g}$ DBE):

$$
V_{\text{ink}} = \frac{20.0\text{ g}}{1.30\text{ g/cm}^3} + \frac{80.0\text{ g}}{0.764\text{ g/cm}^3} = 15.385\text{ cm}^3 + 104.712\text{ cm}^3 = 120.097\text{ cm}^3 \implies \rho_{\text{ink}} = 0.8327\text{ g/cm}^3
$$

  This corresponds to **$12.81\text{ vol\%}$ PHPS : $87.19\text{ vol\%}$ Di-n-butyl Ether**.
  Since $1.000\text{ g}$ of dry PHPS yields $1.3318\text{ g}$ of dense $\text{SiO}_2$, each $1.000\text{ g}$ of cured $\text{SiO}_2$ cladding requires $\frac{1.000\text{ g}}{1.3318} = 0.7509\text{ g}$ of dry PHPS, or $\frac{0.7509\text{ g}}{0.20} = 3.754\text{ g}$ of $20\text{ wt\%}$ PHPS ink.

### 2.3 Formulation 3: Elastomer Shear-Buffer ($G_{\text{buf}} = 50\text{ MPa}$ PDMS-PDPS System)
Standard polydimethylsiloxane (PDMS) has a shear modulus of only $0.3\text{–}1.0\text{ MPa}$, which would allow excessive vertical deflection during wire/die bonding. To raise the shear modulus to exactly $G_{\text{buf}} = 50\text{ MPa}$ while preserving thermal stability up to $250\text{ }^\circ\text{C}$, diphenylsiloxane units and surface-treated fumed nanosilica are incorporated into a solventless 3-part addition-cure formulation:

* **Component A (Base Polymer, $75.00\text{ wt\%}$):** Vinyl-terminated polydimethylsiloxane-co-diphenylsiloxane copolymer containing $35.0\text{ mol\%}$ diphenylsiloxane units ($M_w \approx 28,000\text{ g/mol}$, vinyl content $0.18\text{ mmol/g}$).
* **Component B (Reinforcing Filler & Crosslinker Blend, $24.90\text{ wt\%}$):** $18.40\text{ wt\%}$ hexamethyldisilazane-treated fumed silica nanoparticles ($d_{50} = 12\text{ nm}$, index-matched to prevent scattering) pre-dispersed with $6.50\text{ wt\%}$ trimethylsilyl-terminated polymethylhydrosiloxane-co-dimethylsiloxane crosslinker ($\text{Si-H}$ content $2.40\text{ mmol/g}$).
* **Component C (Hydrosilylation Catalyst, $0.10\text{ wt\%}$):** Karstedt's platinum(0)-divinyltetramethyldisiloxane complex diluted in cyclic methylvinylsiloxanes ($1.5\text{ wt\% Pt}$ solution, yielding $15\text{ ppm}$ elemental $\text{Pt}$ in the total formulation).
* **Stoichiometric Hydride-to-Vinyl Ratio ($r_{\text{H/V}}$):**

$$
r_{\text{H/V}} = \frac{m_B \cdot c_{\text{Si-H}}}{m_A \cdot c_{\text{Vinyl}}} = \frac{0.0650\text{ g} \times 2.40\text{ mmol/g}}{0.7500\text{ g} \times 0.18\text{ mmol/g}} = \frac{0.1560\text{ mmol}}{0.1350\text{ mmol}} = 1.156 \quad (\text{Ratio } 1.16 : 1.00)
$$

* **Practical Two-Kit Mixing Ratio:** When Component B and Component C are pre-blended as Curing Agent Kit B*, the mixing ratio is exactly **$3.00\text{ parts}$ Base A : $1.00\text{ part}$ Curing Agent B* by weight** ($75.0\text{ wt\%} : 25.0\text{ wt\%}$).

### 2.4 Formulation 4: Reversible Optical Socket Pad ($n_{\text{pad}} = 1.500$, Shore OO 35)
To match the refractive index of the $\text{SiO}_2$ cladding ($n = 1.444$) and expand the nanotaper mode while remaining soft enough to wet the chip interface reversibly under gentle mechanical seating pressure:

* **Part A (Base, $90.91\text{ wt\%}$):** Vinyl-terminated polyphenylmethylsiloxane ($22.0\text{ mol\%}$ phenyl groups, tuning refractive index to $n = 1.500$ at $\lambda = 1550\text{ nm}$) containing $10\text{ ppm}$ Pt catalyst.
* **Part B (Crosslinker, $9.09\text{ wt\%}$):** Hydride-terminated polyphenylmethylsiloxane crosslinker formulated at a slightly sub-stoichiometric hydride-to-vinyl molar ratio of **$r_{\text{H/V}} = 0.95 : 1.00$** to produce a compliant, tack-free Shore OO 35 elastomer gel.
* **Weight Mixing Ratio:** **$10.00 : 1.00$ (Part A : Part B by weight)**.

### 2.5 Formulation 5: Cavity Planarizer Ink (DVS-BCB in Mesitylene)
* **Weight Mixing Ratio:** **$40.00\text{ wt\%}$** B-staged Divinylsiloxane-bis-benzocyclobutene (DVS-BCB) oligomer : **$60.00\text{ wt\%}$** high-purity Mesitylene ($1,3,5$-trimethylbenzene, $\rho = 0.864\text{ g/cm}^3$), equivalent to a **$1.00 : 1.50$ mass ratio**.

### 2.6 Formulation 6 & 7: Process & Reaction Gas Mixtures
* **Photonic Curing Forming Gas:** **$90.00\text{ vol\% }\text{N}_2 + 10.00\text{ vol\% }\text{H}_2$** (molar ratio $9.00 : 1.00$). By molecular weight ($M_{\text{N}_2} = 28.014\text{ g/mol}$, $M_{\text{H}_2} = 2.016\text{ g/mol}$), the mass ratio is **$99.21\text{ wt\% }\text{N}_2 : 0.79\text{ wt\% }\text{H}_2$**.
* **VUV Photo-Oxidation Atmosphere:** **$97.00\text{ vol\% }\text{O}_2 + 3.00\text{ vol\% }\text{H}_2\text{O}$ vapor** at $140\text{ }^\circ\text{C}$ ($M_{\text{O}_2} = 31.998\text{ g/mol}$, $M_{\text{H}_2\text{O}} = 18.015\text{ g/mol}$), corresponding to **$98.29\text{ wt\% }\text{O}_2 : 1.71\text{ wt\% }\text{H}_2\text{O}$**.

### 2.7 Summary Table of Mixing Ratios

| Formulation Name | Primary Active | Co-Reactant / Solvent | Weight Ratio (wt%) | Volume or Molar Ratio |
| :--- | :--- | :--- | :--- | :--- |
| **1. Core Ink** | $\text{Si}_5\text{H}_{10}$ | Anhydrous Cyclooctane | $38.34\% : 61.66\%$ | $35.0\% : 65.0\%\text{ vol}$ |
| **2. Cladding Ink** | PHPS Polymer | Di-n-butyl Ether | $20.00\% : 80.00\%$ | $12.8\% : 87.2\%\text{ vol}$ |
| **3. Shear Buffer** | PDMS-PDPS Base | Silica/Crosslinker + Pt | $75.00\% : 25.00\%$ | $1.16 : 1.00\text{ Si-H/Vinyl}$ |
| **4. Socket Pad** | Phenyl-Vinyl Base | Hydride Crosslinker | $90.91\% : 9.09\%$ | $0.95 : 1.00\text{ Si-H/Vinyl}$ |
| **5. Planarizer Ink** | DVS-BCB Resin | Mesitylene Solvent | $40.00\% : 60.00\%$ | $1.00 : 1.50\text{ mass}$ |
| **6. Forming Gas** | Nitrogen ($\text{N}_2$) | Hydrogen ($\text{H}_2$) | $99.21\% : 0.79\%$ | $90.0\% : 10.0\%\text{ mol}$ |
| **7. VUV Gas** | Oxygen ($\text{O}_2$) | Water Vapor ($\text{H}_2\text{O}$) | $98.29\% : 1.71\%$ | $97.0\% : 3.0\%\text{ mol}$ |

---

## 3. Bill of Materials & Gross Quantity Table (Per 1,000-Bridge Batch)

In industrial slot-die and inkjet production, dispensing heads require line priming and a $25\%$ overfill allowance ($\eta_{\text{disp}} = 1.25$). Furthermore, for the $\text{a-Si:H}$ waveguide layer, a continuous $280\text{ nm}$ wet $\text{Si}_5\text{H}_{10}$ film is printed across the full $0.75\text{ cm}^2$ cavity ($m_{\text{CPS,film}} = 20.22\text{ }\mu\text{g}$ per bridge before UV-NIL and decalin rinse, or $20.22\text{ }\mu\text{g} \times 1.25 = 25.28\text{ }\mu\text{g}$ gross per bridge).

| Material / Chemical | Chemical Formula / Spec | Gross Mass (1 Bridge) | Gross Mass (1,000 Bridges) | Batch Volume (1,000 Bridges) |
| :--- | :--- | :--- | :--- | :--- |
| **Cyclopentasilane** | $\text{Si}_5\text{H}_{10}$ ($99.999\%$ Pure) | $25.28\text{ }\mu\text{g}$ | $25.28\text{ mg}$ | $0.0263\text{ mL}$ |
| **Cyclooctane Solvent** | $\text{C}_8\text{H}_{16}$ (Anhydrous) | $40.65\text{ }\mu\text{g}$ | $40.65\text{ mg}$ | $0.0487\text{ mL}$ |
| **PHPS Polymer** | $\text{-[SiH}_2\text{-NH]-}_n$ ($99.99\%$) | $430.53\text{ }\mu\text{g}$ | $430.53\text{ mg}$ | $0.3312\text{ mL}$ |
| **Di-n-butyl Ether** | $\text{C}_8\text{H}_{18}\text{O}$ (Anhydrous) | $1722.12\text{ }\mu\text{g}$ | $1722.12\text{ mg}$ | $2.2541\text{ mL}$ |
| **PDMS-PDPS Buffer Kit** | $3:1$ Base + Crosslinker/$\text{SiO}_2$ | $2025.00\text{ }\mu\text{g}$ | $2025.00\text{ mg}$ | $1.8750\text{ mL}$ |
| **DVS-BCB Resin** | $40\text{ wt\%}$ Solid fraction | $196.88\text{ }\mu\text{g}$ | $196.88\text{ mg}$ | $0.1875\text{ mL}$ |
| **Mesitylene Solvent** | $\text{C}_9\text{H}_{12}$ ($60\text{ wt\%}$ fraction) | $295.31\text{ }\mu\text{g}$ | $295.31\text{ mg}$ | $0.3418\text{ mL}$ |
| **Socket Pad Silicone** | Phenyl-Methyl ($10:1$ Kit) | $12.60\text{ }\mu\text{g}$ | $12.60\text{ mg}$ | $0.0113\text{ mL}$ |
| **Anhydrous Decalin** | $\text{C}_{10}\text{H}_{18}$ (S-Bend Developer) | $15.00\text{ mg}$ | $15.00\text{ g}$ | $16.74\text{ mL}$ |
| **Buffered Oxide Etch** | $6:1\text{ NH}_4\text{F}/\text{HF}$ Window Etch | $10.00\text{ mg}$ | $10.00\text{ g}$ | $8.85\text{ mL}$ |
| **Process Gases (6N)** | $\text{N}_2/\text{H}_2,\;\text{O}_2/\text{H}_2\text{O},\;\text{CF}_4$ | $120.00\text{ mg}$ | $120.00\text{ g}$ | $96.50\text{ L (STP)}$ |
| **Total Gross Inputs** | **All Dispensed + Process Media** | **$149.75\text{ mg}$** | **$149.75\text{ g}$** | **—** |

*Explanation of Material Quantities:* The combined gross mass of all functional inks dispensed across **1,000 full-flank bridges** (Items 1–8) is just **$4.748\text{ g}$** ($4748.37\text{ mg}$, or $\sim 5.08\text{ mL}$ of liquid precursors). Even highly expensive electronic-grade Cyclopentasilane ($\text{Si}_5\text{H}_{10}$) requires only **$25.28\text{ mg}$** to manufacture $1,000$ bridges, because the core layer is only $220\text{ nm}$ thin.

---

## 4. Complete Cost Breakdown in USD ($) with Total Sum

The economic calculation below is divided into:
* **Part A:** Direct Chemical, Precursor, and Consumable Material Costs.
* **Part B:** Cleanroom Fabrication, Lithography, Laser Micromachining, and Tooling Amortization Costs.
* **Part C:** Optional On-Die Electro-Optic Transceiver & Comb-Laser Overhead (for an end-to-end active comparison against monolithic interposers and pluggable optics).

### 4.1 Direct Material & Fab Manufacturing Cost Table (Passive Inlay Bridge)

| Cost Category / Item | Unit Price Basis | Batch Cost (1,000 Bridges) | Unit Cost (15 mm Bridge) | Unit Cost (1.6 mm Bridge) |
| :--- | :--- | :--- | :--- | :--- |
| **1. $\text{Si}_5\text{H}_{10}$ Core Ink ($65.93\text{ mg}$)** | $\$180.00\text{ / g }\text{Si}_5\text{H}_{10}$ + Ampoule | $\$12.50$ | $\$0.0125$ | $\$0.0013$ |
| **2. PHPS Cladding Ink ($2.153\text{ g}$)** | $\$24.00\text{ / g}$ PHPS Solution | $\$15.50$ | $\$0.0155$ | $\$0.0017$ |
| **3. PDMS-PDPS Shear Buffer ($2.025\text{ g}$)** | $\$8.00\text{ / g}$ Optical Kit | $\$16.20$ | $\$0.0162$ | $\$0.0017$ |
| **4. DVS-BCB Planarizer ($0.492\text{ g}$)** | $\$15.00\text{ / g}$ Solution | $\$7.38$ | $\$0.0074$ | $\$0.0008$ |
| **5. Optical Socket Pads ($12.60\text{ mg}$)** | $\$45.00\text{ / g}$ + Micro-Liner | $\$4.50$ | $\$0.0045$ | $\$0.0005$ |
| **6. Solvents, BOE & 6N Gases** | Decalin, BOE, $\text{N}_2/\text{H}_2$, $\text{O}_2$ | $\$68.92$ | $\$0.0689$ | $\$0.0140$ |
| **Subtotal A: Raw Materials** | **All Chemicals & Gases** | **$\$125.00$** | **$\$0.1250$** | **$\$0.0200$** |
| **7. UV Picosecond Cavity Milling** | Laser Ablation + Plasma | $\$420.00$ | $\$0.4200$ | $\$0.1100$ |
| **8. Slot-Die & VUV Cladding Cure** | 3 Coating + 2 VUV Runs | $\$650.00$ | $\$0.6500$ | $\$0.1800$ |
| **9. Adaptive UV-NIL & Direct-Write** | Stamp Amortization + $405\text{ nm}$ | $\$1,180.00$ | $\$1.1800$ | $\$0.3100$ |
| **10. Xenon Flash Photonic Curing** | $80\text{ }\mu\text{s}$ Forming-Gas Anneal | $\$310.00$ | $\$0.3100$ | $\$0.0900$ |
| **11. Window Etch, Pad Mate & QC** | BOE Thinning + Optical Test | $\$465.00$ | $\$0.4650$ | $\$0.1300$ |
| **Subtotal B: Fab Processing** | **All Cleanroom Steps** | **$\$3,025.00$** | **$\$3.0250$** | **$\$0.8200$** |
| **TOTAL SUM (Passive Bridge)** | **Complete Inlay Bridge** | **$\$3,150.00$** | **$\$3.1500$** | **$\$0.8400$** |

*Explanation of Cost Calculation:*
* **Raw Material Cost per Bridge:** Even for the largest $15.0\text{ mm}$ full-flank bridge ($3000$ waveguides), the total chemical and gas consumption costs only **$\$0.125$ ($12.5\text{ cents}$)** per bridge (**$\$125.00$** per $1,000$ bridges).
* **Fabrication & Lithography Cost per Bridge:** Cleanroom processing—dominated by the high-precision adaptive UV-Nanoimprint step and maskless $405\text{ nm}$ laser direct-writing of the S-bend compensation zones ($\$1.18$ per bridge)—totals **$\$3.025$** per $15.0\text{ mm}$ bridge.
* **Total All-In Passive Bridge Sum:** A finished, tested $15.0\text{ mm}$ optical inlay bridge with integrated elastomer shear buffer and reversible optical socket pads costs **$\$3.15$ per unit** (**$\$3,150.00$ per $1,000$ units**). For the compact $1.6\text{ mm}$ bridge ($20.48\text{ TB/s}$, exceeding an entire HBM stack), the unit cost drops to **$\$0.84$ per bridge** (**$\$840.00$ per $1,000$ units**).

---

### 4.2 System-Level Economic Comparison (Active + Passive Link Total Cost for $192\text{ TB/s}$)

To evaluate the complete system cost of transporting $192.0\text{ TB/s}$ bidirectionally between two TPU-9 class dies (including the silicon photonics E/O modulator array, Ge-on-Si photodiode array, and shared external CW comb-laser sources at die edges), the table below compares the printed $\text{a-Si:H}$ inlay bridge against conventional packaging technologies:

| Interconnect Technology | Hardware Required for $192\text{ TB/s}$ | Power Consumption | Total Cost per Link (USD) | Cost per $\text{TB/s}$ (USD) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Printed $\text{a-Si:H}$ Inlay (Passive)** | $1\times$ $15\text{ mm}$ Printed Bridge | $0\text{ W}$ (Passive Waveguide) | **$\$3.15$** | **$\$0.016\text{ / TB/s}$** |
| **2. Printed $\text{a-Si:H}$ Inlay (Complete)** | Bridge ($\$3.15$) + Die E/O & Comb Laser ($\$28.50$) | $354.0\text{ W}$ ($0.461\text{ pJ/bit}$) | **$\$31.65$** | **$\$0.165\text{ / TB/s}$** |
| **3. Monolithic Si Interposer (CoWoS)** | Full-Reticle Crystalline Si Wafer Slab | $\sim 1,850\text{ W}$ ($\sim 2.4\text{ pJ/bit}$) | **$\$420.00$** | **$\$2.188\text{ / TB/s}$** |
| **4. Copper Board Traces + Retimers** | $6,850$ Diff. Pairs + Active Retimers | $\sim 4,900\text{ W}$ ($\sim 6.4\text{ pJ/bit}$) | **$\$1,680.00$** | **$\$8.750\text{ / TB/s}$** |
| **5. Pluggable $1.6\text{T}$ OSFP Optics** | $960\times$ Front-Panel Transceivers | $\sim 10,750\text{ W}$ ($\sim 14.0\text{ pJ/bit}$) | **$\$1,152,000.00$** | **$\$6,000.00\text{ / TB/s}$** |

*Summary of Economic Impact:* By replacing a $\$420.00$ monolithic silicon interposer slab with a $\$3.15$ localized printed $\text{a-Si:H}$ waveguide inlay ($\$31.65$ including active on-die electro-optics and comb-laser share), packaging interconnect cost drops by **$92.5\%$**, while eliminating reticle size limits and cutting interconnect power consumption by more than **$80\%$**.