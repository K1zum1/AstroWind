python3 master.py
python3 problem_setup.py
radmc3d mctherm setthreads 4
radmc3d image lambda 28.221 incl 90 phi 0 npix 1000
python3 executeWind.py
