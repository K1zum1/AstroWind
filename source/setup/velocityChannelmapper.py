import matplotlib.pyplot as plt
from radmc3dPy.image import readImage
import numpy as np
import os

matplotlib.use('Agg')

image_dir = './velocity_channels'
image_files = sorted(os.listdir(image_dir), key=lambda x: int(x.split('_')[1].split('.')[0]))

plt.rcParams["figure.figsize"] = (20, 10)
plots_per_row = 5
num_slices = len(image_files)
num_rows = (num_slices + plots_per_row - 1) // plots_per_row
fig, axes = plt.subplots(num_rows, plots_per_row, figsize=(20, 5 * num_rows))

for index, file_name in enumerate(image_files):
    a = readImage(os.path.join(image_dir, file_name))
    row = index // plots_per_row
    col = index % plots_per_row
    ax = axes[row, col]
    im = ax.imshow(a.image, origin='lower', cmap='hot')
    velocity = file_name.split('_')[1].split('.')[0]
    ax.set_title(f'Velocity = {velocity} km/s')
    ax.axis('off')

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax)

plt.savefig("velocity_channel_visualization.png", dpi=300)
plt.close(fig)
