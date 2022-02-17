# Wave run-up: "old Delft formula"
def wrun_up_old(wperiod, wheight, slope):
    import numpy as np                
    import matplotlib.pyplot as plt
    dike_slope = 1 / slope
    wlength0 = 1.56 * wperiod**2
    wsteepness = wheight / wlength0
    
    wrunup_old = 8 * wheight * dike_slope
    
    print(f"\nWave run-up ('Old Delft' formula): {wrunup_old:.2f} (m)\n")
    fig, (a0, a1) = plt.subplots(1,2, figsize = (21, 5),
                                 gridspec_kw={'width_ratios': [1, 5]})
    a0.plot(wsteepness, wheight, 'h', color='gray',
               markersize=15, markerfacecolor='green',
               markeredgecolor='black', markeredgewidth=2)
    a0.set_xlim(0, 0.1)
    a0.set_ylim(0, 10)
    a0.set_xticks(np.linspace(0, 0.1, 6))
    a0.set_yticks(np.linspace(0, 10, 11))
    a0.set_xlabel('$H/L$ (-)')
    a0.set_ylabel('$H_s$ (m)')
    a0.grid()
    a1.plot(wrunup_old, wheight, 'd', color='blue',
               markersize=15, markerfacecolor='green',
               markeredgecolor='black', markeredgewidth=2)
    a1.set_xlim(0, 140)
    a1.set_ylim(0, 10)
    a1.set_xticks(np.linspace(0, 150, 31))
    a1.set_yticks(np.linspace(0, 10, 11))
    a1.set_xlabel('Wave Run-up: Old Delft Formula (m)')
    a1.set_ylabel('$H_s$ (m)')
    a1.grid()
    return

# Wave run-up: CUR-TAW
def wrun_up_curtaw(wperiod, wheight, wangle, slope, slope_roughness, berm):
    import numpy as np                
    import matplotlib.pyplot as plt
    # Library parameters
    dike_slope = 1 / slope
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
    wrunup_curtaw = 1.75 * wheight * slope_roughness * berm_factor * woblique * break_par
    # Print results
    print(f"Breaking parameter = {break_par:.2f}. \
\nWavelength = {wlength:.2f} (m).\
\nWave run-up (CUR-TAW equation) = {wrunup_curtaw:.3f} (m).\n")
    # Plot results
    fig, (a0, a1) = plt.subplots(1,2, figsize = (21, 5), 
                                 gridspec_kw={'width_ratios': [1, 5]})
    a0.plot(wsteepness, wheight, 'h', color='gray',
               markersize=15, markerfacecolor='green',
               markeredgecolor='black', markeredgewidth=2)
    a0.set_xlim(0, 0.1)
    a0.set_ylim(0, 10)
    a0.set_xticks(np.linspace(0, 0.1, 6))
    a0.set_yticks(np.linspace(0, 10, 11))
    a0.set_xlabel('$H/L$ (-)')
    a0.set_ylabel('$H_s$ (m)')
    a0.grid()
    a1.plot(wrunup_curtaw, wheight, 'd', color='blue',
            markersize=15, markerfacecolor='green',
            markeredgecolor='black', markeredgewidth=2,
            label="Wave run-up (m)")
    a1.set_xlim(0, 140)
    a1.set_ylim(0, 10)
    a1.set_xticks(np.linspace(0, 150, 31))
    a1.set_yticks(np.linspace(0, 10, 11))
    a1.set_xlabel('Wave Run-up: CUR-TAW Equation (m)')
    a1.set_ylabel('$H_s$ (m)')
    #a1.legend(loc='upper right', bbox_to_anchor=(0.90, 0.90))
    a1.grid()
    return