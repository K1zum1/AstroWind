#use these commands if you are on a windows machine and cannot generate the plot on the CLI.

import matplotlib
matplotlib.use('Agg')

from radmc3dPy.image import *
import matplotlib.pyplot as plt
from matplotlib import cm

a = readImage()

plotImage(a, log=True, maxlog=4, cmap=cm.hot, bunit='snu', dpc=140, arcsec=True)

plt.savefig('#.png')
plt.close()

