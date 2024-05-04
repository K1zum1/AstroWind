python3 master.py
python3 problem_setup.py

radmc3d image iline 6 incl 80 vkms $1

import matplotlib
from radmc3dPy.image import *
import matplotlib.pyplot as plt
from matplotlib import cm
matplotlib.use('Agg')
a = readImage()
plotImage(a, log=True, maxlog=4, cmap.cm.hot, bunit='snu', dpc=140, arcsec=True)
plt.savefig('output_image.png')
plt.close()