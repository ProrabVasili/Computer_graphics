import numpy as np
import matplotlib.pyplot as plt
from typing import Union

def oblique_product(p: np.array, a: np.array, b: np.array) -> Union[float, int]:
  return (a[0] - p[0])*(b[1] - p[1]) - (a[1] - p[1])*(b[0] - p[0]) 

def convex_hull(points: np.array) -> np.array:
    U, L = [], []

    for point in points:
      while (len(L) > 1 and oblique_product(point, L[-2], L[-1]) <= 0):
        L.pop()
      L += [point]

    for point in points[::-1]:
      while (len(U) > 1 and oblique_product(point, U[-2], U[-1]) <= 0):
        U.pop()
      U += [point]

    return L+U

points = np.loadtxt('DS5.txt', delimiter=" ", dtype=np.int64)[:, ::-1]

px = 1/plt.rcParams['figure.dpi'] 
plt.subplots(figsize=(960*px, 540*px))
plt.title('Convex hull', fontsize = 50)

points = points[np.lexsort((points[:, 0], points[:, 1]))]

convex_hull_dataset = np.array(convex_hull(points))   
plt.scatter(points[:, 0], points[:, 1], s=2, color='orange')
plt.plot(convex_hull_dataset[:, 0], convex_hull_dataset[:, 1], linewidth=3)
plt.savefig('ibd_ch.png')

np.savetxt('convex_hull.txt', convex_hull_dataset)

plt.show()
