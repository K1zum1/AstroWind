# Density Map Visualization

This Jupyter notebook contains a script for visualizing a 3D density map using matplotlib. The data is read from a CSV file and reshaped into a 3D numpy array. The script then generates a series of 2D density maps, each representing a slice of the 3D density map.

## Prerequisites

- Python
- Jupyter Notebook
- Matplotlib
- NumPy
- SciPy

## How to Run

1. Ensure that you have all the prerequisites installed.
2. Open the `density_map.ipynb` file in Jupyter Notebook.
3. Run all the cells in the notebook.

## Output

The script will display a series of 2D density maps, each representing a slice of the 3D density map. The color of each point on the map corresponds to the density at that point.

The script also includes a line to save the final figure as a PNG file. This line is currently commented out. If you wish to save the figure, uncomment this line:

```python
# plt.savefig("wind_density_visualization.png", dpi=300)
```

## Data Format
The script expects the density data to be in a CSV file named wind_density_output.csv. The data should be a single column of density values, which the script will reshape into a 3D array.

## Customization
You can customize the resolution of the grid and the number of levels in the density map by modifying the following lines:

```python
resX=1000, resY=1000  # Resolution of the grid
levels = np.logspace(np.log10(density_data.min()+1), np.log10(density_data.max()), num=50)  # Number of levels in the density map
```