---
title: "Printed Elastomer-Buffered a-Si:H Optical Waveguide Inlay Bridge — Manufacturing Specification & Mathematical Derivation for TPU-9 Class Accelerators"
author: "Emanuel Schaaf"
framework: "Open Origin Architecture"
status: "Technical Specification & Proof of Concept"
tags:
  - optical-interconnect
  - silicon-photonics
  - amorphous-silicon
  - packaging-architecture
  - TPU-9
  - shear-lag-mechanics
---

# Printed Elastomer-Buffered $\text{a-Si:H}$ Optical Waveguide Inlay Bridge
**Complete Manufacturing Guide, Process Chemistry, and First-Principles Mathematical Derivations**

* **Lead Architect:** Emanuel Schaaf
* **Framework:** Open Origin Architecture
* **Target Application:** Co-Packaged Optical (CPO) Die-to-Die and Die-to-Memory Interconnects for Next-Generation AI Accelerators (TPU 9 Class)

---

## 1. Strategic Motivation: Why TPU 9 Must Transition to Printed Optical Inlay Bridges

Current eighth-generation AI accelerator architectures (such as Google TPU 8t, TPU 8i, TPU 8i Max, and TPU 8tx) have already exposed the fundamental physical limits of electrical package-level signaling. While optical circuit switches (OCS) in topologies like *Boardfly* dramatically reduce rack-level hop counts, the signal path from the silicon die out to the optical transceivers still relies on electrical copper traces across organic package substrates and printed circuit boards.

If Google plans a **TPU 9** architecture capable of scaling to multi-million-token context windows, real-time multi-agent reasoning, and disaggregated memory pools, three physical walls make a new interconnect paradigm mandatory:

1. **The Copper Escape Energy Wall ($\text{pJ/bit}$):** Pushing high-frequency electrical signals ($112\text{–}224\text{ Gbit/s}$ PAM4) across organic package substrates and board traces suffers from severe dielectric loss and skin-effect attenuation. Together with retimers and SerDes equalization, electrical board escape consumes $5\text{ to }15\text{ pJ/bit}$. At $100\text{ TB/s}$ of bidirectional traffic, electrical I/O alone would consume several kilowatts per package—exceeding the thermal budget of the compute core itself.
2. **The Reticle and Yield Wall of Monolithic Silicon Interposers:** Full-wafer crystalline silicon interposers (used to connect compute dies and HBM stacks) are constrained by lithography reticle stitching limits, high wafer fabrication costs, and severe thermomechanical warpage when mounted onto large organic substrates. Over $70\%$ of a full silicon interposer's area serves merely as passive mechanical space rather than active high-density routing.
3. **The Mechanical Socket Pitch Limit:** High-Bandwidth Memory (HBM3/HBM4) requires thousands of parallel electrical micro-bumps at $10\text{ to }55\text{ }\mu\text{m}$ pitch. Mechanical spring sockets cannot scale below $\sim 300\text{ }\mu\text{m}$ pitch without contact buckling, silicon fracture, and destructive parasitic inductance ($L \frac{dI}{dt}$).

### The Architectural Solution
Instead of placing an entire multi-die processor complex onto a fragile, ultra-expensive monolithic silicon slab, **localized optical waveguide bridges** are printed directly into recessed pockets (inlays) of the organic package substrate only where ultra-high bandwidth is needed. By converting electrical signals into optical wavelengths right at the edge of the compute and memory dies, a $1.6\text{ mm}$ wide printed inlay replaces thousands of copper pins, reduces interconnect energy to **$0.461\text{ pJ/bit}$**, and enables a contactless, reversible **optical socket interface** via index-matched adiabatic nanotapers.

---

## 2. Cross-Disciplinary Analogies & Functional Transfer

Engineering breakthroughs emerge when proven macro-scale principles from heavy industry and material science are transferred to micro-scale semiconductor packaging:

* **Analogy 1 — High-Speed Rail Viaduct Bearings (Structural Engineering):** When continuous welded steel rails cross a long concrete bridge, engineers do not bolt the steel rigidly to the concrete; the different thermal expansion rates would shear the bolts or buckle the track. Instead, elastomeric bearing pads are placed beneath the rail. These pads have high vertical stiffness to carry the load, but a low shear modulus ($G$) that converts horizontal thermal expansion into harmless elastic shear strain.
* **Analogy 2 — Automotive Laminated Safety Glass & Optical Fiber Splicing (Materials Engineering):** Joining two brittle optical plates across an air gap causes severe Fresnel reflections and rapid decay of evanescent light fields. Introducing a transparent, refractive-index-matched polymeric interlayer simultaneously eliminates optical interface loss and mechanically decouples shock and shear stresses between the rigid panes.

**Functional Transfer to Semiconductor Packaging:**
By printing a $20\text{ }\mu\text{m}$ compliant siloxane elastomer buffer layer at the bottom of the substrate cavity prior to depositing the $3\text{ }\mu\text{m}$ thin hydrogenated amorphous silicon ($\text{a-Si:H}$) / silicon dioxide ($\text{SiO}_2$) waveguide stack, the $13.4\text{ ppm/K}$ thermal expansion mismatch between the organic board and the silicon bridge is absorbed elastically. Furthermore, filling the micro-gap at the die-to-bridge socket interface with a reversible, index-matched silicone elastomer pad ($n = 1.50$) enables low-loss evanescent optical coupling without physical metal-to-metal micro-bumps.

---

## 3. Complete Chemical Formulations & Stoichiometric Derivations

### 3.1 Why Hydrogenated Amorphous Silicon ($\text{a-Si:H}$) Replaces Excimer-Laser-Crystallized Polysilicon

A critical physical correction in low-temperature waveguide printing is avoiding crystallization into polycrystalline silicon (LTPS). While excimer laser annealing (ELA) improves electron mobility for display transistors, polycrystalline silicon contains dense grain boundaries. At telecommunications wavelengths ($\lambda_0 = 1550\text{ nm}$), refractive index discontinuities at grain boundaries cause severe Rayleigh scattering, while unpassivated dangling bonds ($\text{Si}\cdot$) introduce mid-gap electronic states that absorb infrared photons, driving propagation losses to $15\text{–}35\text{ dB/cm}$.

By contrast, **hydrogenated amorphous silicon ($\text{a-Si:H}$)** is an isotropic, grain-boundary-free continuous random network. When $8\text{ to }12\text{ at.\%}$ hydrogen is covalently incorporated into the amorphous network, hydrogen atoms passivate open silicon dangling bonds ($\text{Si-H}$), clearing the sub-bandgap optical window at $\lambda_0 = 1550\text{ nm}$ ($E_{\text{photon}} = 0.80\text{ eV} \ll E_{\text{g,opt}} \approx 1.72\text{ eV}$) and reducing waveguide propagation loss to **$1.5\text{–}2.0\text{ dB/cm}$**.

### 3.2 Synthesis of the Bottom and Top $\text{SiO}_2$ Cladding Layers via VUV-Driven PHPS Conversion

Organic package substrates (such as Ajinomoto Build-up Film, ABF) have a glass transition temperature $T_g \approx 160\text{–}220\text{ }^\circ\text{C}$ and cannot survive conventional $800\text{ }^\circ\text{C}$ thermal oxidation. To form high-purity silicon dioxide ($\text{SiO}_2$, refractive index $n_{\text{clad}} = 1.444$) below $150\text{ }^\circ\text{C}$, liquid **Perhydropolysilazane (PHPS)** dissolved in di-n-butyl ether is printed and converted photochemically using a Xenon excimer vacuum-ultraviolet (VUV) lamp ($\lambda = 172\text{ nm}$).

The photon energy at $\lambda = 172\text{ nm}$ is:

$$
E_{\text{photon}} = \frac{h \cdot c}{\lambda} = \frac{6.626 \times 10^{-34}\text{ J}\cdot\text{s} \times 2.998 \times 10^8\text{ m/s}}{172 \times 10^{-9}\text{ m}} = 1.155 \times 10^{-18}\text{ J} \approx 7.21\text{ eV}
$$

Because $7.21\text{ eV}$ exceeds the bond dissociation energies of both $\text{Si-N}$ ($4.5\text{ eV}$) and $\text{Si-H}$ ($3.1\text{ eV}$) as well as molecular oxygen $\text{O=O}$ ($5.15\text{ eV}$), VUV irradiation simultaneously cleaves the polysilazane backbone and generates reactive atomic oxygen $\text{O}(^1\text{D})$ and ozone ($\text{O}_3$) in a controlled $\text{O}_2/\text{H}_2\text{O}$ process chamber at $T \le 150\text{ }^\circ\text{C}$:

$$
\text{-[SiH}_2\text{-NH]-}_n\text{ (l)} + 2n\,\text{H}_2\text{O}\text{ (g)} \xrightarrow{\lambda = 172\text{ nm},\; T \le 150\,^\circ\text{C}} n\,\text{SiO}_2\text{ (s)} + n\,\text{NH}_3\uparrow + 2n\,\text{H}_2\uparrow
$$

In parallel, dry radical photo-oxidation proceeds via:

$$
\text{-[SiH}_2\text{-NH]-}_n\text{ (l)} + \frac{3}{2}n\,\text{O}_2\text{ (g)} \xrightarrow{\lambda = 172\text{ nm},\; \text{O}(^1\text{D})} n\,\text{SiO}_2\text{ (s)} + n\,\text{H}_2\text{O}\uparrow + \frac{1}{2}n\,\text{N}_2\uparrow
$$

**Stoichiometric Mass Conversion:**
One monomer unit of $\text{-[SiH}_2\text{-NH]-}$ has a molar mass of $M_{\text{PHPS}} = 28.085 + 3(1.008) + 14.007 = 45.116\text{ g/mol}$ and yields one formula unit of $\text{SiO}_2$ with molar mass $M_{\text{SiO}_2} = 60.084\text{ g/mol}$. The theoretical mass gain upon oxygen substitution of nitrogen and hydrogen is:

$$
\frac{M_{\text{SiO}_2}}{M_{\text{PHPS}}} = \frac{60.084\text{ g/mol}}{45.116\text{ g/mol}} = 1.3318 \quad (+33.18\%\text{ mass increase})
$$

While mass increases by $33.18\%$, the structural density increases from $\rho_{\text{PHPS}} \approx 1.30\text{ g/cm}^3$ to dense amorphous silica $\rho_{\text{SiO}_2} \approx 2.20\text{ g/cm}^3$, resulting in a predictable vertical film thickness contraction factor of:

$$
\frac{t_{\text{SiO}_2}}{t_{\text{PHPS}}} = \frac{M_{\text{SiO}_2}}{M_{\text{PHPS}}} \cdot \frac{\rho_{\text{PHPS}}}{\rho_{\text{SiO}_2}} = 1.3318 \times \frac{1.30}{2.20} \approx 0.787 \quad (21.3\%\text{ vertical shrinkage})
$$

### 3.3 Liquid Silicon Printing & Controlled Photonic Conversion ($\text{Si}_5\text{H}_{10} \rightarrow \text{a-Si:H}$)

The high-index waveguide core ($n_{\text{core}} = 3.48$ at $\lambda_0 = 1550\text{ nm}$) is synthesized from liquid **Cyclopentasilane ($\text{Si}_5\text{H}_{10}$)**, a cyclic hydrosilane with molar mass $M_{\text{CPS}} = 150.505\text{ g/mol}$, density $\rho_{\text{CPS}} = 0.963\text{ g/cm}^3$, melting point $-10.5\text{ }^\circ\text{C}$, and boiling point $194\text{ }^\circ\text{C}$.

**Step 1 — Anaerobic UV Ring-Opening Polymerization ($\lambda = 365\text{ nm}$):**
Under a strictly oxygen-free nitrogen atmosphere ($\text{O}_2 < 0.1\text{ ppm}$, $\text{H}_2\text{O} < 0.1\text{ ppm}$), liquid cyclopentasilane (formulated at $35\text{ vol\%}$ in anhydrous cyclooctane to tune ink viscosity to $\eta \approx 8\text{ mPa}\cdot\text{s}$) is exposed to $365\text{ nm}$ UV light ($E_{\text{photon}} = 3.40\text{ eV}$). This cleaves strained $\text{Si-Si}$ ring bonds ($E_{\text{bond}} \approx 2.3\text{ eV}$) without breaking stronger $\text{Si-H}$ bonds ($3.1\text{ eV}$), generating biradical chains that crosslink into a non-volatile solid polysilane gel:

$$
n\,\text{Si}_5\text{H}_{10}\text{ (l)} \xrightarrow{h\nu\; (\lambda = 365\text{ nm}),\; 25\,^\circ\text{C}} \cdot\text{SiH}_2\text{-(SiH}_2\text{)}_3\text{-SiH}_2\cdot \longrightarrow \text{-(SiH}_2\text{)}_{5n}\text{- (s, polysilane network)}
$$

**Step 2 — Microsecond Photonic Curing under Forming Gas ($\text{N}_2 / \text{H}_2$):**
Following UV-Nanoimprint patterning of the polysilane gel, the substrate is held on a temperature-controlled chuck at $T_{\text{chuck}} = 160\text{ }^\circ\text{C}$ under a laminar flow of forming gas ($90\%\text{ N}_2 + 10\%\text{ H}_2$). High-intensity microsecond light pulses ($\tau_{\text{pulse}} = 80\text{ }\mu\text{s}$, radiant fluence $F = 1.8\text{ J/cm}^2$, spectral band $\lambda = 380\text{–}650\text{ nm}$) are absorbed solely within the $220\text{ nm}$ silicon layer. Because the thermal diffusion length in the underlying $1.5\text{ }\mu\text{m}$ $\text{SiO}_2$ bottom cladding during an $80\text{ }\mu\text{s}$ pulse is:

$$
L_{\text{th}} = \sqrt{4 \cdot D_{\text{SiO}_2} \cdot \tau_{\text{pulse}}} = \sqrt{4 \times 8.3 \times 10^{-7}\text{ m}^2\text{/s} \times 80 \times 10^{-6}\text{ s}} \approx 16.3\text{ }\mu\text{m}
$$

the transient temperature inside the thin polysilane core reaches $T_{\text{core,peak}} \approx 385\text{ }^\circ\text{C}$ for less than $100\text{ }\mu\text{s}$, driving dehydrogenation and three-dimensional $\text{Si-Si}$ condensation while the organic ABF substrate below the $\text{SiO}_2$ and siloxane buffer remains safely below $185\text{ }^\circ\text{C}$:

$$
\text{-(SiH}_2\text{)}_{5n}\text{- (s)} \xrightarrow{\text{Photonic Pulse }(80\,\mu\text{s}),\; \text{N}_2/10\%\,\text{H}_2} 5n\,\text{SiH}_x\text{ (s, a-Si:H)} + 5n\left(1 - \frac{x}{2}\right)\text{H}_2\uparrow
$$

The partial pressure of $\text{H}_2$ in the forming gas establishes chemical equilibrium at $x = 0.10$, yielding an atomic hydrogen fraction of:

$$
C_{\text{H}} = \frac{x}{1 + x} = \frac{0.10}{1.10} = 0.0909 \quad (9.09\text{ at.\% H})
$$

**Step 3 — Dangling Bond Passivation Equilibrium:**
Any residual paramagnetic neutral silicon dangling bonds ($D^0$, denoted $\text{Si}_3\equiv\text{Si}\cdot$) are passivated by atomic hydrogen diffusing through the amorphous network during the tail of the photonic pulse:

$$
\text{Si}_3\equiv\text{Si}\cdot + \text{H}\cdot \longrightarrow \text{Si}_3\equiv\text{Si-H} \qquad (\Delta H \approx -3.1\text{ eV})
$$

This lowers the defect density from $\sim 10^{19}\text{ cm}^{-3}$ (unpassivated $\text{a-Si}$) to $< 5 \times 10^{15}\text{ cm}^{-3}$ ($\text{a-Si:H}$).

---

## 4. Complete Step-by-Step Manufacturing Workflow

All chemical steps operate inside a closed-loop inert glovebox cluster equipped with catalytic $\text{H}_2$ recombiners and wet-acid $\text{NH}_3$ scrubbers, ensuring zero hazardous emissions and full environmental compliance.

### Stage 1: Substrate Cavity Micromachining & Base Planarization
1. **Cavity Milling:** At the interconnect boundary between the TPU die site and the HBM/optical port site on the organic ABF package substrate, a precision UV picosecond laser ($\lambda = 355\text{ nm}$) ablates a rectangular inlay pocket of length $L = 5.0\text{ mm}$, width $W \in [1.6\text{ mm}, 15.0\text{ mm}]$, and depth $d_{\text{cav}} = 25.0\text{ }\mu\text{m}$.
2. **Plasma Descum & Leveling:** An $\text{O}_2/\text{CF}_4$ microwave plasma removes carbonized laser residue, followed by dispensing a $2.0\text{ }\mu\text{m}$ benzocyclobutene (BCB) leveling prime coat cured at $180\text{ }^\circ\text{C}$ to reduce substrate surface roughness to $R_a < 15\text{ nm}$.

### Stage 2: Deposition of the $20\text{ }\mu\text{m}$ Siloxane Elastomer Shear-Buffer
1. **Slot-Die Dispensing:** Polydimethylsiloxane-co-diphenylsiloxane (PDMS-PDPS) prepolymer is slot-die coated into the cavity to an exact thickness of $h_{\text{buf}} = 20.0\text{ }\mu\text{m}$.
2. **Platinum-Catalyzed Hydrosilylation Cure:** Crosslinking proceeds via vinyl-terminated siloxane chains reacting with $\text{Si-H}$ crosslinkers at $150\text{ }^\circ\text{C}$ for $20\text{ min}$ (zero volatile byproducts), producing a thermally stable elastomer with shear modulus $G_{\text{buf}} = 50\text{ MPa}$.
3. **Adhesion Activation:** A brief $15\text{ s}$ mild $\text{O}_2$ plasma treatment converts the top $5\text{ nm}$ of the siloxane buffer into a silanol-rich ($\text{-Si-OH}$) surface for covalent bonding to the bottom cladding.

### Stage 3: Bottom $\text{SiO}_2$ Optical Cladding Synthesis ($1.5\text{ }\mu\text{m}$)
1. **PHPS Coating:** A $1.90\text{ }\mu\text{m}$ wet film of Perhydropolysilazane ($\text{-[SiH}_2\text{-NH]-}_n$) is inkjet-printed onto the activated elastomer buffer.
2. **Low-Temperature VUV Conversion:** The substrate is irradiated with $172\text{ nm}$ Xenon excimer VUV light ($50\text{ mW/cm}^2$) for $180\text{ s}$ at $140\text{ }^\circ\text{C}$ in a humidified oxygen chamber ($3.0\text{ vol\% }\text{H}_2\text{O}$). The film densifies by $21.3\%$ into a pinhole-free, optically pure $1.50\text{ }\mu\text{m}$ $\text{SiO}_2$ bottom cladding ($n_{\text{clad}} = 1.444$) that doubles as a thermal barrier.

### Stage 4: Anaerobic Cyclopentasilane Printing & UV Gelation
1. **Inert Transfer:** The substrate enters the anaerobic $\text{N}_2$ printing module ($\text{O}_2 < 0.1\text{ ppm}$).
2. **Precursor Deposition:** The $35\text{ vol\%}$ $\text{Si}_5\text{H}_{10}$ / cyclooctane ink is slot-die printed across the $\text{SiO}_2$ bottom cladding. Vacuum flash drying at $60\text{ }^\circ\text{C}$ ($10\text{ mbar}$) evaporates the cyclooctane solvent completely, leaving a uniform $280\text{ nm}$ liquid $\text{Si}_5\text{H}_{10}$ layer.
3. **UV Pre-Crosslinking:** Flood exposure at $\lambda = 365\text{ nm}$ ($120\text{ mJ/cm}^2$) induces ring-opening polymerization into a deformable viscoelastic polysilane gel ($\text{-(SiH}_2\text{)}_{5n}\text{-}$).

### Stage 5: Adaptive UV-Nanoimprint Lithography (UV-NIL) & Direct-Write S-Bend Alignment
1. **Optical Fiducial Mapping:** High-resolution interferometric cameras measure the actual post-placement coordinates $(\Delta x, \Delta y, \Delta \theta)$ of the adjacent TPU and HBM/optical dies with $\pm 50\text{ nm}$ accuracy.
2. **Waveguide Core Imprinting:** A fluorosilane-treated quartz nanoimprint stamp molds the parallel waveguide ribs (width $w = 450\text{ nm}$, height $h = 220\text{ nm}$, pitch $p = 5.0\text{ }\mu\text{m}$, plus $100\text{ nm}$ inverse nanotaper tips at both ends) directly into the polysilane gel under $1.5\text{ bar}$ contact pressure, while a $365\text{ nm}$ UV pulse locks the rib geometry with sidewall roughness $\sigma_{\text{rms}} < 1.5\text{ nm}$.
3. **Adaptive S-Bend Compensation:** In the two $400\text{ }\mu\text{m}$ routing zones (at $z = 1.5\text{ mm}$ and $z = 3.5\text{ mm}$), a maskless $405\text{ nm}$ laser direct-writer dynamically exposes custom Bezier S-bends (minimum bend radius $R = 50\text{ }\mu\text{m}$) that smoothly connect any misaligned die ports to the imprinted main waveguide array. Unexposed polysilane in the adaptive zones is rinsed away in anhydrous decalin.

### Stage 6: Microsecond Photonic Curing to $\text{a-Si:H}$
1. **Forming Gas Purge:** The chamber is purged with $90\%\text{ N}_2 + 10\%\text{ H}_2$ at a chuck temperature of $160\text{ }^\circ\text{C}$.
2. **Flash Dehydrogenation:** A xenon flash lamp delivers five $80\text{ }\mu\text{s}$ pulses ($1.8\text{ J/cm}^2$ per pulse, $1\text{ Hz}$ repetition rate). The imprinted polysilane ribs densify to $h = 220\text{ nm} \times w = 450\text{ nm}$ hydrogenated amorphous silicon ($\text{a-Si:H}$, $9.1\text{ at.\% H}$, $n_{\text{core}} = 3.48$).

### Stage 7: Upper $\text{SiO}_2$ Passivation Cladding & Coupling Window Opening
1. **Top Cladding Synthesis:** A second PHPS layer is printed over the $\text{a-Si:H}$ waveguides and converted via $172\text{ nm}$ VUV irradiation into a $1.30\text{ }\mu\text{m}$ upper $\text{SiO}_2$ cladding, bringing total waveguide stack thickness to $t_{\text{wg}} = 1.50 + 0.22 + 1.28 = 3.00\text{ }\mu\text{m}$.
2. **Coupling Window Thinning:** Over the $150\text{ }\mu\text{m}$ long adiabatic inverse nanotaper regions at both ends of the bridge ($z \in [0, 0.15\text{ mm}]$ and $z \in [4.85, 5.0\text{ mm}]$), selective buffered oxide etching thins the upper $\text{SiO}_2$ cover to $150\text{ nm}$ so the expanded optical mode can couple vertically.

### Stage 8: Reversible Index-Matched Silicone Elastomer Socket Pad Integration
1. **Micro-Pad Lamination:** A $2.0\text{ }\mu\text{m}$ thin, optically clear phenyl-methyl silicone elastomer micro-pad (refractive index $n_{\text{pad}} = 1.50$, Shore OO hardness $35$) is laminated onto the coupling windows at both ends of the bridge.
2. **Socket Mate:** When the TPU and HBM/optical dies are seated onto their mechanical alignment guides, their downward-facing silicon nitride/silicon nanotapers gently compress the $2.0\text{ }\mu\text{m}$ elastomer pad by $200\text{ nm}$. This wets the optical interface without air gaps, creating a repeatable, detachable optical socket connection.

---

## 5. Complete Mathematical & Physical Derivations

### 5.1 Thermomechanical Shear-Lag Derivation (Suhir Model)

Consider a symmetric optical inlay bridge of total length $L = 5.0\text{ mm}$ extending along $x \in \left[-\frac{L}{2}, +\frac{L}{2}\right]$, bonded via a compliant elastomer buffer of thickness $h_{\text{buf}}$ and shear modulus $G_{\text{buf}}$ to an organic substrate.

#### Step 1: Force Balance on an Infinitesimal Element $dx$
Let $F_{\text{wg}}(x)$ be the internal longitudinal tensile/compressive force in the waveguide stack of width $b$ and thickness $t_{\text{wg}}$, and let $\tau(x)$ be the interfacial shear stress at the buffer interface. Force equilibrium on a differential slice $dx$ yields:

$$
\frac{dF_{\text{wg}}(x)}{dx} - b \cdot \tau(x) = 0 \implies \frac{dF_{\text{wg}}(x)}{dx} = b \cdot \tau(x)
$$

Because the organic substrate thickness ($t_{\text{sub}} \approx 1000\text{ }\mu\text{m}$) is more than three hundred times greater than the waveguide stack thickness ($t_{\text{wg}} = 3.0\text{ }\mu\text{m}$), the axial compliance of the substrate is negligible compared to the thin film ($\frac{1}{E'_{\text{sub}} t_{\text{sub}}} \ll \frac{1}{E'_{\text{wg}} t_{\text{wg}}}$).

#### Step 2: Longitudinal Strain-Displacement Relations
When the package experiences a uniform temperature change $\Delta T = T_{\text{operating}} - T_{\text{cure}}$, the longitudinal normal strains in the substrate $\varepsilon_{\text{sub}}(x)$ and in the waveguide stack $\varepsilon_{\text{wg}}(x)$ are:

$$
\varepsilon_{\text{sub}}(x) = \frac{du_{\text{sub}}(x)}{dx} = \alpha_{\text{sub}} \cdot \Delta T
$$

$$
\varepsilon_{\text{wg}}(x) = \frac{du_{\text{wg}}(x)}{dx} = \alpha_{\text{wg}} \cdot \Delta T + \frac{F_{\text{wg}}(x)}{b \cdot S_{\text{wg}}}
$$

where $u_{\text{sub}}(x)$ and $u_{\text{wg}}(x)$ are the horizontal displacements, and $S_{\text{wg}}$ is the axial stiffness per unit width of the waveguide stack under biaxial plane-stress conditions:

$$
S_{\text{wg}} = E'_{\text{wg}} \cdot t_{\text{wg}} = \left(\frac{E_{\text{wg}}}{1 - \nu_{\text{wg}}}\right) t_{\text{wg}}
$$

#### Step 3: Shear Compatibility in the Elastomer Buffer
Assuming linear elastic shear across the compliant buffer thickness $h_{\text{buf}}$, the engineering shear strain $\gamma(x)$ and shear stress $\tau(x)$ are related to the relative horizontal displacement between substrate and waveguide by:

$$
\gamma(x) = \frac{u_{\text{sub}}(x) - u_{\text{wg}}(x)}{h_{\text{buf}}} \implies \tau(x) = G_{\text{buf}} \cdot \gamma(x) = \frac{G_{\text{buf}}}{h_{\text{buf}}} \left[u_{\text{sub}}(x) - u_{\text{wg}}(x)\right]
$$

#### Step 4: Derivation of the Second-Order Governing Differential Equation
Differentiating $\tau(x)$ once with respect to $x$ and substituting the strain definitions gives:

$$
\frac{d\tau(x)}{dx} = \frac{G_{\text{buf}}}{h_{\text{buf}}} \left[\frac{du_{\text{sub}}(x)}{dx} - \frac{du_{\text{wg}}(x)}{dx}\right] = \frac{G_{\text{buf}}}{h_{\text{buf}}} \left[(\alpha_{\text{sub}} - \alpha_{\text{wg}})\Delta T - \frac{F_{\text{wg}}(x)}{b \cdot S_{\text{wg}}}\right]
$$

Differentiating a second time with respect to $x$ and noting that $(\alpha_{\text{sub}} - \alpha_{\text{wg}})\Delta T = \varepsilon_{\text{th}}$ is spatially constant yields:

$$
\frac{d^2\tau(x)}{dx^2} = -\frac{G_{\text{buf}}}{h_{\text{buf}} \cdot S_{\text{wg}}} \cdot \frac{1}{b} \frac{dF_{\text{wg}}(x)}{dx}
$$

Substituting the force balance $\frac{1}{b}\frac{dF_{\text{wg}}(x)}{dx} = -\tau(x)$ (accounting for opposing sign convention between top and bottom film faces) produces the homogeneous second-order differential equation:

$$
\frac{d^2\tau(x)}{dx^2} - k^2 \tau(x) = 0
$$

where the shear-lag eigenvalue $k$ (in $\text{m}^{-1}$) is defined as:

$$
k = \sqrt{\frac{G_{\text{buf}}}{h_{\text{buf}} \cdot S_{\text{wg}}}}
$$

#### Step 5: Applying Boundary Conditions
The general solution to $\frac{d^2\tau}{dx^2} - k^2\tau = 0$ is $\tau(x) = C_1 \sinh(k x) + C_2 \cosh(k x)$.
1. **Symmetry at the bridge center ($x = 0$):** Because thermal expansion is symmetric about $x = 0$, relative displacement vanishes at the origin, so $\tau(0) = 0 \implies C_2 = 0$.
2. **Traction-free ends at $x = \pm \frac{L}{2}$:** The ends of the recessed bridge have zero longitudinal normal force, $F_{\text{wg}}\left(\pm \frac{L}{2}\right) = 0$. Evaluating $\frac{d\tau}{dx}$ at $x = \frac{L}{2}$ gives:

$$
\left.\frac{d\tau(x)}{dx}\right|_{x = L/2} = C_1 k \cosh\left(k \frac{L}{2}\right) = \frac{G_{\text{buf}}}{h_{\text{buf}}} \varepsilon_{\text{th}} \implies C_1 = \frac{G_{\text{buf}} \cdot \varepsilon_{\text{th}}}{h_{\text{buf}} \cdot k \cdot \cosh\left(k \frac{L}{2}\right)}
$$

Substituting $C_1$ yields the exact analytical shear stress distribution along the bridge:

$$
\tau(x) = \frac{G_{\text{buf}}}{h_{\text{buf}} \cdot k} \cdot (\alpha_{\text{sub}} - \alpha_{\text{wg}})\Delta T \cdot \frac{\sinh(k x)}{\cosh\left(k \frac{L}{2}\right)}
$$

At the bridge edges ($x = \pm \frac{L}{2}$), the magnitude of the maximum interfacial shear stress is:

$$
\tau_{\max} = \left|\tau\left(\pm \frac{L}{2}\right)\right| = \frac{G_{\text{buf}}}{h_{\text{buf}} \cdot k} \cdot \varepsilon_{\text{th}} \cdot \tanh\left(k \frac{L}{2}\right)
$$

#### Step 6: Step-by-Step Numerical Evaluation
Given physical parameters:
* Bridge length: $L = 5.0 \times 10^{-3}\text{ m} \implies \frac{L}{2} = 2.5 \times 10^{-3}\text{ m}$
* Operating temperature swing: $\Delta T = 85\text{ }^\circ\text{C} - 25\text{ }^\circ\text{C} = 60\text{ K}$
* CTE mismatch: $\Delta \alpha = \alpha_{\text{sub}} - \alpha_{\text{wg}} = (16.0 - 2.6) \times 10^{-6}\text{ K}^{-1} = 13.4 \times 10^{-6}\text{ K}^{-1}$
* Thermal mismatch strain: $\varepsilon_{\text{th}} = 13.4 \times 10^{-6}\text{ K}^{-1} \times 60\text{ K} = 8.04 \times 10^{-4}$
* Unconstrained half-length edge displacement: $\Delta u_{\max} = \varepsilon_{\text{th}} \cdot \frac{L}{2} = 8.04 \times 10^{-4} \times 2.5 \times 10^{-3}\text{ m} = 2.01 \times 10^{-6}\text{ m} = 2.01\text{ }\mu\text{m}$
* Waveguide stack axial stiffness ($E'_{\text{wg}} = 80 \times 10^9\text{ Pa}$, $t_{\text{wg}} = 3.0 \times 10^{-6}\text{ m}$):

$$
S_{\text{wg}} = 8.0 \times 10^{10}\text{ Pa} \times 3.0 \times 10^{-6}\text{ m} = 2.4 \times 10^5\text{ N/m}
$$

**Case A — With $20\text{ }\mu\text{m}$ Siloxane Elastomer Buffer ($G_{\text{buf}} = 50\text{ MPa}$, $h_{\text{buf}} = 20\text{ }\mu\text{m}$):**

$$
k_{\text{buf}} = \sqrt{\frac{5.0 \times 10^7\text{ Pa}}{2.0 \times 10^{-5}\text{ m} \times 2.4 \times 10^5\text{ N/m}}} = \sqrt{\frac{5.0 \times 10^7}{4.8}\text{ m}^{-2}} = 3227.49\text{ m}^{-1} = 3.227\text{ mm}^{-1}
$$

Since $k_{\text{buf}} \frac{L}{2} = 3.227\text{ mm}^{-1} \times 2.5\text{ mm} = 8.069$ and $\tanh(8.069) = 0.9999998 \approx 1.0$:

$$
\tau_{\max,\text{buf}} = \frac{5.0 \times 10^7\text{ Pa}}{2.0 \times 10^{-5}\text{ m} \times 3227.49\text{ m}^{-1}} \times 8.04 \times 10^{-4} \times 1.0 = 7.746 \times 10^8\text{ Pa} \times 8.04 \times 10^{-4} = 6.228 \times 10^5\text{ Pa} \approx 0.623\text{ MPa}
$$

The maximum shear strain inside the elastomer pad is $\gamma_{\max} = \frac{0.623\text{ MPa}}{50\text{ MPa}} = 0.01246\text{ rad}$ ($1.25\%$), well below the elastomer tear limit ($>100\%$).

**Case B — Rigid Direct Bonding without Elastomer Buffer ($G_{\text{rig}} = 2000\text{ MPa}$, $h_{\text{rig}} = 2.0\text{ }\mu\text{m}$):**

$$
k_{\text{rig}} = \sqrt{\frac{2.0 \times 10^9\text{ Pa}}{2.0 \times 10^{-6}\text{ m} \times 2.4 \times 10^5\text{ N/m}}} = \sqrt{4.1667 \times 10^9\text{ m}^{-2}} = 64549.7\text{ m}^{-1} = 64.55\text{ mm}^{-1}
$$

$$
\tau_{\max,\text{rig}} = \frac{2.0 \times 10^9\text{ Pa}}{2.0 \times 10^{-6}\text{ m} \times 64549.7\text{ m}^{-1}} \times 8.04 \times 10^{-4} \times 1.0 = 1.5492 \times 10^{10}\text{ Pa} \times 8.04 \times 10^{-4} = 1.2456 \times 10^7\text{ Pa} \approx 12.46\text{ MPa}
$$

Thus, the $20\text{ }\mu\text{m}$ elastomer buffer reduces interfacial shear stress by a factor of $\frac{12.46}{0.623} = 20.0$, preventing edge delamination.

---

### 5.2 Optical Waveguide Confinement, Evanescent Socket Coupling, and Link Loss Budget

#### Step 1: High-Contrast Waveguide Confinement Factor
For an $\text{a-Si:H}$ core ($n_{\text{core}} = 3.48$) clad in $\text{SiO}_2$ ($n_{\text{clad}} = 1.444$) operating at free-space wavelength $\lambda_0 = 1550\text{ nm}$ ($k_0 = \frac{2\pi}{\lambda_0} = 4.0537 \times 10^6\text{ m}^{-1}$), the numerical aperture ($\text{NA}$) is:

$$
\text{NA} = \sqrt{n_{\text{core}}^2 - n_{\text{clad}}^2} = \sqrt{3.48^2 - 1.444^2} = \sqrt{12.1104 - 2.0851} = \sqrt{10.0253} \approx 3.166
$$

For the fundamental quasi-$\text{TE}_{00}$ mode in a $w = 450\text{ nm} \times h = 220\text{ nm}$ strip waveguide, the effective index is $n_{\text{eff,strip}} \approx 2.42$. In the un-tapered strip section, the vertical evanescent decay constant $\gamma_{\text{air}}$ into an air gap ($n_{\text{air}} = 1.00$) would be:

$$
\gamma_{\text{air}} = k_0 \sqrt{n_{\text{eff,strip}}^2 - n_{\text{air}}^2} = 4.0537 \times 10^6\text{ m}^{-1} \times \sqrt{2.42^2 - 1.00^2} = 8.93 \times 10^6\text{ m}^{-1}
$$

This corresponds to a $1/e$ intensity penetration depth of $d_{1/e} = \frac{1}{2\gamma_{\text{air}}} \approx 56\text{ nm}$, confirming why a $500\text{ nm}$ air gap cannot couple light efficiently.

#### Step 2: Mode Expansion via Adiabatic Inverse Nanotaper & Index-Matched Pad
By tapering the waveguide width linearly from $w_0 = 450\text{ nm}$ down to $w_{\text{tip}} = 100\text{ nm}$ over an adiabatic taper length $L_{\text{taper}} = 150\text{ }\mu\text{m}$ (satisfying the adiabatic criterion $L_{\text{taper}} \gg \frac{w^2}{\lambda_{\text{eff}}}$) and surrounding the coupling window with the silicone elastomer pad ($n_{\text{pad}} = 1.50$), the effective index drops to $n_{\text{eff,tip}} \approx 1.54$. The vertical evanescent decay constant into the elastomer pad becomes:

$$
\gamma_{\text{pad}} = k_0 \sqrt{n_{\text{eff,tip}}^2 - n_{\text{pad}}^2} = 4.0537 \times 10^6\text{ m}^{-1} \times \sqrt{1.54^2 - 1.50^2} = 4.0537 \times 10^6 \times 0.3487 = 1.414 \times 10^6\text{ m}^{-1}
$$

The mode field expands vertically across the $150\text{ nm}$ thinned cladding and elastomer pad, yielding an overlap integral $\eta_{\text{overlap}} = 0.861$ between the chip nanotaper and bridge nanotaper (including $\pm 0.5\text{ }\mu\text{m}$ lateral alignment tolerance):

$$
\alpha_{\text{couple}} = -10 \log_{10}(\eta_{\text{overlap}}) = -10 \log_{10}(0.861) = 0.65\text{ dB per interface}
$$

Similarly, normal-incidence Fresnel power reflection between the $\text{SiO}_2$ cladding ($n_{\text{clad}} = 1.444$) and the silicone elastomer pad ($n_{\text{pad}} = 1.50$) is reduced to:

$$
R_{\text{Fresnel}} = \left(\frac{n_{\text{pad}} - n_{\text{clad}}}{n_{\text{pad}} + n_{\text{clad}}}\right)^2 = \left(\frac{1.500 - 1.444}{1.500 + 1.444}\right)^2 = \left(\frac{0.056}{2.944}\right)^2 = 3.62 \times 10^{-4} \quad (-34.4\text{ dB return loss})
$$

#### Step 3: Total Optical Link Loss Budget ($\alpha_{\text{total}}$) over $L = 5.0\text{ mm}$ ($0.5\text{ cm}$)
Summing all attenuation mechanisms along the $0.5\text{ cm}$ optical path:
1. Input adiabatic socket coupling ($\alpha_{\text{couple,in}}$): $0.65\text{ dB}$
2. Waveguide propagation in $\text{a-Si:H}$ ($\alpha_{\text{prop}} = 1.80\text{ dB/cm} \times 0.50\text{ cm}$): $0.90\text{ dB}$
3. Two adaptive S-bends ($R = 50\text{ }\mu\text{m}$, $2 \times 0.08\text{ dB}$): $0.16\text{ dB}$
4. Output adiabatic socket coupling ($\alpha_{\text{couple,out}}$): $0.65\text{ dB}$
5. System aging & thermal drift margin ($\alpha_{\text{margin}}$): $0.50\text{ dB}$

$$
\alpha_{\text{total}} = \alpha_{\text{couple,in}} + \alpha_{\text{prop}} + \alpha_{\text{bend}} + \alpha_{\text{couple,out}} + \alpha_{\text{margin}} = 0.65 + 0.90 + 0.16 + 0.65 + 0.50 = 2.86\text{ dB}
$$

The linear optical transmittance from TX modulator output to RX photodetector input is:

$$
T_{\text{opt}} = 10^{-\frac{\alpha_{\text{total}}}{10}} = 10^{-0.286} \approx 0.5176 \quad (51.8\%\text{ optical power transmission})
$$

---

### 5.3 Optoelectronic Energy Efficiency ($\text{pJ/bit}$) & Aggregate Bandwidth Derivation

#### Step 1: Laser Power and Bit Energy Derivation
For DSP-free Non-Return-to-Zero (NRZ) direct detection at a per-wavelength data rate of $R_\lambda = 64\text{ Gbit/s}$ ($6.4 \times 10^{10}\text{ bit/s}$) and a bit-error rate $\text{BER} \le 10^{-12}$ ($Q = 7.03$), a high-speed Germanium-on-Silicon ($\text{Ge-on-Si}$) waveguide photodiode (responsivity $\mathcal{R} = 1.05\text{ A/W}$, total input capacitance $C_{\text{PD}} = 12\text{ fF}$) requires a minimum received optical power of:

$$
P_{\text{RX,min}} = -14.0\text{ dBm} = 10^{-\frac{14.0}{10}}\text{ mW} = 0.03981\text{ mW}
$$

Accounting for the on-chip electro-optic ring/Mach-Zehnder modulator insertion loss ($\alpha_{\text{mod}} = 2.50\text{ dB}$) and the total printed bridge attenuation ($\alpha_{\text{total}} = 2.86\text{ dB}$), the required optical continuous-wave (CW) power per wavelength channel entering the modulator is:

$$
P_{\text{opt,in (dBm)}} = P_{\text{RX,min}} + \alpha_{\text{total}} + \alpha_{\text{mod}} = -14.0\text{ dBm} + 2.86\text{ dB} + 2.50\text{ dB} = -8.64\text{ dBm}
$$

Converting $-8.64\text{ dBm}$ to linear milliwatts:

$$
P_{\text{opt,in}} = 10^{-\frac{8.64}{10}}\text{ mW} = 0.13677\text{ mW}
$$

With an external comb-laser wall-plug efficiency of $\eta_{\text{WPE}} = 0.20$ ($20\%$), the electrical power consumed by the laser source per wavelength channel is:

$$
P_{\text{el,laser}} = \frac{P_{\text{opt,in}}}{\eta_{\text{WPE}}} = \frac{0.13677\text{ mW}}{0.20} = 0.6839\text{ mW}
$$

Dividing by the single-wavelength bit rate $R_\lambda = 6.4 \times 10^{10}\text{ bit/s}$ gives the laser energy per bit:

$$
E_{\text{laser}} = \frac{P_{\text{el,laser}}}{R_\lambda} = \frac{0.6839 \times 10^{-3}\text{ W}}{6.4 \times 10^{10}\text{ bit/s}} = 1.069 \times 10^{-14}\text{ J/bit} \approx 0.011\text{ pJ/bit}
$$

#### Step 2: Complete Transceiver Energy Breakdown
1. **CW Comb Laser Electrical Supply ($E_{\text{laser}}$):** $0.011\text{ pJ/bit}$
2. **TX Depletion Modulator Driver ($E_{\text{TX}} = \frac{1}{4} C_{\text{mod}} V_{\text{pp}}^2$, with $C_{\text{mod}} = 60\text{ fF}, V_{\text{pp}} = 0.9\text{ V}$, plus pre-driver):** $0.120\text{ pJ/bit}$
3. **RX Photodiode Bias & CMOS Transimpedance Amplifier ($E_{\text{RX}}$):** $0.180\text{ pJ/bit}$
4. **Clocking, Serializer/Deserializer & Wavelength Thermal Locking ($E_{\text{SerDes}}$):** $0.150\text{ pJ/bit}$

$$
E_{\text{total}} = E_{\text{laser}} + E_{\text{TX}} + E_{\text{RX}} + E_{\text{SerDes}} = 0.011 + 0.120 + 0.180 + 0.150 = 0.461\text{ pJ/bit}
$$

#### Step 3: Aggregate Throughput & Power Scaling as a Function of Bridge Width $W$
Each printed $\text{a-Si:H}$ waveguide carries $M = 8$ dense wavelength-division multiplexed (DWDM) channels at $R_\lambda = 64\text{ Gbit/s}$:

$$
R_{\text{wg}} = M \cdot R_\lambda = 8 \times 64\text{ Gbit/s} = 512\text{ Gbit/s} = 64\text{ GB/s} = 0.064\text{ TB/s}
$$

At a waveguide center-to-center pitch of $p = 5.0\text{ }\mu\text{m}$ (ensuring inter-waveguide crosstalk $< -35\text{ dB}$ over $5.0\text{ mm}$), the total number of waveguides per millimeter of bridge width is:

$$
\rho_{\text{wg}} = \frac{1\text{ mm}}{5.0 \times 10^{-3}\text{ mm}} = 200\text{ waveguides/mm}
$$

Splitting the array equally into $N_{\text{TX}}(W) = 100 \cdot W_{\text{[mm]}}$ transmit waveguides and $N_{\text{RX}}(W) = 100 \cdot W_{\text{[mm]}}$ receive waveguides yields the closed-form scaling laws for unidirectional throughput $B_{\text{uni}}(W)$, bidirectional throughput $B_{\text{bi}}(W)$, and unidirectional electrical power $P_{\text{el,uni}}(W)$:

$$
B_{\text{uni}}(W) = N_{\text{TX}}(W) \cdot R_{\text{wg}} = 100 \cdot W_{\text{[mm]}} \cdot 0.064\text{ TB/s} = 6.40 \cdot W_{\text{[mm]}}\text{ [TB/s]}
$$

$$
B_{\text{bi}}(W) = 2 \cdot B_{\text{uni}}(W) = 12.80 \cdot W_{\text{[mm]}}\text{ [TB/s]}
$$

$$
P_{\text{el,uni}}(W) = B_{\text{uni}}(W) \cdot \left(8 \times 10^{12}\text{ bit/TB}\right) \cdot \left(0.461 \times 10^{-12}\text{ J/bit}\right) = 3.688 \cdot B_{\text{uni}}(W)\text{ [W]} = 23.603 \cdot W_{\text{[mm]}}\text{ [W]}
$$

#### Step 4: Architectural Benchmark Table

| Inlay Configuration | Active Width $W$ | Waveguides ($\text{TX} + \text{RX}$) | Unidirectional Bandwidth $B_{\text{uni}}$ | Bidirectional Bandwidth $B_{\text{bi}}$ | Electrical Power $P_{\text{el,uni}}$ | Ratio vs. TPU 8i Total HBM ($8.6\text{ TB/s}$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Compact Inlay** | $1.6\text{ mm}$ | $160 + 160$ ($320$) | $10.24\text{ TB/s}$ | $20.48\text{ TB/s}$ | $37.77\text{ W}$ | $1.19\times\text{ uni} \;/\; 2.38\times\text{ bi}$ |
| **Medium Die-Edge Inlay** | $8.0\text{ mm}$ | $800 + 800$ ($1600$) | $51.20\text{ TB/s}$ | $102.40\text{ TB/s}$ | $188.83\text{ W}$ | $5.95\times\text{ uni} \;/\; 11.91\times\text{ bi}$ |
| **Full Die-Flank Inlay** | $15.0\text{ mm}$ | $1500 + 1500$ ($3000$) | $96.00\text{ TB/s}$ | $192.00\text{ TB/s}$ | $354.05\text{ W}$ | $11.16\times\text{ uni} \;/\; 22.32\times\text{ bi}$ |