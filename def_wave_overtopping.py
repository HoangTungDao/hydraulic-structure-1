# Wave Overtopping
def wave_overtopping(wperiod, wheight, wangle, slope, slope_roughness, 
                     crest_fboard, add_crest_fboard, berm, verwall):
    import numpy as np                
    import matplotlib.pyplot as plt
    # Fix parameters
    dike_slope = 1 / slope
    gravity = 9.81
    # wave period and steepness
    wperiod_m10 = wperiod * 0.9
    wlength = 1.56 * wperiod_m10**2
    wsteepness = wheight / wlength
    # Iribarren number
    iribarren = dike_slope / np.sqrt(wsteepness)
    # Slope roughness
    if slope_roughness == 1.0:
        print("Slope material: asphalt, concrete with a smooth surface.")
    elif slope_roughness == 0.9:
        print("Slope material: concrete blocks, block mats.")
    elif slope_roughness == 0.7:
        print("Slope material: gravel, gabions.")
    elif slope_roughness == 0.6:
        print("Slope material: quarry stone (rip-rap).")
    elif slope_roughness == 0.5:
        print("Slope material: cubes (random positioning).")
    else:
        print("Slope material: X-blocs, tetrapods, dolosses.")
    # Berm factor
    if berm == 0:
        berm_factor = 1
        print(f"Dike has no berm --\u2192 Berm fator = {berm_factor:.2f}")
    else:
        berm_factor = 0.7
        print(f"Dike has a berm --\u2192 Berm fator = {berm_factor:.2f} \
(but it needs to accurately calculate)")
    # Vertical Wall
    if verwall == 0:
        verwall_factor = 1.0
        print(f"Dike has no vertical wall --\u2192 Vertical wall fator = {verwall_factor:.2f}")
    else:
        verwall_factor = 1.35 - 0.0078 * 90
        print(f"Dike has a vertical wall --\u2192 Vertical wall fator = {verwall_factor:.2f}")
    # Wave angle factor
    if wangle <= 80 and wangle >= 0:
        woblique = 1 - 0.0022 * wangle
        print(f"Wave direction = {wangle:.2f}\N{superscript zero} --\u2192 \
Oblique wave factor = {woblique:.4f}.")
    else:
        woblique = 0.0824
        print(f"Wave direction = {wangle:.2f}\N{superscript zero} --\u2192 \
Oblique wave factor = {woblique:.4f}.")

    # Calculations
    # Fixed calculations
    overtopping_a = np.sqrt(gravity * wheight ** 3)
    overtopping_b = 0.023 * iribarren * berm_factor / (np.sqrt(dike_slope))
    overtopping_d = iribarren * wheight * berm_factor * slope_roughness * woblique * verwall_factor
    # Before adding crest height    
    overtopping_cmean = 2.5 * crest_fboard
    overtopping_cmax = 1.35 * crest_fboard
    overtopping_dmean = overtopping_cmean / overtopping_d
    overtopping_dmax = overtopping_cmax / overtopping_d
    # After adding crest height
    new_crest_fboard = crest_fboard + add_crest_fboard
    overtopping_newcmean = 2.5 * new_crest_fboard
    overtopping_newcmax = 1.35 * new_crest_fboard
    overtopping_newdmean = overtopping_newcmean / overtopping_d
    overtopping_newdmax = overtopping_newcmax / overtopping_d    
    # Discharge
    overtopping = overtopping_a * overtopping_b * np.exp(-1 * overtopping_dmean ** 1.3)
    overtopping_max = overtopping_a * 0.1035 * np.exp(-1 * overtopping_dmax ** 1.3)
    overtopping_lit = overtopping * 1000
    overtopping_litmax = overtopping_max * 1000
    overtopping_new = overtopping_a * overtopping_b * np.exp(-1 * overtopping_newdmean ** 1.3)
    overtopping_newmax = overtopping_a * 0.1035 * np.exp(-1 * overtopping_newdmax ** 1.3)
    overtopping_litnew = overtopping_new * 1000
    overtopping_litnewmax = overtopping_newmax * 1000
    # Print results
    print(f"Iribarren number = {iribarren:.2f}. \
\nWavelength = {wlength:.2f} (m).\
\nWave steepness = {wsteepness:.2f}.\
\nWave overtopping discharge q = {overtopping:.3f} \
(m\N{superscript three}/s/m) = {overtopping_lit:.2f} (l/s/m);\
\nwith the maximum discharge = {overtopping_max:.3f}\
(m\N{superscript three}/s/m) = {overtopping_litmax:.2f} (l/s/m).\
\nIf the dike is {add_crest_fboard} (m) higher \
\n--\u2192 \
Wave overtopping discharge q(new) = {overtopping_new:.3f} \
(m\N{superscript three}/s/m) = {overtopping_litnew:.2f} (l/s/m);\
\nwith the maximum discharge = {overtopping_newmax:.3f}\
(m\N{superscript three}/s/m) = {overtopping_litnewmax:.2f} (l/s/m).")
    # Plot
    fig, (a0, a1) = plt.subplots(1,2, figsize = (18, 5))
    a0.plot(overtopping, wheight, 'o', color='blue',
            markersize=11, markerfacecolor='blue',
            markeredgecolor='black', markeredgewidth=3,
            label="Overtopping with initial inputs")
    a0.plot(overtopping_max, wheight, 'o', color='red',
            markersize=11, markerfacecolor='red',
            markeredgecolor='black', markeredgewidth=3,
            label="Max Overtopping with additional crest height")
    a0.plot(overtopping_new, wheight, 'd', color='blue',
            markersize=13, markerfacecolor='blue',
            markeredgecolor='black', markeredgewidth=1.2,
            label="Overtopping with additional inputs")
    a0.plot(overtopping_newmax, wheight, 'd', color='red',
            markersize=13, markerfacecolor='red',
            markeredgecolor='black', markeredgewidth=1.2,
            label="Max Overtopping with additional crest height")
    a0.set_xlim(0, 2)
    a0.set_ylim(0, 10)
    a0.set_xticks(np.linspace(0, 2, 11))
    a0.set_yticks(np.linspace(0, 10, 11))
    a0.set_xlabel('Overtopping discharge (m\N{superscript three}/s/m)')
    a0.set_ylabel('$H_{m0}$ (m)')
    a0.legend(loc='upper right', bbox_to_anchor=(0.90, 0.90))
    a0.grid()
    
    a1.plot(overtopping_lit, wheight, 'o', color='blue',
            markersize=11, markerfacecolor='blue',
            markeredgecolor='black', markeredgewidth=3,
            label="Overtopping with initial inputs")
    a1.plot(overtopping_litmax, wheight, 'o', color='red',
            markersize=11, markerfacecolor='red',
            markeredgecolor='black', markeredgewidth=3,
            label="Max Overtopping with additional crest height")    
    a1.plot(overtopping_litnew, wheight, 'd', color='blue',
            markersize=13, markerfacecolor='blue',
            markeredgecolor='black', markeredgewidth=1.2,
            label="Overtopping with additional inputs")
    a1.plot(overtopping_litnewmax, wheight, 'd', color='red',
            markersize=13, markerfacecolor='red',
            markeredgecolor='black', markeredgewidth=1.2,
            label="Max Overtopping with additional crest height")    
    a1.set_xlim(0, 2000)
    a1.set_ylim(0, 10)
    a1.set_xticks(np.linspace(0, 2000, 11))
    a1.set_yticks(np.linspace(0, 10, 11))
    a1.set_xlabel('Overtopping discharge (liter/s/m)')
    a1.set_ylabel('$H_{m0}$ (m)')
    a1.legend(loc='upper right', bbox_to_anchor=(0.90, 0.90))
    a1.grid()
    return