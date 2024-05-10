import matplotlib.pyplot as plt
import numpy as np
import os
from radmc3dPy.image import readImage

def calculate_flux(image_file):
    img = readImage(image_file)
    im_nx, im_ny = img.nx, img.ny
    pixsize_x, pixsize_y = img.sizepix_x, img.sizepix_y
    dA = pixsize_x * pixsize_y

    image_data = img.image.flatten()
    total_flux = np.sum(image_data) * dA * 1e7
    return total_flux, im_nx, im_ny, image_data

def plot_images_with_flux(image_dir, output_file):
    image_files = sorted(os.listdir(image_dir), key=lambda x: int(x.split('_')[1].split('.')[0]))
    plt.rcParams["figure.figsize"] = (20, 10)
    plots_per_row = 5
    num_slices = len(image_files)
    num_rows = (num_slices + plots_per_row - 1) // plots_per_row
    fig, axes = plt.subplots(num_rows, plots_per_row, figsize=(20, 5 * num_rows))

    total_flux_sum = 0
    flux_values = []

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

    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    fig.colorbar(im, cax=cbar_ax)

    fig.text(0.5, 0.01, f'Total Flux: {total_flux_sum:.2e}', ha='center', va='center', fontsize=25, fontweight='bold')
    
    plt.savefig(output_file, dpi=300)
    plt.close(fig)

image_dir = './velocity_channels'
output_file = './velocity_channel_visualization.png'
plot_images_with_flux(image_dir, output_file)
