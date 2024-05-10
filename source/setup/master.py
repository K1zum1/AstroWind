import numpy as np
from parameters import *

def coordinate_system():
    d = -5 * AU
    x_values = np.linspace(-64, 64, 64) * AU
    y_values = np.linspace(-64, 64, 64) * AU
    z_values = np.linspace(-64, 64, 64) * AU

    x_values = x_values[x_values != 0]
    y_values = y_values[y_values != 0]
    z_values = z_values[z_values != 0]

    X, Y, Z = np.meshgrid(x_values, y_values, z_values, indexing="ij")
    R_plane = np.sqrt(X**2 + Y**2)
    R_values = np.sqrt(X**2 + Y**2 + Z**2)

    r_base = R_plane * np.abs(d) / (np.abs(d) + np.abs(z_values))

    return R_values, y_values, R_plane, z_values, r_base, X, Y, Z

def calculate_angle(R_plane, z_values):
    m1 = z_values / R_plane
    delta = np.pi / 2 - np.arctan(m1)
    return delta

def calculate_mass_loss_rate(r_base, M_dot_w, p, r_in, r_out, R_plane, k):
    mass_loss_rate = np.zeros_like(r_base)
    mask = (r_base >= r_in) & (r_base <= r_out)
    if np.any(mask):
        mass_loss_rate[mask] = k * (R_plane[mask] ** p)
    return mass_loss_rate

def get_source_point(R_plane, z_values, d):
    D = np.sqrt(R_plane**2 + (np.abs(z_values) + np.abs(d)) ** 2)
    return D

def calculate_vp(d, GM_star, lmbda, r_base):
    factor = 2 * lmbda - 3
    if factor < 0:
        raise ValueError("Invalid value of lambda causing sqrt of negative number")
    vp = (np.sqrt(factor) * np.sqrt(GM_star)) / np.sqrt(r_base)
    return vp

def wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l):
    abs_cos_delta = np.abs(np.cos(delta))
    return (m_dot_wi / (vp_wi_l * abs_cos_delta)) * (np.abs(d) / (D_wi_l * abs_cos_delta)) ** 2

try:
    R_values, y_values, R_plane, z_values, r_base, X, Y, Z = coordinate_system()
    vp_wi_l = calculate_vp(d, GM_star, lmbda, r_base)
    m_dot_wi = calculate_mass_loss_rate(r_base, M_dot_w, p, r_in, r_out, R_plane, k)
    delta = calculate_angle(R_plane, z_values)
    D_wi_l = get_source_point(R_plane, z_values, d)
    density = wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l)

    density_flattened = density.flatten()
    np.savetxt("wind_density_output.csv", density_flattened, delimiter=",", header="Density", comments="")
    vp_flat = vp_wi_l.flatten()
    np.savetxt("wind_output.csv", vp_flat, delimiter=",", header="Velocity", comments="")
    temp0_array = np.full((262144,), temp0)
    np.savetxt("temp0_output.csv", temp0_array, delimiter=",", header="Temp0", comments="")
    

    print("The simulation has been successfully executed and the results have been saved.")
    print("The results are saved in the following files:")
    print("1. wind_density_output.csv")
    print("2. wind_output.csv")
    print("3. temp0_output.csv")
    
except Exception as e:
    print("An error occurred during the simulation:", str(e))
