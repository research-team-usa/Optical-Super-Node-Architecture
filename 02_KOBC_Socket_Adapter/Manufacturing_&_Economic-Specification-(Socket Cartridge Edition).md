---
title: "KOBC Socket Adapter Module — Assembly Workflow, Alloy/Ceramic Formulations, Mass Balance & Complete USD Cost Breakdown"
author: "Emanuel Schaaf"
framework: "Open Origin Architecture"
status: "Manufacturing & Economic Specification (Socket Cartridge Edition)"
tags:
  - socket-adapter
  - bill-of-materials
  - mass-balance
  - cost-analysis
  - titanium-latch
  - glass-ceramic
---

# Detachable KOBC Optical Socket Adapter Module
**Complete Cartridge Assembly Workflow, Material Formulations, Weight Table, and USD Cost Analysis**

* **Lead Architect:** Emanuel Schaaf
* **Framework:** Open Origin Architecture
* **Reference Unit:** Full-Flank Detachable Cartridge **KOBC-15mm** ($W = 15.0\text{ mm}$, $L = 5.0\text{ mm}$ Optical Span, $L_{\text{ext}} = 6.2\text{ mm}$ Total Cartridge Length including Kinematic Ears, $192.0\text{ TB/s}$ Bidirectional Throughput)

---

## 1. Step-by-Step Cartridge Manufacturing & Socket Assembly Workflow

1. **Wafer-Scale Glass-Ceramic Carrier Preparation:** A $200\text{ mm}$ diameter, $500\text{ }\mu\text{m}$ thick Zero/Low-CTE Lithium-Aluminosilicate (LAS) glass-ceramic wafer ($\alpha = 2.8\text{ ppm/K}$) is femtosecond-laser-machined with conical seating pockets for the three $\varnothing 400\text{ }\mu\text{m}$ ruby microspheres per bridge site and $10\text{ }\mu\text{m}$ thermal isolation trenches around the coupling windows.
2. **Inverted Elastomer & Optical Stack Printing:**
   * A $2.0\text{ }\mu\text{m}$ DVS-BCB primer and the $20.0\text{ }\mu\text{m}$ PDMS-PDPS shear-buffer layer ($G_{\text{buf}} = 50\text{ MPa}$) are slot-die coated onto the carrier wafer and cured at $150\text{ }^\circ\text{C}$.
   * The $1.50\text{ }\mu\text{m}$ bottom $\text{SiO}_2$ cladding is printed from PHPS ink and VUV-converted at $140\text{ }^\circ\text{C}$ ($\lambda = 172\text{ nm}$).
   * The $280\text{ nm}$ $\text{Si}_5\text{H}_{10}$ core layer is printed under anaerobic $\text{N}_2$, pre-gelled at $365\text{ nm}$, imprinted via UV-NIL with the $3000$ waveguide ribs ($450\text{ nm} \times 220\text{ nm}$) and inverse nanotapers, and photonically cured ($80\text{ }\mu\text{s}$ xenon flash in $90\%\text{ N}_2 / 10\%\text{ H}_2$) into low-loss $\text{a-Si:H}$ ($1.8\text{ dB/cm}$).
   * The $1.28\text{ }\mu\text{m}$ top $\text{SiO}_2$ cladding is deposited via VUV-PHPS and thinned to $150\text{ nm}$ over the two $150\text{ }\mu\text{m}$ coupling windows.
3. **Micro-Castellated Silicone Pad Imprinting:** The $10:1$ phenyl-methyl silicone elastomer ($n_{\text{pad}} = 1.500$) is dispensed onto the coupling windows and imprinted with a PTFE-coated quartz mold to form the $40\text{ }\mu\text{m} \times 40\text{ }\mu\text{m} \times 2.0\text{ }\mu\text{m}$ micro-pillows separated by $10\text{ }\mu\text{m}$ expansion channels ($S = 5.00$).
4. **Ruby Microsphere Bonding & Top Thermal Cap Integration:** Three Grade-5 synthetic ruby spheres ($\varnothing 400\text{ }\mu\text{m}$, sphericity $\le 0.13\text{ }\mu\text{m}$) are bonded into the carrier's kinematic pockets using UV-cured cycloaliphatic epoxy. A $100\text{ }\mu\text{m}$ copper-graphene thermal spreader + $25\text{ }\mu\text{m}$ Indium-pad is laminated to the top face before singulating the wafer into individual $15.0\text{ mm} \times 6.2\text{ mm}$ KOBC cartridges.
5. **Die-Edge V-Groove Etching & Field Installation:** On the TPU and HBM/OCS wafers, three radial $\langle 111 \rangle$ V-grooves ($54.74^\circ$) are KOH-etched into the passive perimeter during standard wafer fab and coated with $200\text{ nm}$ $\text{Si}_3\text{N}_4$. During system assembly, the KOBC cartridge is dropped onto the V-grooves and locked with a single click of the $\text{Ti-6Al-4V}$ double-cantilever spring latch ($F_{\text{latch}} = 12.00\text{ N}$).

---

## 2. Exact Chemical, Ceramic & Metallurgical Mixing Ratios

In addition to the seven optical ink and gas formulations defined for the waveguide stack, the detachable KOBC socket hardware requires four structural material compositions with exact stoichiometric/weight ratios:

### 2.1 Formulation 8: Low-CTE LAS Glass-Ceramic Carrier Backbone ($\alpha = 2.8\text{ ppm/K}$)
Synthesized via controlled nucleation and crystallization of a $\text{Li}_2\text{O}-\text{Al}_2\text{O}_3-\text{SiO}_2$ glass melt ($\rho_{\text{LAS}} = 2.53\text{ g/cm}^3$):

* **Exact Oxide Weight Ratio ($\text{wt\%}$):**
  * **$65.50\text{ wt\%}$** Silica ($\text{SiO}_2$, network former)
  * **$22.50\text{ wt\%}$** Alumina ($\text{Al}_2\text{O}_3$, tetrahedral network stabilizer)
  * **$4.20\text{ wt\%}$** Lithia ($\text{Li}_2\text{O}$, $\beta$-eucryptite / $\beta$-spodumene negative-CTE crystal phase former: $\text{Li}_2\text{O}\cdot\text{Al}_2\text{O}_3\cdot 4\text{SiO}_2$)
  * **$4.30\text{ wt\%}$** Titania + Zirconia ($\text{TiO}_2 : \text{ZrO}_2$ in a **$1.15 : 1.00$ mass ratio**, i.e., $2.30\text{ wt\% }\text{TiO}_2 + 2.00\text{ wt\% }\text{ZrO}_2$, acting as heterogeneous nanoscale nucleating agents)
  * **$3.50\text{ wt\%}$** Magnesium & Zinc Oxide ($\text{MgO} : \text{ZnO} = 1.00 : 1.50$, flux modifiers tuning the thermal expansion coefficient to exactly $+2.8\text{ ppm/K}$ across $20\text{–}100\text{ }^\circ\text{C}$ to match silicon).

### 2.2 Formulation 9: Synthetic Ruby Kinematic Microspheres ($\alpha\text{-Al}_2\text{O}_3\text{:Cr}^{3+}$)
Manufactured via Verneuil flame-fusion crystallization ($\rho_{\text{ruby}} = 3.99\text{ g/cm}^3$, Vickers hardness $2,000\text{ HV}$):

* **Exact Weight Ratio:** **$99.00\text{ wt\%}$** ultra-pure $\alpha$-Aluminum Oxide ($\text{Al}_2\text{O}_3$, $M = 101.961\text{ g/mol}$) doped with **$1.00\text{ wt\%}$** Chromium(III) Oxide ($\text{Cr}_2\text{O}_3$, $M = 151.990\text{ g/mol}$).
* **Molar Ratio:** $\text{Al}^{3+} : \text{Cr}^{3+} = 147.6 : 1.00$. The $\text{Cr}^{3+}$ substitution enables instant machine-vision fluorescence inspection ($\lambda_{\text{em}} = 694.3\text{ nm}$) of sphere seating prior to latching.

### 2.3 Formulation 10: Titanium Spring Latch Alloy ($\text{Ti-6Al-4V}$, Grade 5 ELI)
Solution-treated and aged ($\text{STA}$) alpha-beta titanium alloy ($\rho_{\text{Ti}} = 4.43\text{ g/cm}^3$, $E = 114\text{ GPa}$):

* **Exact Metallurgical Weight Ratio:** **$89.87\text{ wt\%}$** Titanium ($\text{Ti}$) : **$6.00\text{ wt\%}$** Aluminum ($\text{Al}$, $\alpha$-phase stabilizer) : **$4.00\text{ wt\%}$** Vanadium ($\text{V}$, $\beta$-phase stabilizer) : **$0.13\text{ wt\%}$** Max Interstitial Iron/Oxygen ($\text{Fe} \le 0.10\text{ wt\%}$, $\text{O} \le 0.03\text{ wt\%}$).

### 2.4 Formulation 11: Low-Shrinkage Cycloaliphatic Epoxy Sphere Adhesive
To lock the three ruby microspheres into the glass-ceramic pockets with $<0.08\%$ curing shrinkage:

* **Exact Weight Mixing Ratio:** **$30.00\text{ wt\%}$** $3,4$-Epoxycyclohexylmethyl-$3',4'$-epoxycyclohexane carboxylate resin : **$69.00\text{ wt\%}$** spherical fused-silica sub-micron filler ($\alpha = 0.55\text{ ppm/K}$) : **$1.00\text{ wt\%}$** Diaryliodonium hexafluoroantimonate cationic UV photoinitiator (**Mass Ratio $30.0 : 69.0 : 1.0$**).

---

## 3. Complete Weight & Volume Table (Single KOBC-15mm Cartridge + Latch & 1,000-Unit Batch)

The physical dimensions of the full-flank **KOBC-15mm** cartridge are $W = 15.0\text{ mm}$, total length $L_{\text{ext}} = 6.20\text{ mm}$ ($5.00\text{ mm}$ optical span + $2 \times 0.60\text{ mm}$ kinematic seating ears, gross carrier area $A_{\text{cart}} = 93.0\text{ mm}^2 = 0.93\text{ cm}^2$).

| Sub-Assembly / Component | Material Specification | Net Volume (1 Unit) | Net Dry Mass (1 Unit) | Batch Net Mass (1,000 Units) | Gross Input Mass (1,000 Units) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Optical Waveguide & Buffer Stack** | 6-Layer $\text{a-Si:H}/\text{SiO}_2/\text{PDMS}$ ($75\text{ mm}^2$) | $1.869\text{ mm}^3$ | $2.253\text{ mg}$ | $2.253\text{ g}$ | $4.748\text{ g}$ (Inks) |
| **2. Glass-Ceramic Carrier Backbone** | LAS Glass-Ceramic ($93\text{ mm}^2 \times 0.5\text{ mm}$) | $46.500\text{ mm}^3$ | $117.645\text{ mg}$ | $117.645\text{ g}$ | $147.056\text{ g}$ (Wafer) |
| **3. Kinematic Ruby Microspheres ($3\times$)** | $\varnothing 0.40\text{ mm }\alpha\text{-Al}_2\text{O}_3\text{:Cr}^{3+}$ | $0.1005\text{ mm}^3$ | $0.401\text{ mg}$ | $0.401\text{ g}$ | $0.420\text{ g}$ ($3,150\text{ pcs}$) |
| **4. Sphere Bonding Epoxy** | Silica-Filled Cycloaliphatic Epoxy | $0.015\text{ mm}^3$ | $0.027\text{ mg}$ | $0.027\text{ g}$ | $0.045\text{ g}$ |
| **5. Top Copper-Graphene Spreader** | $90\text{ }\mu\text{m Cu} + 10\text{ }\mu\text{m}$ CVD Graphene | $7.500\text{ mm}^3$ | $62.400\text{ mg}$ | $62.400\text{ g}$ | $74.880\text{ g}$ |
| **6. Top Thermal Shunt Pad (TIM)** | $25\text{ }\mu\text{m}$ Indium-Silicone Foil | $1.875\text{ mm}^3$ | $6.000\text{ mg}$ | $6.000\text{ g}$ | $7.200\text{ g}$ |
| **Subtotal: Detachable Cartridge** | **Plug-In KOBC-15mm Cartridge** | **$57.860\text{ mm}^3$** | **$188.726\text{ mg}$** | **$188.726\text{ g}$** | **$234.349\text{ g}$** |
| **7. Dual-Cantilever Spring Latch** | $\text{Ti-6Al-4V}$ ($2\text{ Arms} + \text{Bridge Clip}$) | $14.200\text{ mm}^3$ | $62.906\text{ mg}$ | $62.906\text{ g}$ | $88.068\text{ g}$ (Strip) |
| **8. Socket Retainer Posts ($2\times$)** | Low-CTE Invar-36 ($\text{Fe-36Ni}$) | $6.400\text{ mm}^3$ | $51.520\text{ mg}$ | $51.520\text{ g}$ | $64.400\text{ g}$ |
| **TOTAL SOCKET MODULE** | **Cartridge + Latch + Retainers** | **$78.460\text{ mm}^3$** | **$303.152\text{ mg}$** | **$303.152\text{ g}$** | **$386.817\text{ g}$** |

*Explanation of Weight Balance:*
* The **detachable KOBC-15mm cartridge itself weighs only $188.73\text{ mg}$** ($0.189\text{ g}$) — lighter than a standard postage stamp — while carrying $3,000$ optical waveguides ($192.0\text{ TB/s}$ bidirectional throughput).
* Including the reusable **$\text{Ti-6Al-4V}$ double-cantilever spring latch ($62.91\text{ mg}$)** and the two **Invar-36 retainer posts ($51.52\text{ mg}$)** permanently mounted on the socket frame, the entire mechanical + optical interconnect assembly adds just **$303.15\text{ mg}$ ($0.303\text{ g}$)** per die flank ($303.15\text{ g}$ total net weight for $1,000$ complete assemblies).

---

## 4. Complete USD ($) Cost Table with Total Sum (Cartridge + Socket Hardware)

The cost breakdown below covers all raw materials, wafer-scale glass-ceramic carrier processing, optical waveguide printing, kinematic ruby assembly, and the reusable titanium latch mechanism across three modular sizes (**KOBC-1x** at $1.6\text{ mm}$, **KOBC-5x** at $8.0\text{ mm}$, and **KOBC-9x/15mm** at $15.0\text{ mm}$):

| Cost Component / Process Step | Unit Cost Basis | Batch Cost (1,000 × 15mm Units) | Unit Cost: KOBC-15mm ($192\text{ TB/s}$) | Unit Cost: KOBC-5x 8mm ($102.4\text{ TB/s}$) | Unit Cost: KOBC-1x 1.6mm ($20.48\text{ TB/s}$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Optical Waveguide Inks & Gases** | $\text{Si}_5\text{H}_{10}$, PHPS, PDMS, BCB, 6N Gas | $\$125.00$ | $\$0.1250$ | $\$0.0680$ | $\$0.0200$ |
| **2. LAS Glass-Ceramic Carrier Wafer** | $200\text{ mm}$ Wafer ($\sim 180$ Sites/Wafer) | $\$340.00$ | $\$0.3400$ | $\$0.1900$ | $\$0.0500$ |
| **3. Grade-5 Ruby Spheres ($3\times$) & Epoxy** | $\$0.045\text{ / Sphere}$ + UV Epoxy | $\$145.00$ | $\$0.1450$ | $\$0.1450$ | $\$0.1450$ |
| **4. Cu-Graphene Cap & Indium TIM** | Stamped Cu-C Foil + In-Silicone Pad | $\$210.00$ | $\$0.2100$ | $\$0.1200$ | $\$0.0350$ |
| **Subtotal A: Cartridge Materials** | **All Physical Cartridge Inputs** | **$\$820.00$** | **$\$0.8200$** | **$\$0.5230$** | **$\$0.2500$** |
| **5. Femtosecond Carrier Pocket Milling** | Laser Pocket + Thermal Trenching | $\$380.00$ | $\$0.3800$ | $\$0.2200$ | $\$0.0800$ |
| **6. Slot-Die, VUV & Flash Photonic Cure** | Wafer-Scale Coating + Annealing | $\$790.00$ | $\$0.7900$ | $\$0.4400$ | $\$0.1900$ |
| **7. UV-NIL Waveguide & Pillow Molding** | Imprint Litho + S-Bend Direct-Write | $\$1,120.00$ | $\$1.1200$ | $\$0.6500$ | $\$0.2800$ |
| **8. Pick-and-Place Sphere Assembly & QC** | Vision Alignment + Interferometry | $\$390.00$ | $\$0.3900$ | $\$0.3100$ | $\$0.2200$ |
| **Subtotal B: Cartridge Fabrication** | **All Wafer & Assembly Steps** | **$\$2,680.00$** | **$\$2.6800$** | **$\$1.6200$** | **$\$0.7700$** |
| **SUBTOTAL (Replaceable Cartridge)** | **Finished Plug-In KOBC Cartridge** | **$\$3,500.00$** | **$\$3.5000$** | **$\$2.1430$** | **$\$1.0200$** |
| **9. $\text{Ti-6Al-4V}$ Spring Latch + Invar Posts** | Photochemical Etching + Heat Treat | $\$850.00$ | $\$0.8500$ | $\$0.6200$ | $\$0.3800$ |
| **10. Die-Edge KOH V-Groove Mask Step** | Wafer-Level KOH + $\text{Si}_3\text{N}_4$ Liner | $\$250.00$ | $\$0.2500$ | $\$0.1870$ | $\$0.1000$ |
| **Subtotal C: Permanent Socket Hardware** | **Reusable Latch + V-Groove Prep** | **$\$1,100.00$** | **$\$1.1000$** | **$\$0.8070$** | **$\$0.4800$** |
| **GRAND TOTAL (Complete KOBC System)** | **Cartridge + Reusable Socket** | **$\$4,600.00$** | **$\$4.6000$** | **$\$2.9500$** | **$\$1.5000$** |

*Summary of Final Cost & Upgrade Economics:*
* **Initial Full-Socket Installation (Cartridge + Permanent Titanium Latch + V-Grooves):** Installing the complete detachable optical socket system for a $15.0\text{ mm}$ full-flank link ($192.0\text{ TB/s}$) costs **$\$4.60$ per unit** (**$\$4,600.00$ per $1,000$ units**), or **$\$1.50$ per unit** for the compact $1.6\text{ mm}$ HBM-replacement module.
* **Future Field-Upgrade Cost (Cartridge Swap Only):** Because the $\text{Ti-6Al-4V}$ latch and KOH silicon V-grooves ($\$1.10$) remain permanently on the socket, upgrading an accelerator cluster to a newer optical cartridge generation costs only **$\$3.50$ per $15.0\text{ mm}$ bridge** (**$\$1.02$ per $1.6\text{ mm}$ bridge**) and takes less than $5\text{ seconds}$ per socket click.