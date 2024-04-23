This is the setup file for LTE3D, to be modified alongside data from [Disc-Wind-Density-Program](https://github.com/K1zum1/Disc-Wind-Density-Program/blob/main/source/parameters/wind_density_output.csv). This will be fed into RADMC3D to produce an output image.

Here is how to start the model. First make sure to have compiled radmc3d
Then enter this directory, and type

`python3 problem_setup.py`

Then in the linux shell type, for instance:

 `radmc3d image lambda 2600.757 incl 60 phi 30`

where 2600.757 is the wavelength in micron of the CO 1-0 line. Due to the
solid-body rotation of the gas an image around the line center of CO will
become a band in the image. You can also do this:

 `radmc3d image iline 1 incl 60 phi 30`

which does the same. Note that we now have only a single molecule. If
we have more, you may need to specify which molecule/atom you mean:

`radmc3d image imolspec 1 iline 1 incl 60 phi 30`

You can also make an image at a different velocity channel:

`radmc3d image iline 1 vkms 10 incl 60 phi 30`

which moves the band in the image a bit due to a 10 km/s shift
off the line center.

NOTE: If you would put vturb0=0.d0 in the problem_setup.pro, then the
      local line width becomes so small, that the image resolution 
      of 100x100 (default) will not be enough to resolve the band in 
      the image. This will lead to inaccurate total flux estimates.
      Try it out, and play with changing velocity channel. Note: in
      this case the "doppler catching" algorithm will not help, because
      the problem here lies not in the ray-tracing, but in the image
      resolution. 
