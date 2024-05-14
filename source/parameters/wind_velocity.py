import numpy as np
from parameters import *
from coordinate_system import *

R_values, y_values, R_plane, z_values, r_base, X, Y, Z = coordinate_system(d)


def get_source_point(R_plane, z_values, d):
    D = np.sqrt(R_plane**2 + (np.abs(z_values) + np.abs(d)) ** 2)
    return D

def calculate_vp(d, GM_star, lmbda, r_base):
    factor = 2 * lmbda - 3
    if factor < 0:
        raise ValueError("Invalid value of lambda causing sqrt of negative number")

    vp = (np.sqrt(factor) * np.sqrt(GM_star)) / np.sqrt(r_base)
    return vp


vp = calculate_vp(d, GM_star, lmbda, r_base)

output_path = "./visualize/wind_output.csv"


vp_flat = vp.flatten()
np.savetxt(output_path, vp_flat, delimiter=",", header="Velocity", comments="")
print("Wind velocity has been computed and saved to  wind_output.csv")


def format_number(number, is_decimal=False):

    if is_decimal:
        return f"{number:20.8f}"
    else:
        return f"{number:20.2e}"


shape = r_base.shape
markdown_table_path = "./dataset/check_velocity_values.md"

with open(markdown_table_path, "w") as file:
    file.write(
        "| X (AU)               | Y (AU)               | Z (AU)               | Velocity (AU)        |\n"
    )
    file.write(
        "|----------------------|----------------------|----------------------|----------------------|\n"
    )
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                x_in_au = format_number(X[i, j, k] / AU, is_decimal=True)
                y_in_au = format_number(Y[i, j, k] / AU, is_decimal=True)
                z_in_au = format_number(Z[i, j, k] / AU, is_decimal=True)
                vp_in_au = format_number(vp[i, j, k], is_decimal=False)
                file.write(f"| {x_in_au} | {y_in_au} | {z_in_au} | {vp_in_au} |\n")
