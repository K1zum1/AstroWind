import numpy as np
from parameters import *
from coordinate_system import coordinate_system
from wind_velocity import calculate_vp, get_source_point
from mass_loss import calculate_mass_loss_rate
from angle import calculate_angle

try:
    R_values, y_values, R_plane, z_values, r_base, X, Y, Z = coordinate_system()
    vp_wi_l = calculate_vp(d, GM_star, lmbda, r_base)
    m_dot_wi = calculate_mass_loss_rate(r_base, M_dot_w, p, r_in, r_out, R_plane, k)
    delta = calculate_angle(R_plane, z_values)
    D_wi_l = get_source_point(R_plane, z_values, d)

    def wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l):
        abs_cos_delta = np.abs(np.cos(delta))
        return (m_dot_wi / (vp_wi_l * abs_cos_delta)) * (
            np.abs(d) / (D_wi_l * abs_cos_delta)
        ) ** 2

    density = wind_density(m_dot_wi, vp_wi_l, delta, d, D_wi_l)
    density_flattened = density.flatten()

    output_path_source = "./visualize/wind_density_output.csv"
    output_path_setup = "./setup/wind_density_output.csv"
    output_path_temp0 = "./setup/temp0_output.csv"

    np.savetxt(output_path_source, density_flattened, delimiter=",", header="Density", comments="")
    np.savetxt(output_path_setup, density_flattened, delimiter=",", header="Density", comments="")

    shape = density.shape
    markdown_table_path = "./dataset/check_density_values.md"

    def format_number(number, is_decimal=False):
        if is_decimal:
            return f"{number:20.8f}"
        else:
            return f"{number:20.2e}"

    with open(markdown_table_path, "w") as f:
        f.write("| X (AU)               | Y (AU)               | Z (AU)               | Density (AU^-3)      |\n")
        f.write("|----------------------|----------------------|----------------------|----------------------|\n")
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    x_in_au = format_number(X[i, j, k] / AU, is_decimal=True)
                    y_in_au = format_number(Y[i, j, k] / AU, is_decimal=True)
                    z_in_au = format_number(Z[i, j, k] / AU, is_decimal=True)
                    density_in_au3 = format_number(density[i, j, k], is_decimal=False)
                    f.write(f"| {x_in_au} | {y_in_au} | {z_in_au} | {density_in_au3} |\n")
    temp0_array = np.full((262144,), temp0)
    np.savetxt(output_path_temp0, temp0_array, delimiter=",", header="Temp0", comments="")

    print("The simulation has been successfully executed and the results have been saved.")
except Exception as e:
    print("An error occurred during the simulation:", str(e))
