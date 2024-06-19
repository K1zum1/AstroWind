import numpy as np
from parameters import *
from coordinate_system import *

R_values, y_values, R_plane, z_values, r_base, X, Y, Z = coordinate_system(d)

def calculate_temperature(r_base, z_values):
	T = 1000*(0.1*AU/abs(r_base))*((abs(r_base)/abs(z_values))**0.5)
	return T
