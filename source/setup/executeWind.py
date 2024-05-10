
import matplotlib
from radmc3dPy.image import *
import matplotlib.pyplot as plt
from matplotlib import cm

fig1=plt.figure()
plt.ioff()

a = readImage()
result = plotImage(a, log=True, maxlog=4,fig=fig1, cmap=cm.hot, bunit='snu', dpc=140, arcsec=True)

plt.savefig('output_1.png')
plt.close()