import numpy as np
from astro_constants import AU
from coordinate_system import coordinate_system
from wind_velocity import calculate_wind_velocity, get_source_point
from mass_loss import calculate_mass_loss_rate
from angle import calculate_angle

d = -5 * AU
R_values, y_values, R_plane, z_values = coordinate_system()
vp_wi_l = calculate_wind_velocity(R_values, y_values, z_values)
m_dot_wi = calculate_mass_loss_rate(R_plane)
delta = calculate_angle(R_plane, z_values)
D_wi_l = get_source_point(y_values, z_values, d)

def wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l):
    return (m_dot_wi / (vp_wi_l * np.abs(np.cos(delta)))) * (d / (D_wi_l * np.cos(delta)))**2

density = wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l)

density_flattened = density.flatten()

np.savetxt("wind_density_output.csv", density_flattened, delimiter=',', header='Density', comments='')