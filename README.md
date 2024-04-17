This program models aspects of a stellar accretion disk winds, computing the cylindrical radius on a grid, the mass-loss rate as a function of w, and the wind's azimuthal velocity component, assuming conservation of angular momentum. The equation has been modified to assume some constant properities. Documentation of this will be written later.

**PROJECT TO BE COMPLETED BY JUNE 2024**

To run the density computation, navigate to the source directory and run

`python parameters\wind_density.py`

This will generate a 1D CSV file called `wind_density_output.csv`. 

Then use the `density_map.ipynb` to view the density. (Note: Jupyter notebook is required to use this)

Optionally use the `density_map.py` if you do not have Jupyter Notebook installed.