import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# region
import random
numbers = []
for i in range(100):
    numbers.append(random.random())

# list comprehension
numbers = [123 for i in range(100)]
# endregion

plt.style.use("seaborn-whitegrid")

x_values = range(10)

# Customising line styles
plt.plot(x_values, [x for x in x_values], linestyle="dashed")
plt.plot(x_values, [x + 1 for x in x_values], linestyle="dotted")
plt.plot(x_values, [x + 2 for x in x_values], linestyle="dashdot")
plt.plot(x_values, [x + 3 for x in x_values], linestyle="solid")

plt.plot(x_values, [x + 5 for x in x_values], linestyle="--")
plt.plot(x_values, [x + 6 for x in x_values], linestyle=":")
plt.plot(x_values, [x + 7 for x in x_values], linestyle="-.")
plt.plot(x_values, [x + 8 for x in x_values], linestyle="-")


# plt.axis("equal")
plt.show()

# linear_space(0, 10, 1000)
def linear_space(start, stop, points):
    delta = stop - start
    num = points - 1
    values = [start + delta * i / num for i in range(num)]
    values += [stop]
    return values


import math


x_values = linear_space(0, 10, 100)

# Customising colours
# Can be chosen by:
#   name (html colours)
#   initials
#   hexcodes
#   rgb (0, 1)
#   grayscale (0-1)
plt.plot(x_values, [math.sin(x) for x in x_values], c="rebeccapurple")
plt.plot(x_values, [math.sin(x - 1) for x in x_values], c="k")
plt.plot(x_values, [math.sin(x - 2) for x in x_values], c="#20B2AA")
plt.plot(x_values, [math.sin(x - 3) for x in x_values], c=(1, 1, 0))
plt.plot(x_values, [math.sin(x - 4) for x in x_values], c="0.5")
plt.plot(x_values, [math.sin(x - 5) for x in x_values])

plt.show()



import random

x_values = [random.random() for i in range(100)]
y_values = [random.random() for i in range(100)]
colours = [random.random() for i in range(100)]
sizes = [random.normalvariate(200, 200) for i in range(100)]


# plt.xlim(-4, 4)
# plt.ylim(-4, 4)
plt.scatter(x_values, y_values, c=colours, s=sizes, alpha=0.5, cmap="viridis")
plt.colorbar()
plt.show()

