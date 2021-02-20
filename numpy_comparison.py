# NUMPY is numerical python
# It is designed for very heavy and very high-level mathematical computations.


# create a list of 1,000,000 random numbers with random() function.

import random
import timeit

random_list = [] 

start_time = timeit.default_timer()
for i in range(10000000):
    random_list.append(random.random())
end_time = timeit.default_timer()
time_taken = end_time - start_time

print("Standard Random numbers time taken: " + str(time_taken) +  "s")


# create function to calculate the reciprocal of a list of numbers  (   1 / x  )
def reciprocals(numbers):
    reciprocal = []
    for number in numbers:
        rec = 1/number
        reciprocal.append(rec)
    return reciprocal



start_time = timeit.default_timer()
recs = reciprocals(random_list)
end_time = timeit.default_timer()
time_taken = end_time - start_time
print("Standard Reciprocals time taken: " + str(time_taken) +  "s")



import numpy as np


start_time = timeit.default_timer()
random_list = np.random.rand(10000000)
end_time = timeit.default_timer()
time_taken = end_time - start_time

print("Numpy Random numbers time taken: " + str(time_taken) +  "s")

start_time = timeit.default_timer()
recs = np.reciprocal(random_list)
end_time = timeit.default_timer()
time_taken = end_time - start_time
print("Numpy Reciprocals time taken: " + str(time_taken) +  "s")
