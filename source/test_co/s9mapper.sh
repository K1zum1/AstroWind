python3 master.py
python3 problem_setup.py
radmc3d mctherm setthreads 4
radmc3d image lambda 1301.3 incl 90 phi 0 zoomau -264 264 -264 264 npix 40
python3 generateimage.py
