import numpy as np
from parameters import *
from radmc3dPy.natconst import *

try:
    vp_data = "wind_velocity_output.csv"
    vp = np.loadtxt(vp_data, delimiter=",", skiprows=1).reshape(nx, ny, nz)
    rhogas_data = "wind_density_output.csv"
    rhogas = np.loadtxt(rhogas_data, delimiter=",", skiprows=1).reshape(nx, ny, nz)
    temp_data = "temp0_output.csv"
    temp0 = np.loadtxt(temp_data, delimiter=",", skiprows=1).reshape(nx, ny, nz)
    print("Data loading completed successfully.")
except Exception as e:
    print(f"Error loading data: {e}")

try:
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
    vturb = 6427.0 * np.sqrt(tgas)

    abunco = 1e-4
    factco = abunco/(2.3*mp)
    #nco = rhogas*factco
    nco = np.full((64, 64, 64), 100)
    print("Calculations completed successfully.")
except Exception as e:
    print(f"Error in calculations: {e}")

try:
    with open('numberdens_co.inp','w+') as f:
        f.write('1\n')                       # Format number
        f.write('%d\n'%(nx*ny*nz))           # Nr of cells
        data = nco.ravel(order='F')          # Create a 1-D view, fortran-style indexing
        data.tofile(f, sep='\n', format="%13.6e")
        f.write('\n')
    print("numberdens_co.inp written successfully.")
except Exception as e:
    print(f"Error writing numberdens_co.inp: {e}")

try:
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
    print("amr_grid.inp written successfully.")
except Exception as e:
    print(f"Error writing amr_grid.inp: {e}")

expected_entries = nx * ny * nz
actual_entries = len(rhod.ravel(order='F'))

print(f"Expected Entries: {expected_entries}, Actual Entries: {actual_entries}")

try:
    with open('dust_density.inp', 'w+') as f:
        f.write('1\n')
        f.write(f"{expected_entries}\n")
        f.write('1\n')
        for value in rhod.ravel(order='F'):
            f.write(f"{value:e}\n")
    print("dust_density.inp written successfully.")
except Exception as e:
    print(f"Error writing dust_density.inp: {e}")

try:
    with open('gas_velocity.inp','w+') as f:
        f.write('1\n')
        f.write('%d\n' % (nx * ny * nz))
        for ix in range(nx):
            for iy in range(ny):
                for iz in range(nz):
                    f.write('%13.6e %13.6e %13.6e\n' % (Vx[ix, iy, iz], Vy[ix, iy, iz], Vz[ix, iy, iz]))
    print("gas_velocity.inp written successfully.")
except Exception as e:
    print(f"Error writing gas_velocity.inp: {e}")

try:
    with open('microturbulence.inp','w+') as f:
        f.write('1\n')                       # Format number
        f.write('%d\n'%(nx*ny*nz))           # Nr of cells
        data = vturb.ravel(order='F')        # Create a 1-D view, fortran-style indexing
        data.tofile(f, sep='\n', format="%13.6e")
        f.write('\n')
    print("microturbulence.inp written successfully.")
except Exception as e:
    print(f"Error writing microturbulence.inp: {e}")

try:
    with open('gas_temperature.inp','w+') as f:
        f.write('1\n')                       # Format number
        f.write('%d\n'%(nx*ny*nz))           # Nr of cells
        data = tgas.ravel(order='F')         # Create a 1-D view, fortran-style indexing
        data.tofile(f, sep='\n', format="%13.6e")
        f.write('\n')
    print("gas_temperature.inp written successfully.")
except Exception as e:
    print(f"Error writing gas_temperature.inp: {e}")

try:
    with open('wavelength_micron.inp','w+') as f:
        f.write('%d\n'%(nlam))
        for value in lam:
            f.write('%13.6e\n'%(value))
    print("wavelength_micron.inp written successfully.")
except Exception as e:
    print(f"Error writing wavelength_micron.inp: {e}")

try:
    with open('stars.inp','w+') as f:
        f.write('2\n')
        f.write('1 %d\n\n'%(nlam))
        f.write('%13.6e %13.6e %13.6e %13.6e %13.6e\n\n'%(rstar,mstar,pstar[0],pstar[1],pstar[2]))
        for value in lam:
            f.write('%13.6e\n'%(value))
        f.write('\n%13.6e\n'%(-tstar))
    print("stars.inp written successfully.")
except Exception as e:
    print(f"Error writing stars.inp: {e}")

try:
    with open('dustopac.inp','w+') as f:
        f.write('2               Format number of this file\n')
        f.write('1               Nr of dust species\n')
        f.write('============================================================================\n')
        f.write('1               Way in which this dust species is read\n')
        f.write('0               0=Thermal grain\n')
        f.write('silicate        Extension of name of dustkappa_***.inp file\n')
        f.write('----------------------------------------------------------------------------\n')
    print("dustopac.inp written successfully.")
except Exception as e:
    print(f"Error writing dustopac.inp: {e}")

try:
    with open('lines.inp','w') as f:
        f.write('1\n')
        f.write('1\n')
        f.write('co    leiden    0    0    0\n')
    print("lines.inp written successfully.")
except Exception as e:
    print(f"Error writing lines.inp: {e}")

try:
    with open('radmc3d.inp','w+') as f:
        f.write('nphot = %d\n'%(nphot))
        f.write('scattering_mode_max = 0\n')   # Put this to 1 for isotropic scattering
        f.write('tgas_eq_tdust   = 0')
    print("radmc3d.inp written successfully.")
except Exception as e:
    print(f"Error writing radmc3d.inp: {e}")

print("All files written successfully.")
