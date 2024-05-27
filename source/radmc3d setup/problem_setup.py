import numpy as np
from parameters import *
from radmc3dPy.natconst import *

"""
This section of the code is responsible for loading the data from the output CSV files of the simulation. 
It loads the wind velocity, wind density, and temperature data from their respective CSV files. The data 
is loaded using the numpy function 'loadtxt', with the delimiter set to comma and skipping the first row. 
The loaded data is then reshaped to match the dimensions of the simulation grid (nx, ny, nz).
"""

vp_data = "wind_velocity_output.csv"
vp = np.loadtxt(vp_data, delimiter=",", skiprows=1).reshape(nx, ny, nz)
rhogas_data = "wind_density_output.csv"
rhogas = np.loadtxt(rhogas_data, delimiter=",", skiprows=1).reshape(nx, ny, nz)
temp_data = "temp0_output.csv"
temp0 = np.loadtxt(temp_data, delimiter=",", skiprows=1).reshape(nx, ny, nz)

"""
This section of the code performs several calculations related to the simulation. It first calculates the 
radial distance in the plane, the tangential angles, and the square root of the gravitational constant times 
the mass of the star divided by the radial distance. It then calculates the components of the velocity vector 
using these values. After that, it calculates the dust density, gas temperature, and turbulent velocity. Finally, 
it calculates the number density of the emitting molecule by multiplying the gas density by the abundance of the 
molecule divided by the mean molecular weight. This part has also been modified from the original Dullemond calculations
in order to fit the ideal equations provided by Dr. Uma Gorti. Please review the provided LaTeX document for more information.
"""
X, Y, Z = np.meshgrid(xc, yc, zc)
R_plane = np.sqrt(X**2 + Y**2)
r = R_plane
tan_y_x = np.arctan2(Y, X)
tan_z_r = np.arctan2(Z, r)
sqrt_GMstar_r = np.sqrt(GM_star / (r + 1e-10))


Vx = (sqrt_GMstar_r * np.sin(tan_y_x) + vp * np.cos(tan_z_r) * np.cos(tan_y_x))
Vy = (-sqrt_GMstar_r * np.cos(tan_y_x) + vp * np.cos(tan_z_r) * np.sin(tan_y_x))
Vz = vp * np.sin(tan_z_r)


rhod = rhogas * dusttogas
tgas = temp0
vturb = 792 * np.sqrt(tgas)  

abunco = 1e-4
factco = abunco/(2.3*mp)
nco = rhogas*factco

"""
This section of the code writes the simulation data to various input files for the RADMC-3D radiative transfer code. 
It writes the number density of CO, the grid structure, the dust density, the gas velocity field, the microturbulence,
the gas temperature, the wavelength grid, the stellar parameters, the dust opacity control file, the molecular line data,
and the main control file. The data is written in the format required by RADMC-3D. Altering this section of the code will
cause radiative transfer simulation to malfunction. Please refer to the RADMC-3D documentation for more information.
"""

with open('numberdens_co.inp','w+') as f:
    f.write('1\n')                       # Format number
    f.write('%d\n'%(nx*ny*nz))           # Nr of cells
    data = nco.ravel(order='F')          # Create a 1-D view, fortran-style indexing
    data.tofile(f, sep='\n', format="%13.6e")
    f.write('\n')

# Write the grid file
with open('amr_grid.inp','w+') as f:
    f.write('1\n')                       # iformat
    f.write('0\n')                       # AMR grid style  (0=regular grid, no AMR)
    f.write('0\n')                       # Coordinate system
    f.write('0\n')                       # gridinfo
    f.write('1 1 1\n')                   # Include x,y,z coordinate
    f.write('%d %d %d\n'%(nx,ny,nz))     # Size of grid
    for value in xi:
        f.write('%13.6e\n'%(value))      # X coordinates (cell walls)
    for value in yi:
        f.write('%13.6e\n'%(value))      # Y coordinates (cell walls)
    for value in zi:
        f.write('%13.6e\n'%(value))      # Z coordinates (cell walls)

# Write the dust density file. Here we use a dust-to-gas ratio of 0.01
expected_entries = nx * ny * nz
actual_entries = len(rhod.ravel(order='F'))

print(f"Expected Entries: {expected_entries}, Actual Entries: {actual_entries}")

with open('dust_density.inp', 'w+') as f:
    f.write('1\n')
    f.write(f"{expected_entries}\n")
    f.write('1\n')
    for value in rhod.ravel(order='F'):
        f.write(f"{value:e}\n")

# Write the gas velocity field
with open('gas_velocity.inp','w+') as f:
    f.write('1\n')
    f.write('%d\n' % (nx * ny * nz))
    for ix in range(nx):
        for iy in range(ny):
            for iz in range(nz):
                f.write('%13.6e %13.6e %13.6e\n' % (Vx[ix, iy, iz], Vy[ix, iy, iz], Vz[ix, iy, iz]))

# Write the microturbulence file
with open('microturbulence.inp','w+') as f:
    f.write('1\n')                       # Format number
    f.write('%d\n'%(nx*ny*nz))           # Nr of cells
    data = vturb.ravel(order='F')        # Create a 1-D view, fortran-style indexing
    data.tofile(f, sep='\n', format="%13.6e")
    f.write('\n')

# Write the gas temperature
with open('gas_temperature.inp','w+') as f:
    f.write('1\n')                       # Format number
    f.write('%d\n'%(nx*ny*nz))           # Nr of cells
    data = tgas.ravel(order='F')         # Create a 1-D view, fortran-style indexing
    data.tofile(f, sep='\n', format="%13.6e")
    f.write('\n')

# Write the wavelength file
with open('wavelength_micron.inp','w+') as f:
    f.write('%d\n'%(nlam))
    for value in lam:
        f.write('%13.6e\n'%(value))

# Write the stars.inp file
with open('stars.inp','w+') as f:
    f.write('2\n')
    f.write('1 %d\n\n'%(nlam))
    f.write('%13.6e %13.6e %13.6e %13.6e %13.6e\n\n'%(rstar,mstar,pstar[0],pstar[1],pstar[2]))
    for value in lam:
        f.write('%13.6e\n'%(value))
    f.write('\n%13.6e\n'%(-tstar))

# Dust opacity control file
with open('dustopac.inp','w+') as f:
    f.write('2               Format number of this file\n')
    f.write('1               Nr of dust species\n')
    f.write('============================================================================\n')
    f.write('1               Way in which this dust species is read\n')
    f.write('0               0=Thermal grain\n')
    f.write('silicate        Extension of name of dustkappa_***.inp file\n')
    f.write('----------------------------------------------------------------------------\n')

# Write the lines.inp control file
with open('lines.inp','w') as f:
    f.write('1\n')
    f.write('1\n')
    f.write('co    leiden    0    0\n')

# Write the radmc3d.inp control file
with open('radmc3d.inp','w+') as f:
    f.write('nphot = %d\n'%(nphot))
    f.write('scattering_mode_max = 0\n')   # Put this to 1 for isotropic scattering
    f.write('tgas_eq_tdust   = 1')

"""
Remark:

This problem setup is modular to fit RADMC3D strict input requirements. However, there are a few areas that could be improved:
I am currently working on a more flexible version of this code that will allow for more user input and customization.

1. The file paths are hardcoded, which might cause issues if the file structure changes. 
Consider using a more flexible way to handle file paths, such as using a configuration file or command line arguments.

2. The script currently writes output files directly to the disk. This could be problematic if there is not enough disk space
 or if the user does not have write permissions. Consider adding error handling to check for these issues before writing files.

3. The script does not have any logging or progress reporting. This could make it difficult to troubleshoot issues or 
understand what the script is doing. Consider adding logging or print statements to report progress and any issues that occur.

Remember, any changes should be tested thoroughly to ensure they don't break the program.
"""