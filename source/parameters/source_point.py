import numpy as np
from .coordinate_system import y_values


def get_source_point(y_values):
    d = -5

    D = y_values + d
    return D

D = get_source_point(y_values)
# print(D)
    