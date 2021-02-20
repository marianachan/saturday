import numpy as np

# Most Python modules have a core feature or data structure that the module is built
# around.
# Matplotlib = Frame
# Pandas = Dataframe
# Numpy = Array

data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
a = np.array(data)

# Simple indexing
print(a[0])

# Simple slicing
print(a[0:])

# Multi-dimensional indexing
print(a[1, 1])

# Dimensional slicing
print(a[1:3, 3:])



# Functions in numpy are vectorised
# Meaning they work on more than one piece of data
print("\n\n\n\n")


import math
# Standard Python, we have to manually use the function on every bit of data
numbers = range(1, 100)
ys = []
for number in numbers:
    ys.append(math.sin(number))
    
ys = [math.sin(n) for n in numbers]


# Numpy functions will use all the data for us
array = np.array(numbers)
ys = np.sin(array)


print("\n\nArray methods\n")
numbers = np.random.randint(0, 100, 100)
print(numbers)

# minimum = np.min(numbers)
# maximum = np.max(numbers)
# average = np.mean(numbers)
minimum = (numbers).min()
maximum = (numbers).max()
average = (numbers).mean()

print("minimum:", minimum)
print("maximum:", maximum)
print("average:", average)
