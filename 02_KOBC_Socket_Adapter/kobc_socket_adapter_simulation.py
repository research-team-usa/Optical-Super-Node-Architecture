#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
PROJECT: Kinematic Optical Bridge Cartridge (KOBC) - Socket Adapter Simulation
MODULE:  Gent-Lindley Pad Mechanics, 3-V Hertz Kinematics, Thermals & TPU Scaling
Lead Architect: Emanuel Schaaf
Framework:      Open Origin Architecture
===============================================================================
Description:
Complete headless animation script for computing and progressively visualizing
the detachable KOBC socket adapter:
1. Gent-Lindley compression profile (Micro-pillows S=5.0 vs. Solid pad S=37.13)
2. Maxwell 3-V kinematics (Hertzian contact stress p_0 & 57.4 nm repeatability)
3. Thermal cold-plate shunt (ΔT_wg = 1.09 K & thermo-optic shift Δn_eff)
4. Modular bandwidth scaling across Google TPU generations (MOBU grid)
===============================================================================
"""

# 1. Safeguarded Core System and Scientific Module Imports
try:
    import sys
    import os
    import traceback
except ImportError as exc:
    print(f"[CRITICAL ERROR] Standard system modules missing: {exc}")
    input("Press Enter to exit...")
    raise SystemExit(1)

try:
    import matplotlib
    # Headless configuration immediately after import
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.gridspec import GridSpec
except ImportError as exc:
    print(f"[ERROR] Failed to load Matplotlib: {exc}")
    print("Please install matplotlib via: pip install matplotlib")
    input("Press Enter to exit...")
    sys.exit(1)

try:
    import numpy as np
except ImportError as exc:
    print(f"[ERROR] Failed to load NumPy: {exc}")
    print("Please install numpy via: pip install numpy")
    input("Press Enter to exit...")
    sys.exit(1)

try:
    import scipy.constants as const
except ImportError as exc:
    print(f"[ERROR] Failed to load SciPy: {exc}")
    print("Please install scipy via: pip install scipy")
    input("Press Enter to exit...")
    sys.exit(1)


# =============================================================================
# FIRST-PRINCIPLES PHYSICAL AND MECHANICAL MODEL COMPUTATION
# =============================================================================
def compute_kobc_simulation_data(num_points=500):
    """
    Computes all mechanical, kinematic, thermal, and optical state variables
    of the KOBC socket adapter from first principles.
    """
    # -------------------------------------------------------------------------
    # PANEL 1: Gent-Lindley Elastomer Compression across Δh in [0, 250 nm]
    # -------------------------------------------------------------------------
    dh_nm = np.linspace(0.0, 250.0, num_points)
    t_pad_nm = 2000.0                           # Pad thickness: 2.0 µm = 2000 nm
    eps_z = dh_nm / t_pad_nm                    # Vertical compressive strain ε_z

    E0_mpa = 0.45                               # Intrinsic Young's modulus (Shore OO 35)
    k_el = 0.85                                 # Gent-Lindley material factor

    # Case A: Micro-castellated pillow pad (40x40 µm pillows, 10 µm channels)
    a_pil_um = 40.0
    t_pad_um = 2.0
    S_pil = a_pil_um / (4.0 * t_pad_um)         # S = 5.000
    E_eff_pil_mpa = E0_mpa * (1.0 + 2.0 * k_el * (S_pil ** 2))  # 19.575 MPa
    A_total_mm2 = 2.0 * (15.0 * 0.15)           # 2 windows of 2.25 mm² = 4.50 mm²
    fill_factor = 0.80                          # A_eff = 3.60 mm²
    A_eff_pil_mm2 = A_total_mm2 * fill_factor
    F_pil_n = E_eff_pil_mpa * eps_z * A_eff_pil_mm2

    # Case B: Continuous solid pad without relief channels (Hydrostatic lock)
    W_mm = 15.0
    L_pad_mm = 0.15
    t_pad_mm = 0.002
    S_cont = (W_mm * L_pad_mm) / (2.0 * (W_mm + L_pad_mm) * t_pad_mm)  # 37.129
    E_eff_cont_mpa = E0_mpa * (1.0 + 2.0 * k_el * (S_cont ** 2))       # 1055.07 MPa
    F_cont_n = E_eff_cont_mpa * eps_z * A_total_mm2

    # -------------------------------------------------------------------------
    # PANEL 2: Maxwell 3-V Kinematics & Hertzian Contact Mechanics
    # -------------------------------------------------------------------------
    # Net kinematic seating force F_kin from 0.10 N to 8.00 N
    # (Operating point: F_latch = 12.00 N - F_pad(200nm) = 7.047 N -> F_kin = 4.953 N)
    F_kin_n = np.linspace(0.10, 8.00, num_points)
    F_sphere_n = F_kin_n / 3.0                  # 3 ruby microspheres
    theta_v_rad = np.arccos(1.0 / np.sqrt(3.0)) # KOH <111> facet angle: 54.736°
    F_norm_n = F_sphere_n / (2.0 * np.cos(theta_v_rad))

    # Reduced contact modulus E* (Ruby E1=370 GPa, v1=0.22; Si/Si3N4 E2=169 GPa, v2=0.28)
    E1_pa, nu1 = 370.0e9, 0.22
    E2_pa, nu2 = 169.0e9, 0.28
    inv_E_star = ((1.0 - nu1 ** 2) / E1_pa) + ((1.0 - nu2 ** 2) / E2_pa)
    E_star_pa = 1.0 / inv_E_star                # 124.61 GPa
    R_sphere_m = 200.0e-6                       # Sphere radius 200 µm (Ø 400 µm)

    # Hertzian contact radius a, peak pressure p_0, and elastic approach δ_n
    a_contact_m = ((3.0 * F_norm_n * R_sphere_m) / (4.0 * E_star_pa)) ** (1.0 / 3.0)
    p0_gpa = ((3.0 * F_norm_n) / (2.0 * const.pi * (a_contact_m ** 2))) * 1e-9
    delta_n_m = (a_contact_m ** 2) / R_sphere_m

    # Lateral centering repeatability Δr_rep = μ * δ_n (in nm) at μ = 0.08
    mu_fric = 0.08
    repeatability_nm = mu_fric * delta_n_m * 1e9

    # -------------------------------------------------------------------------
    # PANEL 3: Thermal Shunt & Thermo-Optic Stability across T_die [40..100 °C]
    # -------------------------------------------------------------------------
    T_die_c = np.linspace(40.0, 100.0, num_points)
    T_cold_c = 40.0                             # Cold-plate flange temperature: 40.0 °C

    # Thermal resistances in the KOBC module (Shunted design with aerogel trench)
    R_th_bot_shunt = 185.0                      # K/W (with 10 µm aerogel isolation trench)
    R_th_top_shunt = 4.611                      # K/W (LAS carrier + Cu-Graphene + In pad)
    shunt_ratio = R_th_top_shunt / (R_th_bot_shunt + R_th_top_shunt)

    dT_wg_shunt_k = (T_die_c - T_cold_c) * shunt_ratio
    dn_dt_asi = 2.1e-4                          # Thermo-optic coefficient of a-Si:H (1/K)
    dn_eff_shunt = dn_dt_asi * dT_wg_shunt_k

    # Reference comparison: Uncooled bridge without shunt & without isolation trench
    R_th_bot_uncooled = 24.8                    # K/W
    R_th_top_conv = 140.0                       # K/W (passive convection/enclosure only)
    uncooled_ratio = R_th_top_conv / (R_th_bot_uncooled + R_th_top_conv)
    dT_wg_uncooled_k = (T_die_c - T_cold_c) * uncooled_ratio
    dn_eff_uncooled = dn_dt_asi * dT_wg_uncooled_k

    # -------------------------------------------------------------------------
    # PANEL 4: Modular KOBC Scaling across MOBU Units [0..40 MOBU]
    # -------------------------------------------------------------------------
    # 1 MOBU = 1.60 mm width = 320 waveguides = 20.48 TB/s bidirectional
    mobu_units = np.linspace(0.0, 40.0, num_points)
    bw_bi_tbs = mobu_units * 20.48              # Bidirectional throughput in TB/s
    bw_uni_tbs = mobu_units * 10.24             # Unidirectional throughput in TB/s
    pwr_uni_w = bw_uni_tbs * 8.0 * 0.461        # Power consumption at 0.461 pJ/bit

    return {
        "dh_nm": dh_nm,
        "F_pil_n": F_pil_n,
        "F_cont_n": F_cont_n,
        "S_pil": S_pil,
        "S_cont": S_cont,
        "F_kin_n": F_kin_n,
        "p0_gpa": p0_gpa,
        "repeatability_nm": repeatability_nm,
        "T_die_c": T_die_c,
        "dT_wg_shunt_k": dT_wg_shunt_k,
        "dT_wg_uncooled_k": dT_wg_uncooled_k,
        "dn_eff_shunt": dn_eff_shunt,
        "dn_eff_uncooled": dn_eff_uncooled,
        "mobu_units": mobu_units,
        "bw_bi_tbs": bw_bi_tbs,
        "bw_uni_tbs": bw_uni_tbs,
        "pwr_uni_w": pwr_uni_w,
    }


# =============================================================================
# MAIN VISUALIZATION AND ANIMATION ENGINE
# =============================================================================
def run_kobc_simulation():
    """
    Creates the 4-panel dark-mode dashboard for the KOBC socket adapter,
    progressively animates all trajectories, and saves MP4 (Fallback: GIF) + PNG.
    """
    print("=" * 78)
    print("STARTING SIMULATION: Kinematic Optical Bridge Cartridge (KOBC Socket System)")
    print("Lead Architect: Emanuel Schaaf | Open Origin Architecture")
    print("=" * 78)

    data = compute_kobc_simulation_data(num_points=500)
    num_pts = len(data["dh_nm"])
    num_frames = 125

    # Dark-mode color scheme strictly adhering to architectural specification
    plt.style.use("dark_background")
    BG_FIG = "#0d1117"
    BG_AX = "#161b22"
    GRID_COL = "#30363d"
    COL_CYAN = "#00ffcc"
    COL_MAGENTA = "#ff00ff"
    COL_YELLOW = "#ffd700"
    TEXT_COL = "#e6edf3"

    fig = plt.figure(figsize=(16.5, 9.8), dpi=130, facecolor=BG_FIG)
    gs = GridSpec(2, 2, figure=fig, height_ratios=[1.0, 1.0], hspace=0.35, wspace=0.28)

    ax1 = fig.add_subplot(gs[0, 0], facecolor=BG_AX)
    ax1_r = ax1.twinx()

    ax2 = fig.add_subplot(gs[0, 1], facecolor=BG_AX)
    ax2_r = ax2.twinx()

    ax3 = fig.add_subplot(gs[1, 0], facecolor=BG_AX)
    ax3_r = ax3.twinx()

    ax4 = fig.add_subplot(gs[1, 1], facecolor=BG_AX)
    ax4_r = ax4.twinx()

    fig.suptitle(
        "KINEMATIC OPTICAL BRIDGE CARTRIDGE (KOBC) – MECHANICAL, THERMAL & SCALING SIMULATION\n"
        "Lead Architect: Emanuel Schaaf | Open Origin Architecture",
        fontsize=13.5,
        fontweight="bold",
        color=COL_CYAN,
        y=0.97,
    )

    # -------------------------------------------------------------------------
    # PANEL 1: Gent-Lindley Compression (Micro-Pillows vs. Solid Pad)
    # -------------------------------------------------------------------------
    ax1.set_title(
        "1. Gent-Lindley Pad Mechanics: Micro-Pillows (S=5.0) vs. Solid Pad (S=37.1)",
        color=TEXT_COL, fontsize=10.5, fontweight="bold", pad=9,
    )
    ax1.set_xlabel("Vertical Pad Compression Δh [nm] (Target: 200 nm)", color=TEXT_COL)
    ax1.set_ylabel("Micro-Pillow Pad Clamping Force [N]", color=COL_CYAN)
    ax1_r.set_ylabel("Solid Pad Locking Force (No Channels) [N]", color=COL_MAGENTA)

    ax1.set_xlim(0.0, 250.0)
    ax1.set_ylim(0.0, 15.0)
    ax1_r.set_ylim(0.0, 650.0)
    ax1.grid(True, color=GRID_COL, linestyle="--", linewidth=0.7, alpha=0.8)

    ax1.axvline(200.0, color=GRID_COL, linestyle="-.", linewidth=1.1)
    ax1.axhline(
        12.0, color=COL_YELLOW, linestyle=":", linewidth=1.5,
        label="Ti-6Al-4V Spring Latch F_latch (12.00 N)"
    )

    (line_f_pil,) = ax1.plot(
        [], [], color=COL_CYAN, linewidth=2.6,
        label="Micro-Pillow Pad (7.05 N @ 200 nm)"
    )
    (line_f_cont,) = ax1_r.plot(
        [], [], color=COL_MAGENTA, linewidth=2.1, linestyle="--",
        label="Solid Pad without Channels (474.8 N @ 200 nm)"
    )
    (dot_f_pil,) = ax1.plot([], [], "o", color=COL_CYAN, markersize=7)
    (dot_f_cont,) = ax1_r.plot([], [], "s", color=COL_MAGENTA, markersize=6)

    text_p1 = ax1.text(
        0.03, 0.52, "", transform=ax1.transAxes, color=TEXT_COL, fontsize=8.5,
        bbox=dict(boxstyle="round,pad=0.35", facecolor=BG_FIG, edgecolor=GRID_COL, alpha=0.92),
    )
    lines_p1 = [line_f_pil, line_f_cont]
    ax1.legend(
        lines_p1, [l.get_label() for l in lines_p1],
        loc="upper left", fontsize=8.0, facecolor=BG_FIG, edgecolor=GRID_COL,
    )

    # -------------------------------------------------------------------------
    # PANEL 2: Maxwell 3-V Kinematics (Hertzian Stress & Repeatability)
    # -------------------------------------------------------------------------
    ax2.set_title(
        "2. Maxwell 3-V Kinematics: Centering Precision & Hertzian Stress",
        color=TEXT_COL, fontsize=10.5, fontweight="bold", pad=9,
    )
    ax2.set_xlabel("Net Kinematic Seating Force F_kin = F_latch - F_pad [N]", color=TEXT_COL)
    ax2.set_ylabel("Centering Repeatability Δr_rep [nm]", color=COL_CYAN)
    ax2_r.set_ylabel("Hertzian Contact Stress p_0 [GPa]", color=COL_MAGENTA)

    ax2.set_xlim(0.10, 8.00)
    ax2.set_ylim(0.0, 95.0)
    ax2_r.set_ylim(0.0, 7.8)
    ax2.grid(True, color=GRID_COL, linestyle="--", linewidth=0.7, alpha=0.8)

    ax2.axvline(4.953, color=GRID_COL, linestyle="-.", linewidth=1.1)
    ax2_r.axhline(
        7.0, color=COL_YELLOW, linestyle=":", linewidth=1.5,
        label="Silicon V-Groove Yield Limit (7.0 GPa)"
    )

    (line_rep,) = ax2.plot(
        [], [], color=COL_CYAN, linewidth=2.6,
        label="Repeatability Δr_rep (57.4 nm @ 4.95 N)"
    )
    (line_p0,) = ax2_r.plot(
        [], [], color=COL_MAGENTA, linewidth=2.2, linestyle="--",
        label="Hertzian Stress p_0 (4.75 GPa @ 4.95 N)"
    )
    (dot_rep,) = ax2.plot([], [], "o", color=COL_CYAN, markersize=7)
    (dot_p0,) = ax2_r.plot([], [], "s", color=COL_MAGENTA, markersize=6)

    text_p2 = ax2.text(
        0.03, 0.50, "", transform=ax2.transAxes, color=TEXT_COL, fontsize=8.5,
        bbox=dict(boxstyle="round,pad=0.35", facecolor=BG_FIG, edgecolor=GRID_COL, alpha=0.92),
    )
    lines_p2 = [line_rep, line_p0]
    ax2.legend(
        lines_p2, [l.get_label() for l in lines_p2],
        loc="upper left", fontsize=8.0, facecolor=BG_FIG, edgecolor=GRID_COL,
    )

    # -------------------------------------------------------------------------
    # PANEL 3: Thermal Cold-Plate Shunt & Thermo-Optic Stability
    # -------------------------------------------------------------------------
    ax3.set_title(
        "3. Thermal Shunt: Waveguide Temperature Rise ΔT_wg vs. Die Temp",
        color=TEXT_COL, fontsize=10.5, fontweight="bold", pad=9,
    )
    ax3.set_xlabel("TPU Die Edge Temperature T_die [°C] (Cold Plate = 40 °C)", color=TEXT_COL)
    ax3.set_ylabel("Temp Rise ΔT_wg (KOBC with Shunt) [K]", color=COL_CYAN)
    ax3_r.set_ylabel("Temp Rise ΔT_wg (Without Shunt) [K]", color=COL_MAGENTA)

    ax3.set_xlim(40.0, 100.0)
    ax3.set_ylim(0.0, 3.0)
    ax3_r.set_ylim(0.0, 60.0)
    ax3.grid(True, color=GRID_COL, linestyle="--", linewidth=0.7, alpha=0.8)

    ax3.axvline(85.0, color=GRID_COL, linestyle="-.", linewidth=1.1)
    ax3.axhline(
        2.0, color=COL_YELLOW, linestyle=":", linewidth=1.5,
        label="Thermo-Optic Stability Limit (2.0 K)"
    )

    (line_dt_shunt,) = ax3.plot(
        [], [], color=COL_CYAN, linewidth=2.6,
        label="KOBC with Cold-Plate Shunt (1.09 K @ 85 °C)"
    )
    (line_dt_unc,) = ax3_r.plot(
        [], [], color=COL_MAGENTA, linewidth=2.1, linestyle="--",
        label="Uncooled Bridge without Shunt (38.2 K @ 85 °C)"
    )
    (dot_dt_shunt,) = ax3.plot([], [], "o", color=COL_CYAN, markersize=7)
    (dot_dt_unc,) = ax3_r.plot([], [], "s", color=COL_MAGENTA, markersize=6)

    text_p3 = ax3.text(
        0.03, 0.48, "", transform=ax3.transAxes, color=TEXT_COL, fontsize=8.5,
        bbox=dict(boxstyle="round,pad=0.35", facecolor=BG_FIG, edgecolor=GRID_COL, alpha=0.92),
    )
    lines_p3 = [line_dt_shunt, line_dt_unc]
    ax3.legend(
        lines_p3, [l.get_label() for l in lines_p3],
        loc="upper left", fontsize=8.0, facecolor=BG_FIG, edgecolor=GRID_COL,
    )

    # -------------------------------------------------------------------------
    # PANEL 4: Modular TPU Scaling (MOBU Grid up to TPU 9 4-Flanks)
    # -------------------------------------------------------------------------
    ax4.set_title(
        "4. Modular KOBC Scaling (1 MOBU = 1.6 mm = 20.48 TB/s bi)",
        color=TEXT_COL, fontsize=10.5, fontweight="bold", pad=9,
    )
    ax4.set_xlabel("Number of Plugged MOBU Units N (TPU v1 to TPU 9 4-Flanks)", color=TEXT_COL)
    ax4.set_ylabel("Total Bidirectional Throughput [TB/s]", color=COL_CYAN)
    ax4_r.set_ylabel("Unidirectional Electrical Power [W] (@ 0.461 pJ/bit)", color=COL_YELLOW)

    ax4.set_xlim(0.0, 40.0)
    ax4.set_ylim(0.0, 900.0)
    ax4_r.set_ylim(0.0, 1700.0)
    ax4.grid(True, color=GRID_COL, linestyle="--", linewidth=0.7, alpha=0.8)

    # Markers for key TPU scaling configurations
    for n_mobu, lbl in [
        (5.0, "TPU v2–v6e\n(5× = 102.4 TB/s)"),
        (10.0, "TPU 8i Flank\n(10× = 204.8 TB/s)"),
        (20.0, "TPU 8i Max\n(20× = 409.6 TB/s)"),
        (40.0, "TPU 9 (4 Flanks)\n(40× = 819.2 TB/s)"),
    ]:
        ax4.axvline(n_mobu, color=GRID_COL, linestyle="-.", linewidth=0.9)
        ax4.text(
            n_mobu - 0.6 if n_mobu == 40.0 else n_mobu + 0.5,
            735.0 if n_mobu in (5.0, 20.0) else 610.0,
            lbl, color=TEXT_COL, fontsize=7.5,
            ha="right" if n_mobu == 40.0 else "left",
            bbox=dict(boxstyle="round,pad=0.2", facecolor=BG_FIG, edgecolor=GRID_COL, alpha=0.85),
        )

    (line_bw_bi,) = ax4.plot(
        [], [], color=COL_CYAN, linewidth=2.7,
        label="Bidirectional Throughput [TB/s]"
    )
    (line_bw_uni,) = ax4.plot(
        [], [], color=COL_MAGENTA, linewidth=2.1,
        label="Unidirectional Throughput [TB/s]"
    )
    (line_pwr_4,) = ax4_r.plot(
        [], [], color=COL_YELLOW, linewidth=2.0, linestyle="--",
        label="Electrical Power uni [W]"
    )
    (dot_bw_bi,) = ax4.plot([], [], "o", color=COL_CYAN, markersize=7)
    (dot_bw_uni,) = ax4.plot([], [], "o", color=COL_MAGENTA, markersize=6)
    (dot_pwr_4,) = ax4_r.plot([], [], "s", color=COL_YELLOW, markersize=6)

    text_p4 = ax4.text(
        0.03, 0.44, "", transform=ax4.transAxes, color=TEXT_COL, fontsize=8.5,
        bbox=dict(boxstyle="round,pad=0.35", facecolor=BG_FIG, edgecolor=GRID_COL, alpha=0.92),
    )
    lines_p4 = [line_bw_bi, line_bw_uni, line_pwr_4]
    ax4.legend(
        lines_p4, [l.get_label() for l in lines_p4],
        loc="upper left", fontsize=8.0, facecolor=BG_FIG, edgecolor=GRID_COL,
    )

    # Axis styling for all primary and secondary axes
    for axis_obj in [ax1, ax1_r, ax2, ax2_r, ax3, ax3_r, ax4, ax4_r]:
        axis_obj.tick_params(colors=TEXT_COL, labelsize=8.5)
        for spine in axis_obj.spines.values():
            spine.set_color(GRID_COL)

    # -------------------------------------------------------------------------
    # ANIMATION UPDATE FUNCTION
    # -------------------------------------------------------------------------
    def init():
        for ln in [
            line_f_pil, line_f_cont, dot_f_pil, dot_f_cont,
            line_rep, line_p0, dot_rep, dot_p0,
            line_dt_shunt, line_dt_unc, dot_dt_shunt, dot_dt_unc,
            line_bw_bi, line_bw_uni, line_pwr_4, dot_bw_bi, dot_bw_uni, dot_pwr_4,
        ]:
            ln.set_data([], [])
        for txt in [text_p1, text_p2, text_p3, text_p4]:
            txt.set_text("")
        return (
            line_f_pil, line_f_cont, dot_f_pil, dot_f_cont,
            line_rep, line_p0, dot_rep, dot_p0,
            line_dt_shunt, line_dt_unc, dot_dt_shunt, dot_dt_unc,
            line_bw_bi, line_bw_uni, line_pwr_4, dot_bw_bi, dot_bw_uni, dot_pwr_4,
            text_p1, text_p2, text_p3, text_p4,
        )

    def update(frame):
        active_frames = num_frames - 15
        progress = min(1.0, (frame + 1) / float(active_frames))
        idx = max(1, int(progress * num_pts))

        # 1. Gent-Lindley Pad Compression
        dh_s = data["dh_nm"][:idx]
        fp_s = data["F_pil_n"][:idx]
        fc_s = data["F_cont_n"][:idx]
        line_f_pil.set_data(dh_s, fp_s)
        line_f_cont.set_data(dh_s, fc_s)
        dot_f_pil.set_data([dh_s[-1]], [fp_s[-1]])
        dot_f_cont.set_data([dh_s[-1]], [fc_s[-1]])
        text_p1.set_text(
            f"Compression Δh:   {dh_s[-1]:5.1f} nm\n"
            f"Micro-Pillows:    {fp_s[-1]:5.2f} N (S=5.00)\n"
            f"Solid Pad (rigid):{fc_s[-1]:5.1f} N (S=37.13)\n"
            f"Reduction Factor: 67.4× less force"
        )

        # 2. Maxwell 3-V Kinematics
        fk_s = data["F_kin_n"][:idx]
        rep_s = data["repeatability_nm"][:idx]
        p0_s = data["p0_gpa"][:idx]
        line_rep.set_data(fk_s, rep_s)
        line_p0.set_data(fk_s, p0_s)
        dot_rep.set_data([fk_s[-1]], [rep_s[-1]])
        dot_p0.set_data([fk_s[-1]], [p0_s[-1]])
        text_p2.set_text(
            f"Seating Force F_kin: {fk_s[-1]:5.2f} N\n"
            f"Repeatability:       {rep_s[-1]:5.1f} nm (Tol: 500 nm)\n"
            f"Hertz Stress p_0:    {p0_s[-1]:5.2f} GPa (Limit: 7.0 GPa)\n"
            f"Status: 100% Elastic 6-Point Seat"
        )

        # 3. Thermal Cold-Plate Shunt
        td_s = data["T_die_c"][:idx]
        dts_s = data["dT_wg_shunt_k"][:idx]
        dtu_s = data["dT_wg_uncooled_k"][:idx]
        dn_val = data["dn_eff_shunt"][idx - 1]
        line_dt_shunt.set_data(td_s, dts_s)
        line_dt_unc.set_data(td_s, dtu_s)
        dot_dt_shunt.set_data([td_s[-1]], [dts_s[-1]])
        dot_dt_unc.set_data([td_s[-1]], [dtu_s[-1]])
        text_p3.set_text(
            f"Die Temperature:  {td_s[-1]:5.1f} °C\n"
            f"ΔT_wg with Shunt: {dts_s[-1]:5.2f} K\n"
            f"ΔT_wg Uncooled:   {dtu_s[-1]:5.1f} K\n"
            f"Index Drift Δn:   {dn_val:.2e}"
        )

        # 4. Modular TPU Scaling
        mb_s = data["mobu_units"][:idx]
        bbi_s = data["bw_bi_tbs"][:idx]
        buni_s = data["bw_uni_tbs"][:idx]
        pw_s = data["pwr_uni_w"][:idx]
        line_bw_bi.set_data(mb_s, bbi_s)
        line_bw_uni.set_data(mb_s, buni_s)
        line_pwr_4.set_data(mb_s, pw_s)
        dot_bw_bi.set_data([mb_s[-1]], [bbi_s[-1]])
        dot_bw_uni.set_data([mb_s[-1]], [buni_s[-1]])
        dot_pwr_4.set_data([mb_s[-1]], [pw_s[-1]])
        text_p4.set_text(
            f"MOBU Units:       {mb_s[-1]:5.1f}× ({mb_s[-1]*1.6:5.1f} mm Width)\n"
            f"Bidirectional:    {bbi_s[-1]:6.1f} TB/s\n"
            f"Unidirectional:   {buni_s[-1]:6.1f} TB/s\n"
            f"Power (uni):      {pw_s[-1]:6.1f} W (@ $4.60 / Module)"
        )

        return (
            line_f_pil, line_f_cont, dot_f_pil, dot_f_cont,
            line_rep, line_p0, dot_rep, dot_p0,
            line_dt_shunt, line_dt_unc, dot_dt_shunt, dot_dt_unc,
            line_bw_bi, line_bw_uni, line_pwr_4, dot_bw_bi, dot_bw_uni, dot_pwr_4,
            text_p1, text_p2, text_p3, text_p4,
        )

    anim = animation.FuncAnimation(
        fig,
        update,
        init_func=init,
        frames=num_frames,
        interval=40,
        blit=True,
    )

    # -------------------------------------------------------------------------
    # EXPORT LOGIC: MP4 PRIMARY -> AUTOMATIC GIF FALLBACK IF FFMPEG IS MISSING
    # -------------------------------------------------------------------------
    mp4_filename = "kobc_socket_adapter_simulation.mp4"
    gif_filename = "kobc_socket_adapter_simulation.gif"
    png_filename = "kobc_socket_adapter_final_state.png"

    # Save high-resolution reference image of the final state
    update(num_frames - 1)
    fig.savefig(png_filename, dpi=180, facecolor=BG_FIG, bbox_inches="tight")
    print(f"[INFO] High-resolution final state image saved: {os.path.abspath(png_filename)}")

    try:
        print(f"[INFO] Exporting high-resolution MP4 animation to '{mp4_filename}'...")
        ffmpeg_writer = animation.FFMpegWriter(
            fps=25,
            metadata=dict(
                title="KOBC Optical Socket Adapter Simulation",
                artist="Lead Architect: Emanuel Schaaf | Open Origin Architecture",
            ),
            bitrate=3400,
        )
        anim.save(mp4_filename, writer=ffmpeg_writer, dpi=130, savefig_kwargs={"facecolor": BG_FIG})
        print(f"[SUCCESS] MP4 video successfully generated: {os.path.abspath(mp4_filename)}")
    except Exception:
        print("[NOTICE] FFmpeg unavailable – automatically switching to GIF export (PillowWriter)...")
        try:
            pillow_writer = animation.PillowWriter(fps=20)
            anim.save(gif_filename, writer=pillow_writer, dpi=110, savefig_kwargs={"facecolor": BG_FIG})
            print(f"[SUCCESS] Animated GIF successfully generated: {os.path.abspath(gif_filename)}")
        except Exception as gif_err:
            print(f"[WARNING] GIF export could not be completed either: {gif_err}")

    plt.close(fig)

    # Exact operating-point evaluation for console summary (at Δh = 200 nm, F_kin = 4.953 N, T_die = 85 °C)
    idx_200nm = np.argmin(np.abs(data["dh_nm"] - 200.0))
    idx_fkin = np.argmin(np.abs(data["F_kin_n"] - 4.953))
    idx_85c = np.argmin(np.abs(data["T_die_c"] - 85.0))

    print("=" * 78)
    print("SIMULATION COMPLETED – KOBC SOCKET OPERATING POINT METRICS:")
    print(f"  * Pad Force at 200 nm (Micro-Pillows S=5.0):  {data['F_pil_n'][idx_200nm]:.2f} N (vs. {data['F_cont_n'][idx_200nm]:.1f} N Solid Pad)")
    print(f"  * Kinematic Repeatability (4.95 N):           {data['repeatability_nm'][idx_fkin]:.1f} nm @ {data['p0_gpa'][idx_fkin]:.2f} GPa Hertz Stress")
    print(f"  * Waveguide Temp Rise at 85 °C Die Temp:      {data['dT_wg_shunt_k'][idx_85c]:.2f} K (Δn_eff = {data['dn_eff_shunt'][idx_85c]:.2e})")
    print(f"  * Maximum 4-Flank Throughput (40× MOBU):      {data['bw_bi_tbs'][-1]:.1f} TB/s bi ({data['bw_uni_tbs'][-1]:.1f} TB/s uni)")
    print("=" * 78)


# =============================================================================
# ROBUST EXECUTION WRAPPER
# =============================================================================
if __name__ == "__main__":
    try:
        run_kobc_simulation()
    except KeyboardInterrupt:
        print("\n[ABORTED] Execution terminated by user (Ctrl+C).")
    except Exception as err:
        print("\n" + "!" * 78)
        print(f"[RUNTIME ERROR] Unexpected error during execution: {err}")
        print("-" * 78)
        traceback.print_exc()
        print("!" * 78)
    finally:
        try:
            input("\nPress Enter to close the console window...")
        except EOFError:
            pass