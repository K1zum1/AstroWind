from mass_loss import calculate_mass_loss_rate
from angle import calculate_angle
from wind_velocity import calculate_wind_velocity 
from source_point import get_source_point

import sympy as sp

m_dot_wi = sp.symbols('m_dot_wi')  # mass flux at a given radius w_i
vp_wi_l = sp.symbols('vp_wi_l')    # velocity component at w_i and l
delta = sp.symbols('delta')        # angle (radians) between the stream line and the disc normal
d = sp.symbols('d')                # distance from the source point S to a point along the stream line
D_wi_l = sp.symbols('D_wi_l')      # function D(w_i, l)




rho_wi_l = (m_dot_wi / (vp_wi_l * sp.Abs(sp.cos(delta)))) * (d / (D_wi_l * sp.cos(delta)))**2