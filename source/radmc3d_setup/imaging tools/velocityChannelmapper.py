import matplotlib.pyplot as plt
import numpy as np
import os
from radmc3dPy.image import readImage

"""
This function calculates the flux (luminosity) of the image. It is based on a simple 
sum of the pixel values contained in the image#.out file. The flux is calculated in erg/s/cm^2. 
"""
def calculate_flux(image_file):
    img = readImage(image_file)
    im_nx, im_ny = img.nx, img.ny
    pixsize_x, pixsize_y = img.sizepix_x, img.sizepix_y
    dA = pixsize_x * pixsize_y

    image_data = img.image.flatten()
    total_flux = np.sum(image_data) * dA * 1e7
    return total_flux, im_nx, im_ny, image_data

""" This function plots the images contained in the image#.out files and adds the flux value to the title of each image """ 

def plot_images_with_flux(image_dir, output_file):

    """
    This section of the code first retrieves and sorts the list of image files in the directory 
    based on the number in the filename. It then sets the size of the figures to be created and defines the number of 
    plots per row. After that, it calculates the total number of slices (images) and the number of rows needed 
    for the plots. Finally, it creates a grid of subplots with the calculated number of rows and columns.
    """

    image_files = sorted(os.listdir(image_dir), key=lambda x: int(x.split('_')[1].split('.')[0]))
    plt.rcParams["figure.figsize"] = (20, 10)
    plots_per_row = 5
    num_slices = len(image_files)
    num_rows = (num_slices + plots_per_row - 1) // plots_per_row
    fig, axes = plt.subplots(num_rows, plots_per_row, figsize=(20, 5 * num_rows))
    total_flux_sum = 0
    flux_values = []

    """
    This section of the code iterates over the list of image files. For each file, it calculates the flux 
    and updates the total flux sum. It also determines the row and column indices for the subplot grid based
    on the current index. If the maximum value in the image data is greater than the minimum, the data is 
    normalized; otherwise, it's set to zero. The image data is then displayed on the subplot. The velocity is 
    extracted from the file name and used to set the title of the subplot. The subplot's axes are turned off 
    for a cleaner look, and the calculated flux is displayed as text below the subplot.
    """

    for index, file_name in enumerate(image_files):
        file_path = os.path.join(image_dir, file_name)
        flux, im_nx, im_ny, image_data = calculate_flux(file_path)
        flux_values.append(flux)
        total_flux_sum += flux

        row = index // plots_per_row
        col = index % plots_per_row
        ax = axes[row, col]

        if np.max(image_data) > np.min(image_data):
            image_data = (image_data - np.min(image_data)) / (np.max(image_data) - np.min(image_data))
        else:
            image_data = np.zeros_like(image_data)

        im = ax.imshow(image_data.reshape(im_nx, im_ny), origin='lower', cmap='hot')
        velocity = file_name.split('_')[1].split('.')[0]
        ax.set_title(f'Velocity = {velocity} km/s')
        ax.axis('off')
        
        ax.text(0.5, -0.1, f'Flux: {flux:.2e}', ha='center', va='center', transform=ax.transAxes)

    """
    This section of the code first adjusts the subplot to make room for a colorbar on the right. 
    It then adds an axes to the figure for the colorbar and creates the colorbar itself. After that, 
    it adds a text to the figure displaying the total flux sum. The figure is then saved to the specified 
    output file with a resolution of 300 dpi and the figure is closed. Finally, it defines the directory 
    containing the image files and the output file path, and calls the 'plot_images_with_flux' function with these paths.
    """

    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im, cax=cbar_ax)

    fig.text(0.5, 0.01, f'Total Flux: {total_flux_sum:.2e}', ha='center', va='center', fontsize=25, fontweight='bold')
    
    plt.savefig(output_file, dpi=300)
    plt.close(fig)

image_dir = './velocity_channels'
output_file = './velocity_channel_visualization.png'
plot_images_with_flux(image_dir, output_file)

"""
Remark for the user:

The resolution of the saved figure is currently set to 300 dpi, which is a good balance between quality and file 
size. However, if you need a higher resolution image, you can increase the dpi value in the plt.savefig function.

The colorbar and the total flux text are currently positioned with fixed coordinates. If you want to 
change their positions, you can modify the values in the fig.add_axes and fig.text functions respectively.

The directory paths and the output file path are currently hardcoded. If you want to make the script more 
flexible, you can modify the script to take these paths as command line arguments.

Remember, any changes should be tested thoroughly to ensure they don't break the program.
"""