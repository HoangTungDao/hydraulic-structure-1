# Wave run-up: "old Delft formula"
def wrun_up_old(wperiod, wheight, dike_slope):
    import numpy as np                
    import matplotlib.pyplot as plt
    
    wlength0 = 1.56 * wperiod**2
    wsteepness = wheight / wlength0
    
    wrunup_old = 8 * wheight * dike_slope
    
    print(f"Wave run-up followed 'Old Delft' formula is {wrunup_old:.2f} (m) \n")
    
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
def wrun_up_curtaw(wperiod, wheight, dike_slope, wangle):
    import numpy as np                
    import matplotlib.pyplot as plt
    # Fix parameters
    slope_roughness = 0.7
    berm_factor = 1
    woblique = 1 - 0.0022 * wangle
    wperiod_m10 = wperiod * 0.9
    wlength = 1.56 * wperiod_m10**2
    wsteepness = wheight / wlength
    break_par = dike_slope / np.sqrt(wsteepness)
    
    wrunup_curtaw = 1.75 * wheight * slope_roughness * berm_factor * woblique * break_par
    
    print(f"Oblique wave factor is {woblique:.2f}. \
\nBreaking parameter is {break_par:.2f}. \
\nWavelength is {wlength:.2f} (m).\
\nAnd wave run-up followed CUR-TAW equation is {wrunup_curtaw:.2f} (m).\n")
    
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

# Wave Overtopping
def wave_overtopping(wperiod, wheight, dike_slope, wangle, crest_fboard, add_crest_fboard):
    import numpy as np                
    import matplotlib.pyplot as plt
    # Fix parameters
    gravity = 9.81
    slope_roughness = 1.0
    berm_factor = 1.0
    verwall_factor = 1.0
    woblique = 1 - 0.0033 * wangle
    wperiod_m10 = wperiod * 0.9
    wlength = 1.56 * wperiod_m10**2
    wsteepness = wheight / wlength
    break_par = dike_slope / np.sqrt(wsteepness)
    
    overtopping_a = 0.067 / dike_slope
    overtopping_b = 4.3 / (break_par * berm_factor * slope_roughness * woblique * verwall_factor)
    
    overtopping = overtopping_a * np.exp(-1 * overtopping_b * crest_fboard / wheight) * np.sqrt(gravity * wheight**3)
    overtopping_lit = overtopping * 1000
    new_crest_fboard = crest_fboard + add_crest_fboard
    overtopping_add = overtopping_a * np.exp(-1 * overtopping_b * new_crest_fboard / wheight) * np.sqrt(gravity * wheight**3)
    overtopping_add_lit = overtopping_add * 1000
    
    print(f"Oblique wave factor is {woblique:.2f}. \
\nBreaking parameter is {break_par:.2f}. \
\nWavelength is {wlength:.2f} (m).\
\nWave steepness is {wsteepness:.2f}.\
\nParameter A is {overtopping_a:.2f} and parameter B is {overtopping_a:.2f}.\
\nWave overtopping discharge is {overtopping:.3f} (m\N{superscript three}/s/m) or \
{overtopping_lit:.2f} (l/s/m).\
\nIf the dike is {add_crest_fboard} (m) higher, the overtopping discharge is {overtopping_add:.3f} \
(m\N{superscript three}/s/m) or {overtopping_add_lit:.2f} (l/s/m).\n")
    
    fig, (a0, a1) = plt.subplots(1,2, figsize = (18, 5))
    a0.plot(overtopping, wheight, 'd', color='blue',
            markersize=13, markerfacecolor='blue',
            markeredgecolor='black', markeredgewidth=1.2,
            label="Overtopping for initial inputs")
    a0.plot(overtopping_add, wheight, '^', color='blue',
            markersize=13, markerfacecolor='red',
            markeredgecolor='black', markeredgewidth=1.2,
            label="Overtopping for additional inputs")
    a0.set_xlim(0, 2)
    a0.set_ylim(0, 10)
    a0.set_xticks(np.linspace(0, 2, 11))
    a0.set_yticks(np.linspace(0, 10, 11))
    a0.set_xlabel('Overtopping discharge (m3/s/m)')
    a0.set_ylabel('$H_{m0}$ (m)')
    a0.legend(loc='upper right', bbox_to_anchor=(0.90, 0.90))
    a0.grid()
    
    a1.plot(overtopping_lit, wheight, 'd', color='blue',
            markersize=11, markerfacecolor='blue',
            markeredgecolor='black', markeredgewidth=1.2,
            label="Overtopping for initial inputs")
    a1.plot(overtopping_add_lit, wheight, '^', color='blue',
            markersize=11, markerfacecolor='red',
            markeredgecolor='black', markeredgewidth=1.2,
            label="Overtopping for additional inputs")
    a1.set_xlim(0, 1500)
    a1.set_ylim(0, 10)
    a1.set_xticks(np.linspace(0, 1500, 11))
    a1.set_yticks(np.linspace(0, 10, 11))
    a1.set_xlabel('Overtopping discharge (liter/s/m)')
    a1.set_ylabel('$H_{m0}$ (m)')
    a1.legend(loc='upper right', bbox_to_anchor=(0.90, 0.90))
    a1.grid()
    return
