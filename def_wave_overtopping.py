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
    # breaking parameter
    break_par = dike_slope / np.sqrt(wsteepness)
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
    # Initial inputs
    overtopping_a = 0.067 / dike_slope
    overtopping_b = 4.3 / (break_par * berm_factor * slope_roughness * woblique * verwall_factor)
    overtopping = overtopping_a * np.exp(-1 * overtopping_b * crest_fboard / wheight) * np.sqrt(gravity * wheight**3)
    overtopping_lit = overtopping * 1000
    # Adding crest height
    new_crest_fboard = crest_fboard + add_crest_fboard
    overtopping_add = overtopping_a * np.exp(-1 * overtopping_b * new_crest_fboard / wheight) * np.sqrt(gravity * wheight**3)
    overtopping_add_lit = overtopping_add * 1000
    # Print results
    print(f"Breaking parameter = {break_par:.2f}. \
\nWavelength = {wlength:.2f} (m).\
\nWave steepness = {wsteepness:.2f}.\
\nParameter A = {overtopping_a:.2f} and parameter B = {overtopping_b:.2f}. \
\nWave overtopping discharge q = {overtopping:.3f} \
(m\N{superscript three}/s/m) = {overtopping_lit:.2f} (l/s/m).\
\nIf the dike is {add_crest_fboard} (m) higher --\u2192 \
Wave overtopping discharge q(new) = {overtopping_add:.3f} \
(m\N{superscript three}/s/m) = {overtopping_add_lit:.2f} (l/s/m).\n")
    # Plot
    fig, (a0, a1) = plt.subplots(1,2, figsize = (18, 5))
    a0.plot(overtopping, wheight, '+', color='blue',
            markersize=13, markerfacecolor='blue',
            markeredgecolor='black', markeredgewidth=3,
            label="Overtopping with initial inputs")
    a0.plot(overtopping_add, wheight, 'd', color='blue',
            markersize=13, markerfacecolor='red',
            markeredgecolor='black', markeredgewidth=1.2,
            label="Overtopping with additional inputs")
    a0.set_xlim(0, 2)
    a0.set_ylim(0, 10)
    a0.set_xticks(np.linspace(0, 2, 11))
    a0.set_yticks(np.linspace(0, 10, 11))
    a0.set_xlabel('Overtopping discharge (m3/s/m)')
    a0.set_ylabel('$H_{m0}$ (m)')
    a0.legend(loc='upper right', bbox_to_anchor=(0.90, 0.90))
    a0.grid()
    
    a1.plot(overtopping_lit, wheight, '+', color='blue',
            markersize=13, markerfacecolor='blue',
            markeredgecolor='black', markeredgewidth=3,
            label="Overtopping with initial inputs")
    a1.plot(overtopping_add_lit, wheight, 'd', color='blue',
            markersize=13, markerfacecolor='red',
            markeredgecolor='black', markeredgewidth=1.2,
            label="Overtopping with additional inputs")
    a1.set_xlim(0, 2000)
    a1.set_ylim(0, 10)
    a1.set_xticks(np.linspace(0, 2000, 11))
    a1.set_yticks(np.linspace(0, 10, 11))
    a1.set_xlabel('Overtopping discharge (liter/s/m)')
    a1.set_ylabel('$H_{m0}$ (m)')
    a1.legend(loc='upper right', bbox_to_anchor=(0.90, 0.90))
    a1.grid()
    return