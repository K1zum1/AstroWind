import numpy as np
from radmc3dPy.natconst import *

# Astronomical Constants
AU = 1.493e13  # Astronomical unit in kilometers
MS = 1.99e+33   # Solar mass in grams
RS = 6.96e10   # Solar radius in cm
MU = 2.3e-24    # Mean molecular weight in grams

# Star Parameters
GM_star = 1.334e26  # Gravitational parameter for the star

# Wind Parameters
M_dot_w = 1e17  # Wind mass loss rate
lmbda = 1.6     # Alfven lever parameter
d = -5 * AU     # Distance for wind source point calculation
p = 3.4959999999999996  # Exponent in mass loss rate calculation
temp0 = 30 # Temperature of the wind

# Radial Boundaries for Mass Loss Calculation
r_in = 5 * AU  # Inner boundary radius
r_out = 10 * AU  # Outer boundary radius
k = ((p + 2) * M_dot_w) / (2 * np.pi * (r_out**(p + 2) - r_in**(p + 2))) # Porportionality constant for mass loss rate

# Monte Carlo parameters
nphot = 1e7

# Grid parameters
nx, ny, nz = 64, 64, 64
sizex = 100 * AU
sizey = 100 * AU
sizez = 100 * AU

# Model parameters
omega = 2 * np.pi / (50 * year)
rhogas0 = 1e-16
dusttogas = 0.001
vturb0 = 1 * 1e5

# Star parameters from constants file
mstar = MS
rstar = 2 * RS  
tstar = 5500  
pstar = np.array([0., 0., 0.])

# Wavelength settings
lam1, lam2, lam3, lam4 = 0.1, 7.0, 25.0, 10000.0
n12, n23, n34 = 20, 100, 30
lam12 = np.logspace(np.log10(lam1), np.log10(lam2), n12, endpoint=False)
lam23 = np.logspace(np.log10(lam2), np.log10(lam3), n23, endpoint=False)
lam34 = np.logspace(np.log10(lam3), np.log10(lam4), n34, endpoint=True)
lam = np.concatenate([lam12, lam23, lam34])
nlam = lam.size

# Grid setup
xi = np.linspace(-sizex, sizex, nx + 1)
yi = np.linspace(-sizey, sizey, ny + 1)
zi = np.linspace(-sizez, sizez, nz + 1)
xc = 0.5 * (xi[0:nx] + xi[1:nx + 1])
yc = 0.5 * (yi[0:ny] + yi[1:ny + 1])
zc = 0.5 * (zi[0:nz] + zi[1:nz + 1])

