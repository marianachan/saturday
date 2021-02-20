import requests
import os
import datetime


url = "http://drive.google.com/uc?id=13zc5_-NYEk8T9yn7eytNGqUJJpsUQs1f"

filename = "metro_bike_2019.csv"
if not os.path.exists(filename):
    print("Downloading data.")
    request = requests.get(url)
    
    file = open(filename, "w")
    file.write(request.text)
    file.close()
    print("Finished downloading.")

else:
    print("Using cached file.")


# Read and split up the file.

file = open(filename, mode="r")
contents = file.read()
file.close()

lines = contents.splitlines()
print(type(lines))
print(len(lines))



# duration 1, start_time 2, start_station 4, end_station 7

data = {
    "duration": [],
    "start_time": [],
    "start_station": [],
    "end_station": [],
}

lines.pop(0)
for line in lines:
    values = line.split(",")

    if len(values) == 0 or len(values) == 1:
        continue

    # Function to parse a datetime string
    #                   "2019-01-01 00:07:00"
    datestring_format = r"%Y-%m-%d %H:%M:%S"
    datestring = values[2].strip("\"")
    converted_date = datetime.datetime.strptime(datestring, datestring_format)
    
    data["duration"].append(int(values[1]))
    data["start_time"].append(converted_date)
    data["start_station"].append(int(values[4]))
    data["end_station"].append(int(values[7]))
    


print(next(zip(*data.values())))

# What was the longest journey.

longest = max(data["duration"])
hours = longest/60
print(f"{hours} hrs time record")

# Finding the index of the longest journey

longest_index = data["duration"].index(longest)
longest_date = data["start_time"][longest_index]


print(longest_date.strftime("The longest duration journey was on %d of %B"))



# Plot the number of journeys for each day.
# "2019-01-01 00:07:00"

# cardinal numbers from 1
# ordinal numbers from 0

day_numbers = []

for day in data["start_time"]:
    day_number = int(day.strftime("%j"))
    day_numbers.append(day_number)

day_counts = []
for i in range(1, 366):
    day_counts.append(day_numbers.count(i))

print("Journeys on the 1st of Jan:", day_counts[0])
print("Journeys on the 27th of April:", day_counts[116])


import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

plt.plot( range(1, 366) , day_counts)

# Create more human-friendly labels for the x-axis
positions = [i * 31 for i in range(12)]

# positions = [0, 31, 59, 90, 121, ]
labels = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
plt.xticks(positions, labels)

# Add horizontal grid lines
plt.grid(axis="y")

plt.savefig("bikes.png")



# 20201024121433
# 5.2 seconds to completion
# 232MB maximum memory usage
