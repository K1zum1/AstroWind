# LTE3D Setup Guide

This setup guide is designed for the LTE3D project, which uses data from the [Disc-Wind-Density-Program](https://github.com/K1zum1/Disc-Wind-Density-Program/blob/main/source/parameters/wind_density_output.csv) to generate visual outputs with RADMC3D.

## Prerequisites

Ensure the following requirements are met:
- RADMC3D compiled and ready on your system
- You are able to generate data through the DWDP program

## Installation and Execution

**To initiate the LTE3D model:**

Compile `radmc3d` if not already compiled.
Navigate to the directory containing the setup files.
Run the setup script for the model and the grid:
```python
python3 master.py
python3 problem_setup.py
```

For an image with an inclination of 80 degrees and a line velocity of 2 km/s:
```bash
radmc3d image incl 80 iline 2 vkms 7
```
For an image at 1300 microns with an inclination of 70 degrees and azimuthal angle of 30 degrees:
```bash
radmc3d image lambda 1300 incl 70 phi 30
```

Windows users can plot using Python if CLI issues arise:

```python
import matplotlib
matplotlib.use('Agg')
from radmc3dPy.image import *
import matplotlib.pyplot as plt
from matplotlib import cm
a = readImage()
plotImage(a, log=True, maxlog=4, cmap=cm.hot, bunit='snu', dpc=140, arcsec=True)
plt.savefig('output_image.png') 
plt.close()
```