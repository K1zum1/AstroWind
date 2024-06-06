import numpy as np

# Astronomical Constants
AU = 1.493e13  # Astronomical unit in kilometers
MS = 1.99e+33   # Solar mass in grams
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
