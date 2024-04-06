import numpy as np
from astro_constants import AU
from coordinate_system import coordinate_system

R_values, y_values, R_plane, z_values = coordinate_system()

def get_source_point(y_values, z_values, d=-5 * AU):
    r = np.sqrt(y_values**2 + z_values**2)
    rb = r * d / (d + z_values)
    return rb

def calculate_sound_speed(r):
    c_s = 1.7321e5 * (r / AU)**(-0.575)
    return c_s

def calculate_keplerian_velocity(r):
    v_phi = 29.9e5 / np.sqrt(r / AU)
    return v_phi

def calculate_escape_velocity(rb):
    v_esc = np.sqrt(2) * 29.9e5 / np.sqrt(rb / AU)
    return v_esc

def calculate_wind_velocity(R_values, y_values, z_values, f=0.9, beta=3):
    rb = get_source_point(y_values, z_values)
    c_s_rb = calculate_sound_speed(rb)
    v_esc_R = calculate_escape_velocity(rb)
    
    r = np.sqrt(y_values**2 + z_values**2)
    l = np.sqrt(r**2 * (1 - d / (d + z_values))**2 + z_values**2)
    
    v_p = c_s_rb + (f * v_esc_R - c_s_rb) * (l / (l + 1.5e14))**beta
    return v_p

wind_velocity = calculate_wind_velocity(R_values, y_values, z_values)
