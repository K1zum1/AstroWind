"""
This section of the code is responsible for generating an image from the RADMC-3D simulation results. 
It first imports the necessary modules. It then creates a new figure and turns off interactive mode to 
prevent the figure from being displayed immediately. It reads the image data from the RADMC-3D output using
the 'readImage' function. The image data is then plotted on the figure using the 'plotImage' function, with
the color map set to 'hot', the brightness unit set to 'snu', the distance to the object set to 140 parsecs,
and the axes in arcseconds. The image is displayed in logarithmic scale with a maximum of 4. The resulting 
image is then saved to 'output.png' and the figure is closed.
"""
import matplotlib
from radmc3dPy.image import *
import matplotlib.pyplot as plt
from matplotlib import cm

fig1=plt.figure()
plt.ioff()

a = readImage()
result = plotImage(a, log=True, maxlog=4,fig=fig1, cmap=cm.hot, bunit='snu', dpc=140, arcsec=True)

plt.savefig('output.png')
plt.close()