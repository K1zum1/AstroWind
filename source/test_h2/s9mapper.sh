python3 master.py
python3 problem_setup.py
radmc3d mctherm setthreads 10
radmc3d image lambda 4.6947 incl 90 phi 0 sizeau 200
python3 executeWind.py
