#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
PROJECT: Optical a-Si:H Waveguide Inlay Bridge (TPU-9 Interconnect Concept)
MODULE:  Thermomechanical Shear, Optical Attenuation & Throughput Simulation
Lead Architect: Emanuel Schaaf
Framework:      Open Origin Architecture
===============================================================================
Description:
Complete headless animation script for coupled calculation and progressive
visualization of:
1. Thermomechanical interfacial shear stress via the Suhir shear-lag model
2. Optical attenuation and transmission profile along the 5.0 mm bridge span
3. Bandwidth and power scaling across the active bridge width (0-15 mm / MOBU)
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
    import scipy.special as sp
except ImportError as exc:
    print(f"[ERROR] Failed to load SciPy: {exc}")
    print("Please install scipy via: pip install scipy")
    input("Press Enter to exit...")
    sys.exit(1)


# =============================================================================
# FIRST-PRINCIPLES PHYSICAL AND ARCHITECTURAL MODEL COMPUTATION
# =============================================================================
def compute_simulation_data(num_points=500):
    """
    Computes all physical field quantities of the 5.0 mm optical waveguide
    bridge based on exact first-principles equations.
    """
    # -------------------------------------------------------------------------
    # A. Thermomechanics (Suhir Shear-Lag Model)
    # -------------------------------------------------------------------------
    L_bridge_m = 5.0e-3               # Total bridge span length: 5.0 mm
    half_L_m = L_bridge_m / 2.0       # Half span length: 2.5 mm
    delta_T = 60.0                    # Thermal excursion: 60 K (25 °C -> 85 °C)
    alpha_sub = 16.0e-6               # CTE of organic ABF substrate (1/K)
    alpha_wg = 2.6e-6                 # CTE of a-Si:H / SiO2 waveguide stack (1/K)
    delta_alpha = alpha_sub - alpha_wg
    eps_th = delta_alpha * delta_T    # Differential thermal strain: 8.04e-4

    E_biax_wg = 80.0e9                # Biaxial modulus of waveguide stack (Pa)
    t_wg = 3.0e-6                     # Waveguide stack thickness: 3.0 µm
    S_wg = E_biax_wg * t_wg           # Axial membrane stiffness: 2.4e5 N/m

    # Case 1: Compliant Siloxane Elastomer Shear-Buffer (Corrected Design)
    G_buf = 50.0e6                    # Buffer shear modulus: 50 MPa
    h_buf = 20.0e-6                   # Buffer thickness: 20 µm
    k_buf = np.sqrt(G_buf / (h_buf * S_wg))

    # Case 2: Rigid Direct Bonding without Elastomer Buffer (Baseline Reference)
    G_rig = 2000.0e6                  # Rigid epoxy shear modulus: 2000 MPa
    h_rig = 2.0e-6                    # Bondline thickness: 2 µm
    k_rig = np.sqrt(G_rig / (h_rig * S_wg))

    # Spatial coordinate x from -2.5 mm to +2.5 mm
    x_m = np.linspace(-half_L_m, half_L_m, num_points)
    x_mm = x_m * 1e3

    # Interfacial shear stress profile tau(x) in MPa (signed and magnitude)
    # Evaluated via sinh(k*x)/cosh(k*L/2) in numerically stable exponential form
    def shear_stress_mpa(x_arr, G_val, h_val, k_val):
        prefactor = (G_val / (h_val * k_val)) * eps_th * 1e-6  # in MPa
        # Numerically stable formulation for large k*L/2:
        # sinh(k*x)/cosh(k*L/2) = sign(x) * (exp(-k*(L/2 - |x|)) - exp(-k*(L/2 + |x|))) / (1 + exp(-k*L))
        abs_x = np.abs(x_arr)
        num = np.exp(-k_val * (half_L_m - abs_x)) - np.exp(-k_val * (half_L_m + abs_x))
        den = 1.0 + np.exp(-2.0 * k_val * half_L_m)
        return prefactor * np.sign(x_arr) * (num / den)

    tau_buf_mpa = shear_stress_mpa(x_m, G_buf, h_buf, k_buf)
    tau_rig_mpa = shear_stress_mpa(x_m, G_rig, h_rig, k_rig)

    # -------------------------------------------------------------------------
    # B. Optical Loss Budget along z in [0, 5.0 mm]
    # -------------------------------------------------------------------------
    z_mm = np.linspace(0.0, 5.0, num_points)

    # 1. Input and output evanescent coupling (Adiabatic nanotaper + index pad)
    # Modeled as sharp error-function transitions at z = 0.08 mm and z = 4.92 mm
    coupling_in_db = 0.65 * 0.5 * (1.0 + sp.erf((z_mm - 0.08) / 0.04))
    coupling_out_db = 0.65 * 0.5 * (1.0 + sp.erf((z_mm - 4.92) / 0.04))

    # 2. Linear propagation in hydrogenated amorphous silicon (1.8 dB/cm = 0.18 dB/mm)
    prop_asi_db = 0.18 * z_mm

    # 3. Two adaptive S-bend compensation zones at z = 1.5 mm and z = 3.5 mm (0.08 dB each)
    sbend_1_db = 0.08 * 0.5 * (1.0 + sp.erf((z_mm - 1.50) / 0.12))
    sbend_2_db = 0.08 * 0.5 * (1.0 + sp.erf((z_mm - 3.50) / 0.12))

    # 4. Distributed system margin across the span (0.50 dB total = 0.10 dB/mm)
    margin_db = 0.10 * z_mm

    # Cumulative total insertion loss of the corrected a-Si:H bridge
    loss_asi_db = (
        coupling_in_db
        + prop_asi_db
        + sbend_1_db
        + sbend_2_db
        + margin_db
        + coupling_out_db
    )
    trans_asi_pct = (10.0 ** (-loss_asi_db / 10.0)) * 100.0

    # Comparison curve: Uncorrected ELA polysilicon (20 dB/cm = 2.0 dB/mm + air gap)
    loss_poly_db = (
        3.50 * 0.5 * (1.0 + sp.erf((z_mm - 0.08) / 0.04))
        + 2.00 * z_mm
        + sbend_1_db * 4.0
        + sbend_2_db * 4.0
        + 3.50 * 0.5 * (1.0 + sp.erf((z_mm - 4.92) / 0.04))
    )
    trans_poly_pct = (10.0 ** (-loss_poly_db / 10.0)) * 100.0

    # -------------------------------------------------------------------------
    # C. Data Throughput & Power Consumption across Active Width W [0, 15 mm]
    # -------------------------------------------------------------------------
    w_mm = np.linspace(0.0, 15.0, num_points)
    # 200 waveguides/mm total -> 100 TX + 100 RX per mm at 5 µm pitch
    # Per waveguide: 8 DWDM channels * 64 Gbit/s = 512 Gbit/s = 0.064 TB/s
    throughput_uni_tbs = w_mm * 100.0 * 0.064        # 6.4 TB/s per mm (unidirectional)
    throughput_bi_tbs = throughput_uni_tbs * 2.0     # 12.8 TB/s per mm (bidirectional)

    # Electrical power per direction at 0.461 pJ/bit
    # 1 TB/s = 8e12 bit/s -> Power = TB/s * 8e12 * 0.461e-12 W = TB/s * 3.688 W
    power_uni_watts = throughput_uni_tbs * 8.0 * 0.461

    return {
        "x_mm": x_mm,
        "tau_buf_mpa": tau_buf_mpa,
        "tau_rig_mpa": tau_rig_mpa,
        "z_mm": z_mm,
        "loss_asi_db": loss_asi_db,
        "trans_asi_pct": trans_asi_pct,
        "loss_poly_db": loss_poly_db,
        "trans_poly_pct": trans_poly_pct,
        "w_mm": w_mm,
        "throughput_uni_tbs": throughput_uni_tbs,
        "throughput_bi_tbs": throughput_bi_tbs,
        "power_uni_watts": power_uni_watts,
    }


# =============================================================================
# MAIN VISUALIZATION AND ANIMATION ENGINE
# =============================================================================
def run_simulation():
    """
    Creates the dark-mode dashboard, progressively animates all trajectories
    over time, and exports the result as MP4 (Fallback: GIF) + PNG.
    """
    print("=" * 75)
    print("STARTING SIMULATION: Optical a-Si:H Bridge (Open Origin Architecture)")
    print("Lead Architect: Emanuel Schaaf")
    print("=" * 75)

    data = compute_simulation_data(num_points=500)
    num_pts = len(data["x_mm"])
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

    fig = plt.figure(figsize=(16, 9.5), dpi=130, facecolor=BG_FIG)
    gs = GridSpec(2, 2, figure=fig, height_ratios=[1.0, 1.05], hspace=0.34, wspace=0.24)

    ax_shear = fig.add_subplot(gs[0, 0], facecolor=BG_AX)
    ax_opt = fig.add_subplot(gs[0, 1], facecolor=BG_AX)
    ax_thru = fig.add_subplot(gs[1, :], facecolor=BG_AX)
    ax_power = ax_thru.twinx()

    # Global Dashboard Header
    fig.suptitle(
        "OPTICAL a-Si:H WAVEGUIDE BRIDGE (L = 5.0 mm) – SYSTEM SIMULATION\n"
        "Lead Architect: Emanuel Schaaf | Open Origin Architecture",
        fontsize=14,
        fontweight="bold",
        color=COL_CYAN,
        y=0.97,
    )

    # -------------------------------------------------------------------------
    # PANEL 1: Thermomechanical Interfacial Shear Stress (Suhir Model)
    # -------------------------------------------------------------------------
    ax_shear.set_title(
        "1. Thermomechanical Shear Stress τ(x) at ΔT = 60 K",
        color=TEXT_COL,
        fontsize=11,
        fontweight="bold",
        pad=10,
    )
    ax_shear.set_xlabel("Bridge Coordinate x from Center of Symmetry [mm]", color=TEXT_COL)
    ax_shear.set_ylabel("Interfacial Shear Stress |τ(x)| [MPa]", color=TEXT_COL)
    ax_shear.set_xlim(-2.5, 2.5)
    ax_shear.set_ylim(0.0, 14.0)
    ax_shear.grid(True, color=GRID_COL, linestyle="--", linewidth=0.7, alpha=0.8)

    # Static reference line: Critical adhesion / delamination threshold
    ax_shear.axhline(
        10.0,
        color=COL_YELLOW,
        linestyle=":",
        linewidth=1.5,
        label="Critical Delamination Threshold (10.0 MPa)",
    )

    (line_tau_rig,) = ax_shear.plot(
        [], [], color=COL_MAGENTA, linewidth=2.2, linestyle="--",
        label="Rigid Direct Bond (τ_max = 12.46 MPa)"
    )
    (line_tau_buf,) = ax_shear.plot(
        [], [], color=COL_CYAN, linewidth=2.6,
        label="20 µm Elastomer Buffer (τ_max = 0.623 MPa)"
    )
    (dot_tau_buf,) = ax_shear.plot([], [], "o", color=COL_CYAN, markersize=7)
    (dot_tau_rig,) = ax_shear.plot([], [], "o", color=COL_MAGENTA, markersize=7)

    text_shear_info = ax_shear.text(
        0.03, 0.78, "", transform=ax_shear.transAxes,
        color=TEXT_COL, fontsize=9,
        bbox=dict(boxstyle="round,pad=0.4", facecolor=BG_FIG, edgecolor=GRID_COL)
    )
    ax_shear.legend(loc="upper right", fontsize=8.5, facecolor=BG_FIG, edgecolor=GRID_COL)

    # -------------------------------------------------------------------------
    # PANEL 2: Optical Attenuation and Transmission Budget
    # -------------------------------------------------------------------------
    ax_opt.set_title(
        "2. Optical Loss Budget & Transmission along z [0 – 5.0 mm]",
        color=TEXT_COL,
        fontsize=11,
        fontweight="bold",
        pad=10,
    )
    ax_opt.set_xlabel("Optical Propagation Path along Printed Bridge z [mm]", color=TEXT_COL)
    ax_opt.set_ylabel("Cumulative Insertion Loss α(z) [dB]", color=TEXT_COL)
    ax_opt.set_xlim(0.0, 5.0)
    ax_opt.set_ylim(0.0, 6.0)
    ax_opt.grid(True, color=GRID_COL, linestyle="--", linewidth=0.7, alpha=0.8)

    # Mark adaptive S-bend compensation positions
    ax_opt.axvline(1.5, color=GRID_COL, linestyle="-.", linewidth=1.0)
    ax_opt.axvline(3.5, color=GRID_COL, linestyle="-.", linewidth=1.0)
    ax_opt.text(1.53, 5.3, "S-Bend 1\n(1.5 mm)", color=TEXT_COL, fontsize=7.5)
    ax_opt.text(3.53, 5.3, "S-Bend 2\n(3.5 mm)", color=TEXT_COL, fontsize=7.5)

    # Receiver sensitivity link budget limit
    ax_opt.axhline(
        4.5, color=COL_YELLOW, linestyle=":", linewidth=1.5,
        label="Max. Allowable Bridge Loss Budget (4.50 dB)"
    )

    (line_loss_poly,) = ax_opt.plot(
        [], [], color=COL_MAGENTA, linewidth=2.0, linestyle="--",
        label="Uncorrected ELA Polysilicon (>17 dB)"
    )
    (line_loss_asi,) = ax_opt.plot(
        [], [], color=COL_CYAN, linewidth=2.6,
        label="Corrected a-Si:H Bridge (2.86 dB @ 5 mm)"
    )
    (dot_loss_asi,) = ax_opt.plot([], [], "o", color=COL_CYAN, markersize=7)

    text_opt_info = ax_opt.text(
        0.03, 0.72, "", transform=ax_opt.transAxes,
        color=TEXT_COL, fontsize=9,
        bbox=dict(boxstyle="round,pad=0.4", facecolor=BG_FIG, edgecolor=GRID_COL)
    )
    ax_opt.legend(loc="lower right", fontsize=8.5, facecolor=BG_FIG, edgecolor=GRID_COL)

    # -------------------------------------------------------------------------
    # PANEL 3: Data Throughput (TB/s) & Electrical Power (W)
    # -------------------------------------------------------------------------
    ax_thru.set_title(
        "3. Data Throughput & Power Scaling across Active Bridge Width W (8× DWDM @ 64 Gbit/s, 5 µm Pitch)",
        color=TEXT_COL,
        fontsize=11,
        fontweight="bold",
        pad=10,
    )
    ax_thru.set_xlabel("Active Width of Printed Optical Bridge Inlay W [mm]", color=TEXT_COL)
    ax_thru.set_ylabel("Data Throughput [TB/s]", color=COL_CYAN)
    ax_power.set_ylabel("Electrical Power per Direction [W] (@ 0.461 pJ/bit)", color=COL_YELLOW)

    ax_thru.set_xlim(0.0, 15.0)
    ax_thru.set_ylim(0.0, 210.0)
    ax_power.set_ylim(0.0, 400.0)
    ax_thru.grid(True, color=GRID_COL, linestyle="--", linewidth=0.7, alpha=0.8)

    # Reference line: Total TPU 8i HBM Bandwidth (8.6 TB/s)
    ax_thru.axhline(
        8.601, color=COL_YELLOW, linestyle=":", linewidth=1.4,
        label="Reference: Total TPU 8i HBM Bandwidth (8.6 TB/s)"
    )

    # Highlight the 3 modular scaling tiers (1.6 mm / 8.0 mm / 15.0 mm)
    for w_mark, label_txt in [
        (1.6, "Compact Inlay / 1× MOBU (1.6 mm)\n10.24 TB/s uni | 20.48 TB/s bi"),
        (8.0, "Medium Inlay / 5× MOBU (8.0 mm)\n51.20 TB/s uni | 102.4 TB/s bi"),
        (15.0, "Full-Flank Inlay / KOBC-15mm (15.0 mm)\n96.0 TB/s uni | 192.0 TB/s bi"),
    ]:
        ax_thru.axvline(w_mark, color=GRID_COL, linestyle="-.", linewidth=1.0)
        ax_thru.text(
            w_mark - 0.15 if w_mark == 15.0 else w_mark + 0.15,
            175.0 if w_mark != 8.0 else 145.0,
            label_txt,
            color=TEXT_COL,
            fontsize=8,
            ha="right" if w_mark == 15.0 else "left",
            bbox=dict(boxstyle="round,pad=0.25", facecolor=BG_FIG, edgecolor=GRID_COL, alpha=0.85),
        )

    (line_thru_bi,) = ax_thru.plot(
        [], [], color=COL_CYAN, linewidth=2.8,
        label="Total Bidirectional Throughput [TB/s]"
    )
    (line_thru_uni,) = ax_thru.plot(
        [], [], color=COL_MAGENTA, linewidth=2.3,
        label="Unidirectional Throughput [TB/s]"
    )
    (line_pwr_uni,) = ax_power.plot(
        [], [], color=COL_YELLOW, linewidth=2.0, linestyle="--",
        label="Electrical Power per Direction [W]"
    )

    (dot_thru_bi,) = ax_thru.plot([], [], "o", color=COL_CYAN, markersize=7)
    (dot_thru_uni,) = ax_thru.plot([], [], "o", color=COL_MAGENTA, markersize=7)
    (dot_pwr_uni,) = ax_power.plot([], [], "s", color=COL_YELLOW, markersize=6)

    text_thru_info = ax_thru.text(
        0.02, 0.56, "", transform=ax_thru.transAxes,
        color=TEXT_COL, fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.45", facecolor=BG_FIG, edgecolor=GRID_COL)
    )

    # Combined legend for Panel 3
    lines_3 = [line_thru_bi, line_thru_uni, line_pwr_uni]
    labels_3 = [l.get_label() for l in lines_3]
    ax_thru.legend(lines_3, labels_3, loc="upper left", fontsize=8.5, facecolor=BG_FIG, edgecolor=GRID_COL)

    # Style axis ticks and spines
    for ax in [ax_shear, ax_opt, ax_thru, ax_power]:
        ax.tick_params(colors=TEXT_COL)
        for spine in ax.spines.values():
            spine.set_color(GRID_COL)

    # -------------------------------------------------------------------------
    # ANIMATION UPDATE FUNCTION
    # -------------------------------------------------------------------------
    def init():
        line_tau_rig.set_data([], [])
        line_tau_buf.set_data([], [])
        dot_tau_buf.set_data([], [])
        dot_tau_rig.set_data([], [])
        line_loss_poly.set_data([], [])
        line_loss_asi.set_data([], [])
        dot_loss_asi.set_data([], [])
        line_thru_bi.set_data([], [])
        line_thru_uni.set_data([], [])
        line_pwr_uni.set_data([], [])
        dot_thru_bi.set_data([], [])
        dot_thru_uni.set_data([], [])
        dot_pwr_uni.set_data([], [])
        text_shear_info.set_text("")
        text_opt_info.set_text("")
        text_thru_info.set_text("")
        return (
            line_tau_rig, line_tau_buf, dot_tau_buf, dot_tau_rig,
            line_loss_poly, line_loss_asi, dot_loss_asi,
            line_thru_bi, line_thru_uni, line_pwr_uni,
            dot_thru_bi, dot_thru_uni, dot_pwr_uni,
            text_shear_info, text_opt_info, text_thru_info,
        )

    def update(frame):
        # Hold the final 15 frames steady at the end state for readability
        active_frames = num_frames - 15
        progress = min(1.0, (frame + 1) / float(active_frames))
        idx = max(1, int(progress * num_pts))

        # 1. Interfacial shear stress (plot magnitude |tau(x)|)
        x_sub = data["x_mm"][:idx]
        tau_b_sub = np.abs(data["tau_buf_mpa"][:idx])
        tau_r_sub = np.abs(data["tau_rig_mpa"][:idx])

        line_tau_buf.set_data(x_sub, tau_b_sub)
        line_tau_rig.set_data(x_sub, tau_r_sub)
        dot_tau_buf.set_data([x_sub[-1]], [tau_b_sub[-1]])
        dot_tau_rig.set_data([x_sub[-1]], [tau_r_sub[-1]])

        text_shear_info.set_text(
            f"Position x: {x_sub[-1]:+5.2f} mm\n"
            f"|τ| Elastomer Buffer: {tau_b_sub[-1]:5.3f} MPa\n"
            f"|τ| Rigid Bonding:    {tau_r_sub[-1]:5.2f} MPa"
        )

        # 2. Optical attenuation & transmission
        z_sub = data["z_mm"][:idx]
        l_asi_sub = data["loss_asi_db"][:idx]
        l_poly_sub = data["loss_poly_db"][:idx]
        t_asi_val = data["trans_asi_pct"][idx - 1]

        line_loss_asi.set_data(z_sub, l_asi_sub)
        line_loss_poly.set_data(z_sub, l_poly_sub)
        dot_loss_asi.set_data([z_sub[-1]], [l_asi_sub[-1]])

        text_opt_info.set_text(
            f"Optical Path z:    {z_sub[-1]:4.2f} mm\n"
            f"a-Si:H Loss:       {l_asi_sub[-1]:4.2f} dB\n"
            f"Transmission T:    {t_asi_val:4.1f} %\n"
            f"Energy Efficiency: 0.461 pJ/bit"
        )

        # 3. Data throughput & electrical power
        w_sub = data["w_mm"][:idx]
        t_bi_sub = data["throughput_bi_tbs"][:idx]
        t_uni_sub = data["throughput_uni_tbs"][:idx]
        p_uni_sub = data["power_uni_watts"][:idx]

        line_thru_bi.set_data(w_sub, t_bi_sub)
        line_thru_uni.set_data(w_sub, t_uni_sub)
        line_pwr_uni.set_data(w_sub, p_uni_sub)

        dot_thru_bi.set_data([w_sub[-1]], [t_bi_sub[-1]])
        dot_thru_uni.set_data([w_sub[-1]], [t_uni_sub[-1]])
        dot_pwr_uni.set_data([w_sub[-1]], [p_uni_sub[-1]])

        wg_count = int(w_sub[-1] * 200)
        text_thru_info.set_text(
            f"Active Bridge Width W: {w_sub[-1]:5.2f} mm ({wg_count} Waveguides)\n"
            f"Unidirectional:        {t_uni_sub[-1]:6.2f} TB/s\n"
            f"Bidirectional:         {t_bi_sub[-1]:6.2f} TB/s\n"
            f"Electrical Power:      {p_uni_sub[-1]:6.1f} W (per direction)"
        )

        return (
            line_tau_rig, line_tau_buf, dot_tau_buf, dot_tau_rig,
            line_loss_poly, line_loss_asi, dot_loss_asi,
            line_thru_bi, line_thru_uni, line_pwr_uni,
            dot_thru_bi, dot_thru_uni, dot_pwr_uni,
            text_shear_info, text_opt_info, text_thru_info,
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
    mp4_filename = "optische_siliziumbruecke_simulation.mp4"
    gif_filename = "optische_siliziumbruecke_simulation.gif"
    png_filename = "optische_siliziumbruecke_final_state.png"

    # Save high-resolution static reference image of the final state
    update(num_frames - 1)
    fig.savefig(png_filename, dpi=180, facecolor=BG_FIG, bbox_inches="tight")
    print(f"[INFO] High-resolution final state image saved: {os.path.abspath(png_filename)}")

    exported_file = None
    try:
        print(f"[INFO] Exporting high-resolution MP4 animation to '{mp4_filename}'...")
        ffmpeg_writer = animation.FFMpegWriter(
            fps=25,
            metadata=dict(
                title="Optical a-Si:H Waveguide Bridge Simulation",
                artist="Lead Architect: Emanuel Schaaf | Open Origin Architecture",
            ),
            bitrate=3200,
        )
        anim.save(mp4_filename, writer=ffmpeg_writer, dpi=130, savefig_kwargs={"facecolor": BG_FIG})
        exported_file = os.path.abspath(mp4_filename)
        print(f"[SUCCESS] MP4 video successfully generated: {exported_file}")
    except Exception:
        # Silent, crash-safe fallback to PillowWriter (GIF)
        print("[NOTICE] FFmpeg unavailable – automatically switching to GIF export (PillowWriter)...")
        try:
            pillow_writer = animation.PillowWriter(fps=20)
            anim.save(gif_filename, writer=pillow_writer, dpi=110, savefig_kwargs={"facecolor": BG_FIG})
            exported_file = os.path.abspath(gif_filename)
            print(f"[SUCCESS] Animated GIF successfully generated: {exported_file}")
        except Exception as gif_err:
            print(f"[WARNING] GIF export could not be completed either: {gif_err}")

    plt.close(fig)
    print("=" * 75)
    print("SIMULATION COMPLETED – SUMMARY OF OPERATING METRICS:")
    print(f"  * Max. Shear Stress (20 µm Buffer):  {np.max(np.abs(data['tau_buf_mpa'])):.3f} MPa (vs. 12.46 MPa rigid)")
    print(f"  * Total Optical Loss (5.0 mm Span):  {data['loss_asi_db'][-1]:.2f} dB ({data['trans_asi_pct'][-1]:.1f} % Transmission)")
    print(f"  * Throughput at 1.6 mm Width:        10.24 TB/s uni | 20.48 TB/s bi @ 37.8 W")
    print(f"  * Throughput at 15.0 mm Width:       96.00 TB/s uni | 192.00 TB/s bi @ 354.0 W")
    print("=" * 75)


# =============================================================================
# ROBUST EXECUTION WRAPPER
# =============================================================================
if __name__ == "__main__":
    try:
        run_simulation()
    except KeyboardInterrupt:
        print("\n[ABORTED] Execution terminated by user (Ctrl+C).")
    except Exception as err:
        print("\n" + "!" * 75)
        print(f"[RUNTIME ERROR] Unexpected error during execution: {err}")
        print("-" * 75)
        traceback.print_exc()
        print("!" * 75)
    finally:
        try:
            input("\nPress Enter to close the console window...")
        except EOFError:
            pass