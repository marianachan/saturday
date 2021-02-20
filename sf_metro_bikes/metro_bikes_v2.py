from matplotlib import pyplot as plt
import requests
import os
import datetime
from csv_process import process_csv


url = "http://drive.google.com/uc?id=13zc5_-NYEk8T9yn7eytNGqUJJpsUQs1f"

filename = "metro_bike_2019.csv"
if not os.path.exists(filename):
    print("Downloading data.")
    request = requests.get(url)

    with open(filename, "w") as file:
        file.write(request.text)

    print("Finished downloading.")

else:
    print("Using cached file.")



# Defining data structures and converting functions separately, just to keep
# our code clean and organised.

def parse_start_time(datestring):
    # Function to parse a datetime string
    #                   "2019-01-01 00:07:00"
    datestring_format = r"%Y-%m-%d %H:%M:%S"
    converted_date = datetime.datetime.strptime(datestring, datestring_format)
    return converted_date

data = {
    "duration": [],
    "start_time": [],
    "start_station": [],
    "end_station": [],
}

converters = {
    "duration": int,
    "start_time": parse_start_time,
    "start_station": int,
    "end_station": int,
}

process_csv(filename, data, converters)


print("Finished processing.")


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


plt.plot(range(1, 366), day_counts)

# Create more human-friendly labels for the x-axis
positions = [i * 31 for i in range(12)]

# positions = [0, 31, 59, 90, 121, ]
labels = ["jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]
plt.xticks(positions, labels)

# Add horizontal grid lines
plt.grid(axis="y")

plt.savefig("bikes.png")
