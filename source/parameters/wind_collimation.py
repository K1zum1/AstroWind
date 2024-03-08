# The azimuthal/rotational component ofthe wind velocity v_φ(w,z)
# is computed from the Keplerian rotational velocity at the emerging
# point of the stream line. This is equation 4 on page 4 of Kurosawa et al. (2006)

G = 6.67430e-11 
M_star = ...  # mass of the central star in kg, needs to be given


wi = ...  # this needs to be given

# Keplerian rotational velocity at the emerging point of the stream line
def v_phi_0(wi):
    return np.sqrt(G * M_star / wi)

# Azimuthal/rotational component of the wind velocity function as given by Equation (4)
def v_phi(w, z, wi):
    return v_phi_0(wi) * (wi / w)
