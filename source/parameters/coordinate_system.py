import numpy as np

x_values = np.linspace(0, 64, 65)  
y_values = np.linspace(0, 64, 65)  

w_values = np.sqrt(np.add.outer(x_values**2, y_values**2))

print(w_values)
