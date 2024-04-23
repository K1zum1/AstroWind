#
# Import NumPy for array handling
#
import numpy as np
from radmc3dPy.natconst import *
pi  = 3.1415926535897932385e0
#
# Import plotting libraries (start Python with ipython --matplotlib)
#
#from mpl_toolkits.mplot3d import axes3d
#from matplotlib import pyplot as plt
#
# Monte Carlo parameters
#
nphot    = 1000000
#
# Grid parameters
#
nx       = 64
ny       = 64
nz       = 64
sizex    = 100*au
sizey    = 100*au
sizez    = 100*au
#
# Model parameters
#
omega    = 2*pi/(50*year)
rhogas0  = 1e-16
temp0    = 100.0
dusttogas= 0.01
vturb0   = 3.*1e5
#
# Star parameters
#
mstar    = ms
rstar    = rs
tstar    = ts
pstar    = np.array([0.,0.,0.])
#
# Write the wavelength_micron.inp file
#
lam1     = 0.1e0
lam2     = 7.0e0
lam3     = 25.e0
lam4     = 1.0e4
n12      = 20
n23      = 100
n34      = 30
lam12    = np.logspace(np.log10(lam1),np.log10(lam2),n12,endpoint=False)
lam23    = np.logspace(np.log10(lam2),np.log10(lam3),n23,endpoint=False)
lam34    = np.logspace(np.log10(lam3),np.log10(lam4),n34,endpoint=True)
lam      = np.concatenate([lam12,lam23,lam34])
nlam     = lam.size
#
# Make grid with size interpreted as half-width size here
#
xi       = np.linspace(-sizex,sizex,nx+1)
yi       = np.linspace(-sizey,sizey,ny+1)
zi       = np.linspace(-sizez,sizez,nz+1)
xc       = 0.5 * ( xi[0:nx] + xi[1:nx+1] )
yc       = 0.5 * ( yi[0:ny] + yi[1:ny+1] )
zc       = 0.5 * ( zi[0:nz] + zi[1:nz+1] )
qq       = np.meshgrid(xc,yc,zc,indexing='ij')
xx       = qq[0]
yy       = qq[1]
zz       = qq[2]

AU = 1.496e+13  
x_values = np.linspace(1, 64, 64) * AU
y_values = np.linspace(1, 64, 64) * AU
z_values = np.linspace(1, 64, 64) * AU

X, Y, Z = np.meshgrid(x_values, y_values, z_values, indexing='ij')
R_plane = np.sqrt(X**2 + Y**2)

r = R_plane  
tan_y_x = np.arctan2(Y, X)
tan_z_r = np.arctan2(Z, r)

vp_data = "wind_velocity_output.csv"
vp = np.loadtxt(vp_data, delimiter=",")
vp = vp.reshape((64, 64, 64))  

sqrt_GMstar_r = np.sqrt(GM_star / (r + 1e-10))

Vx = (sqrt_GMstar_r * np.sin(tan_y_x) +
      vp * np.cos(tan_z_r) * np.cos(tan_y_x))

Vy = (-sqrt_GMstar_r * np.cos(tan_y_x) +
      vp * np.cos(tan_z_r) * np.sin(tan_y_x))

Vz = vp * np.sin(tan_z_r)


rhogas_data = "wind_density_output.csv"
rhogas_flat = np.loadtxt(rhogas_data, delimiter=",")
rhogas = rhogas_flat.reshape(nx, ny, nz)


rhod = rhogas * dusttogas
tgas = np.zeros((nx, ny, nz)) + temp0
vturb = 792 * np.sqrt(tgas)


rhogas_data = "wind_density_output.csv"
rhogas_flat = np.loadtxt(rhogas_data, delimiter=",")
rhogas = rhogas_flat.reshape(nx, ny, nz)
rhod = rhogas * dusttogas
tgas = np.zeros((nx, ny, nz)) + temp0
vturb = 792 * np.sqrt(tgas)


#-------------MAIN MODEL SETUP DONE----------------
#-------------EMITTING SPECIES----------------
#
# Write the molecule number density file. 
#
abunco = 1e-4
factco = abunco/(2.3*mp)
nco    = rhogas*factco
with open('numberdens_co.inp','w+') as f:
    f.write('1\n')                       # Format number
    f.write('%d\n'%(nx*ny*nz))           # Nr of cells
    data = nco.ravel(order='F')          # Create a 1-D view, fortran-style indexing
    data.tofile(f, sep='\n', format="%13.6e")
    f.write('\n')
#-------------EMITTING SPECIES----------------
#
# Write the grid file
#
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
#
# Write the dust density file. Here we use a dust-to-gas ratio of 0.01
#
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
#

with open('gas_velocity.inp','w+') as f:
    f.write('1\n')
    f.write('%d\n' % (nx * ny * nz))
    for ix in range(nx):
        for iy in range(ny):
            for iz in range(nz):
                f.write('%13.6e %13.6e %13.6e\n' % (Vx[ix, iy, iz], Vy[ix, iy, iz], Vz[ix, iy, iz]))


#
# Write the microturbulence file
#
with open('microturbulence.inp','w+') as f:
    f.write('1\n')                       # Format number
    f.write('%d\n'%(nx*ny*nz))           # Nr of cells
    data = vturb.ravel(order='F')          # Create a 1-D view, fortran-style indexing
    data.tofile(f, sep='\n', format="%13.6e")
    f.write('\n')
#
# Write the gas temperature
#
with open('gas_temperature.inp','w+') as f:
    f.write('1\n')                       # Format number
    f.write('%d\n'%(nx*ny*nz))           # Nr of cells
    data = tgas.ravel(order='F')          # Create a 1-D view, fortran-style indexing
    data.tofile(f, sep='\n', format="%13.6e")
    f.write('\n')
#
# Write the wavelength file
#
with open('wavelength_micron.inp','w+') as f:
    f.write('%d\n'%(nlam))
    for value in lam:
        f.write('%13.6e\n'%(value))
#
#
# Write the stars.inp file
#
with open('stars.inp','w+') as f:
    f.write('2\n')
    f.write('1 %d\n\n'%(nlam))
    f.write('%13.6e %13.6e %13.6e %13.6e %13.6e\n\n'%(rstar,mstar,pstar[0],pstar[1],pstar[2]))
    for value in lam:
        f.write('%13.6e\n'%(value))
    f.write('\n%13.6e\n'%(-tstar))
#
# Dust opacity control file
#
with open('dustopac.inp','w+') as f:
    f.write('2               Format number of this file\n')
    f.write('1               Nr of dust species\n')
    f.write('============================================================================\n')
    f.write('1               Way in which this dust species is read\n')
    f.write('0               0=Thermal grain\n')
    f.write('silicate        Extension of name of dustkappa_***.inp file\n')
    f.write('----------------------------------------------------------------------------\n')
#
# Write the lines.inp control file
#
with open('lines.inp','w') as f:
    f.write('1\n')
    f.write('1\n')
    f.write('co    leiden    0    0\n')
#
# Write the radmc3d.inp control file
#
with open('radmc3d.inp','w+') as f:
    f.write('nphot = %d\n'%(nphot))
    f.write('scattering_mode_max = 0\n')   # Put this to 1 for isotropic scattering
    f.write('tgas_eq_tdust   = 1')
