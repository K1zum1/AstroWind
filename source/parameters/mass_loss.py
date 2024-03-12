from coordinate_system import coordinate_system


R_values, _ = coordinate_system()

def calculate_mass_loss_rate(R_values):
    alpha = 0.76 # consistent with the collimated disc-wind model
    q =  -1.15 # dust radiative transfer model of the innermost part of the accetion disc
    p = 4*alpha * q # index of the mid-plane temperature 

    return (R_values)**p

m_dot_wi = calculate_mass_loss_rate(R_values)

#print(m_dot_wi)