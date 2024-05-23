import numpy as np
from parameters import *

# Function to create a coordinate system
def coordinate_system(d):
    # Define x, y, z values in astronomical units
    x_values = np.linspace(-64, 64, 64) * AU
    y_values = np.linspace(-64, 64, 64) * AU
    z_values = np.linspace(-64, 64, 64) * AU

    # Remove zero values from x, y, z arrays
    x_values = x_values[x_values != 0]
    y_values = y_values[y_values != 0]
    z_values = z_values[z_values != 0]

    # Create a 3D grid of x, y, z values
    X, Y, Z = np.meshgrid(x_values, y_values, z_values, indexing="ij")

    # Calculate R_plane and R_values
    R_plane = np.sqrt(X**2 + Y**2)
    R_values = np.sqrt(X**2 + Y**2 + Z**2)

    # Calculate r_base
    r_base = R_plane * np.abs(d) / (np.abs(d) + np.abs(z_values))

    return R_values, y_values, R_plane, z_values, r_base, X, Y, Z

# Function to calculate the angle
def calculate_angle(R_plane, z_values):
    # Calculate the slope
    m1 = z_values / R_plane
    # Calculate the angle
    delta = np.pi / 2 - np.arctan(m1)
    return delta

# Function to calculate the mass loss rate
def calculate_mass_loss_rate(r_base, M_dot_w, p, r_in, r_out, R_plane, k):
    # Initialize mass loss rate array
    mass_loss_rate = np.zeros_like(r_base)
    # Create a mask for values within the range [r_in, r_out]
    mask = (r_base >= r_in) & (r_base <= r_out)
    # If any values in the mask, calculate the mass loss rate
    if np.any(mask):
        mass_loss_rate[mask] = k * (R_plane[mask] ** p)
    return mass_loss_rate

# Function to calculate the source point
def get_source_point(R_plane, z_values, d):
    # Calculate D, the distance from the source point to any point in the space
    D = np.sqrt(R_plane**2 + (np.abs(z_values) + np.abs(d)) ** 2)
    return D

# Function to calculate the poloidal velocity
def calculate_vp(d, GM_star, lmbda, r_base):
    # Calculate the factor used in the velocity equation
    factor = 2 * lmbda - 3
    # Check if the factor is less than 0, which would cause a math error
    if factor < 0:
        raise ValueError("Invalid value of lambda causing sqrt of negative number")
    # Calculate the poloidal velocity
    vp = (np.sqrt(factor) * np.sqrt(GM_star)) / np.sqrt(r_base)
    return vp

# Function to calculate the wind density
def wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l):
    # Calculate the absolute value of the cosine of the angle
    abs_cos_delta = np.abs(np.cos(delta))
    # Calculate the wind density
    return (m_dot_wi / (vp_wi_l * abs_cos_delta)) * (np.abs(d) / (D_wi_l * abs_cos_delta)) ** 2

# Main Execution
try:
    R_values, y_values, R_plane, z_values, r_base, X, Y, Z = coordinate_system(d)
    vp_wi_l = calculate_vp(d, GM_star, lmbda, r_base)
    m_dot_wi = calculate_mass_loss_rate(r_base, M_dot_w, p, r_in, r_out, R_plane, k)
    delta = calculate_angle(R_plane, z_values)
    D_wi_l = get_source_point(R_plane, z_values, d)
    density = wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l)

    density_flattened = density.flatten()
    np.savetxt("wind_density_output.csv", density_flattened, delimiter=",", header="Density", comments="")
    print("Wind density has been computed and saved to wind_density_output.csv")
    
    vp_flat = vp_wi_l.flatten()
    np.savetxt("wind_velocity_output.csv", vp_flat, delimiter=",", header="Velocity", comments="")
    print("Wind velocity has been computed and saved to  wind_output.csv")

    temp0_array = np.full((262144,), temp0)
    np.savetxt("temp0_output.csv", temp0_array, delimiter=",", header="Temp0", comments="")
    print("Wind temperature has been computed and saved to  temp0_output.csv")
    

    print("The simulation has been successfully executed and the results have been saved.")    
except Exception as e:
    print("An error occurred during the simulation:", str(e))
