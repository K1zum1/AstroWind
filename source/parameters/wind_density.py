from mass_loss import calculate_mass_loss_rate
from angle import calculate_angle
from wind_velocity import calculate_wind_velocity



m_dot_wi = calculate_mass_loss_rate()
vp_wi_l = calculate_wind_velocity()
delta = calculate_angle()
d = -5
D_wi_l = get_source_point()

def wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l):
    rho_wi_l = (m_dot_wi / (vp_wi_l * sp.Abs(sp.cos(delta)))) * (d / (D_wi_l * sp.cos(delta)))**2
    return rho_wi_l

wind_density = wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l)