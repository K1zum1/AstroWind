import numpy as np

def calculate_angle():
    m1 = 1.4
    delta = np.pi / 2 - np.arctan(m1)
    return delta

angle = calculate_angle()
# print(angle)