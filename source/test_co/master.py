import numpy as np
from parameters import *

# Function to create a coordinate system
def xyz(d):
    limsx, limsy, limsz = 64, 64, 64
    x_values = np.linspace(-limsx, limsx, nx) * AU
    y_values = np.linspace(-limsy, limsy, ny) * AU
    z_values = np.linspace(-limsz, limsz, nz) * AU

    x_values = x_values[x_values != 0]
    y_values = y_values[y_values != 0]
    z_values = z_values[z_values != 0]

    X, Y, Z = np.meshgrid(x_values, y_values, z_values, indexing="ij")

    R_plane = np.sqrt(X**2 + Y**2)
    R_values = np.sqrt(X**2 + Y**2 + Z**2)

    r_base = R_plane * np.abs(d) / (np.abs(d) + np.abs(z_values))

    return x_values, y_values, z_values, R_values, R_plane, r_base, X, Y, Z

# Function to calculate the angle
def calculate_angle(R_plane, z_values):
    delta = (np.pi / 2) - np.arctan(z_values / R_plane)
    return delta

# Function to calculate the poloidal velocity
def calculate_vp(d, GM_star, lmbda, r_base):
    # Calculate the factor used in the velocity equation
    factor = (2 * lmbda - 3)
    # Check if the factor is less than 0, which would cause a math error
    if factor < 0:
        raise ValueError("Invalid value of lambda causing sqrt of negative number")
    # Calculate the poloidal velocity
    vp = (np.sqrt(factor) * np.sqrt(GM_star)) / np.sqrt(r_base)
    return vp

def wind_density(x_values, y_values, z_values, delta):
    abs_cos_delta = np.abs(np.cos(delta))
    vals = np.full((nx, ny, nz), 0)
    min_val = 0.73
    max_val = 0.75
    for i in range(0, nx):
        for j in range(0, ny):
                for k in range(0, nz):
                        if ((abs_cos_delta[i,j,k] <= max_val) and (abs_cos_delta[i,j,k] >= min_val)):
                                vals[i,j,k] = 1e6
    vals = vals*(2.3e-24)
    return vals

# Main Execution
try:
    # Call all the functions to calculate the wind density
    x_values, y_values, z_values, R_values, R_plane, r_base, X, Y, Z = xyz(d)
    vp_wi_l = calculate_vp(d, GM_star, lmbda, r_base)
    delta = calculate_angle(R_plane, z_values)
    density = wind_density(x_values, y_values, z_values, delta)

    # Save the results to CSV files
    density_flattened = density.flatten()
    np.savetxt("wind_density_output.csv", density_flattened, delimiter=",", header="Density", comments="")
    print("Wind density has been computed and saved to wind_density_output.csv")
    
    vp_flat = vp_wi_l.flatten()
    np.savetxt("wind_velocity_output.csv", vp_flat, delimiter=",", header="Velocity", comments="")
    print("Wind velocity has been computed and saved to  wind_output.csv")
    
    array_size = nx*ny*nz
    temp0_array = np.full((array_size,), temp0)
    np.savetxt("temp0_output.csv", temp0_array, delimiter=",", header="Temp0", comments="")
    print("Wind temperature has been computed and saved to  temp0_output.csv")
    
    print("The simulation has been successfully executed and the results have been saved.")    
except Exception as e:
    print("An error occurred during the simulation:", str(e))
