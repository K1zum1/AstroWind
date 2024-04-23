# Stellar Accretion Disk Winds Model

This program simulates aspects of stellar accretion disk winds. It computes the cylindrical radius on a grid, the mass-loss rate as a function of w, and the azimuthal velocity component of the wind, assuming conservation of angular momentum. The model assumes some properties are constant. Detailed documentation will be provided later.

**Important:** This project is to be completed by June 2024.

## Prerequisites

- Python
- Jupyter Notebook (for `density_map.ipynb`)

## Setup and Execution

Follow these steps to compute and view the density map:

1. **Density Computation**:
   - Navigate to the source directory.
   - Run the following command to generate the `wind_density_output.csv` file:
     ```bash
     python parameters\wind_density.py
     ```

2. **Viewing the Density Map**:
   - If you have Jupyter Notebook installed, open `density_map.ipynb`.
   - Alternatively, run `density_map.py` if you do not have Jupyter Notebook:
     ```bash
     python density_map.py
     ```

## Expected Output

Upon successful execution with correctly defined parameters, you should observe a cone-like structure radiating outwards in the density map. If this is not the case, please double-check your parameters to ensure they align with the expected measurements.

![Density Map Output](example.png)
