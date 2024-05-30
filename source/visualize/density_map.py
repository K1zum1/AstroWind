import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.interpolate import griddata

# Function to create a grid for data interpolation
def grid(x, xmin, xmax, y, ymin, ymax, z, resX=1000, resY=1000):
    # Create an evenly spaced grid of x and y values
    xi = np.linspace(xmin, xmax, resX)
    yi = np.linspace(ymin, ymax, resY)
    # Interpolate the z values onto the grid
    Z = griddata((x, y), z, (xi[None, :], yi[:, None]), method='linear')
    # Create a meshgrid of x and y values
    X, Y = np.meshgrid(xi, yi)
    return X, Y, Z

# Set the colormap to 'jet'
mpl.rc('image', cmap='jet')
# Set the size of the figures
plt.rcParams["figure.figsize"] = (15, 6)

# Load the density data from a CSV file
density_data = np.loadtxt('wind_density_output.csv', delimiter=',', skiprows=1)
# Reshape the density data to a 3D array
density_data = density_data.reshape((64, 64, 64))

# Create a grid of x and y positions
xpos = np.linspace(0, 64, 64)  
ypos = np.linspace(0, 64, 64)
xpos, ypos = np.meshgrid(xpos, ypos)

# Create a logarithmically spaced array of contour levels
levels = np.logspace(np.log10(density_data.min()+1), np.log10(density_data.max()), num=50)

# Calculate the number of rows and columns for the subplots
plots_per_row = 4
num_slices = density_data.shape[2]
num_rows = (num_slices + plots_per_row - 1) // plots_per_row

# Create a figure with multiple subplots
fig, axes = plt.subplots(num_rows, plots_per_row, figsize=(20, 5 * num_rows))

# Loop over each slice in the z direction
for z_slice_index in range(num_slices):
    # Calculate the row and column for this subplot
    row = z_slice_index // plots_per_row
    col = z_slice_index % plots_per_row
    
    # Get the density data for this slice
    density_slice = np.log10(density_data[:, :, z_slice_index] + 1)
    # Interpolate the density data onto a grid
    X, Y, Z = grid(xpos.flatten(), xpos.min(), xpos.max(), ypos.flatten(), ypos.min(), ypos.max(), density_slice.flatten())
    
    # Plot the density data
    ax = axes[row, col]
    im = ax.imshow(Z, extent=(xpos.min(), xpos.max(), ypos.min(), ypos.max()), aspect='auto', origin='lower')
    ax.set_title(f'Z = {z_slice_index}')
    ax.axis('on')  

# Adjust the position of the subplots to make room for the colorbar
fig.subplots_adjust(right=0.8)
# Add a colorbar to the figure
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax)

# Uncomment the following line to save the figure as a PNG file
# plt.savefig("wind_density_visualization.png", dpi=300)

# Display the figure
plt.show()