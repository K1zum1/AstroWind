# The local mass-loss rate per unit area (m˙ ) is assumed to be proportional 
# to the mid-plane temperature of the disc, and is a function
# of the cylindrical radius. m_dot_w is parameterized as equation 2 on page 4 of Kurosawa et al. (2006)

alpha = 0.76 # consistent with the collimated disc-wind model
q =  -1.15 # dust radiative transfer model of the innermost part of the accetion disc
p = 4*alpha * q # index of the mid-plane temperature

def calculate_mass_loss_rate():
     
    return m_dot_w**p

m_dot_wi = calculate_mass_loss_rate()

# print(m_dot_wi)