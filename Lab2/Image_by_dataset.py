import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt('DS5.txt', delimiter = " ", dtype = np.int64)

px = 1/plt.rcParams['figure.dpi'] 
plt.subplots(figsize=(960*px, 540*px))
plt.get_current_fig_manager().canvas.set_window_title("Image by dataset")
plt.scatter(points[:, 1], points[:, 0], s = 2, color = 'orange')

plt.savefig('ibd.png')

plt.show()