import numpy as np
import matplotlib.pyplot as plt

def plot_heatmap_with_wind_density(c1, c2, x_range=(0, 64), y_range=(0, 64)):
    m1 = 1.4
    m2 = 0.8
    c1 = -5
    c2 = -5
    x = np.linspace(x_range[0], x_range[1], 400)
    y = np.linspace(y_range[0], y_range[1], 400)
    X, Y = np.meshgrid(x, y)
    
   
    Y1 = m1 * X + c1
    Y2 = m2 * X + c2
    
    
    inside_boundary = (Y >= np.minimum(Y1, Y2)) & (Y <= np.maximum(Y1, Y2))
    
    
    epsilon = 1e-10  
    intensity = ...
    
    
    outside_value = 0  
    intensity_masked = np.where(inside_boundary, intensity, outside_value)

    
    plt.imshow(intensity_masked, extent=(x.min(), x.max(), y.min(), y.max()), origin='lower', cmap='coolwarm', alpha=1)
    
   
    plt.plot(x, m1*x + c1, label=f'Line 1: y = {m1}x + {c1}', color='blue')
    plt.plot(x, m2*x + c2, label=f'Line 2: y = {m2}x + {c2}', color='red')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.xlim(x_range)
    plt.ylim(y_range)
    plt.colorbar(label='Intensity based on values')
    plt.show()

plot_heatmap_with_custom_outside_color(c1, c2)