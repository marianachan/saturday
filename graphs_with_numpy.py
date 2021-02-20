import math
import matplotlib.pyplot as plt
import numpy as np


x_coords = []
for i in range(400):
    x = -20 + (i / 400) * 41
    x_coords.append(x)
y_coords = []
for x in x_coords:
    y = math.sin(2 * math.sin(2 * math.sin(x)))
    y_coords.append(y)

# arange creates a range from a min to a max using a specific step
x_coords = np.arange(-20, 20, 0.05)
y_coords = np.sin(2 * np.sin(2 * np.sin(x_coords)))

plt.style.use("ggplot")
plt.plot(x_coords, y_coords)

plt.savefig("graph.png")

