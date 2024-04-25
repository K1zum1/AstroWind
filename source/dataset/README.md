After running 

```bash
python parameters\wind_density.py
 ```
you will have access to the following CSV files to assist with data verification:

`check_density_values.csv`

`check_velocity_values.csv`

These files contain XYZ coordinates and corresponding values for density or velocity, scaled by astronomical units (AU). You will be able to manually check these values or adjust the parameters to match specific requirements.

Example Output
Below is an example of what the output will look like in the CSV files:

| X (AU) | Y (AU) | Z (AU) | Velocity (AU)         |
|--------|--------|--------|-----------------------|
| 1.0    | 1.0    | 1.0    | 1.1785113019775793    |
| 1.0    | 1.0    | 2.0    | 1.0101525445522108    |
| 1.0    | 1.0    | 3.0    | 0.8838834764831844    |
| 1.0    | 1.0    | 4.0    | 0.7856742013183862    |

or 

| X (AU) | Y (AU) | Z (AU) | Density (AU^-3)          |
|--------|--------|--------|--------------------------|
| 48.0   | 27.0   | 23.0   | 2.8094299437322665e-29   |
| 48.0   | 27.0   | 24.0   | 2.4414621767034716e-29   |
| 48.0   | 27.0   | 25.0   | 2.1346317751941638e-29   |
| 48.0   | 27.0   | 26.0   | 1.876887822493793e-29    |


