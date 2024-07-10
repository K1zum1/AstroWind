python3 master.py
python3 problem_setup.py
radmc3d mctherm setthreads 4
radmc3d image lambda 1301.3 incl 70 phi 0 zoomau -260 260 -260 260
python3 generateimage.py
