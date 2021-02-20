from csv_process import process_csv


def date_process(date_string):
    date_info = date_string.split("-")
    # Map the int() function over the date_info strings
    # date_numbers = [int(date_info[0]), int(date_info[1]), int(date_info[2])]
    date_numbers = list(map(int, date_info))
    return date_numbers

# Defining the data structure to hold processed data
data = {
    "date": [],
    "max_temp": [],
    "avg_temp": [],
    "min_temp": [],
}

converters = {
    "date": date_process,
    "max_temp": int,
    "avg_temp": int,
    "min_temp": int,
}

process_csv("data.csv", data, converters)

# Process...


# a. Coldest day ever
lowest = min(data["min_temp"])
print("Lowest temp on record:", lowest)

# Find the index of the lowest value
lowest_index = data["min_temp"].index(lowest)
lowest_date = data["date"][lowest_index]
print("On date:", lowest_date)


# b. Hottest day ever
highest = max(data["max_temp"])
print("Highest temp on record:", highest)

# Find the index of the highest value
highest_index = data["max_temp"].index(highest)
highest_date = data["date"][highest_index]
print("On date:", highest_date)


# c. Average temperature for each year

# print(sum(data["avg_temp"]) / len(data["avg_temp"]))


year_averages = {}
year_maximums = {}


# This just flips the columns/rows of the data.
# Unfortunately necessary because of how filter() works and how our data was
# structured. This is one of the things that in future won't be necessary as
# tools like pandas simplify the process a lot.
ordered_data = [[data[column][i] for column in data]
    for i in range(len(data["date"]))]


for year in range(1997, 2016):
    # Predicate function to check if the data is the particular year
    def check_year(row):
        return row[0][0] == year

    # Extracting data for a particular year
    year_data = list(filter(check_year, ordered_data))

    # Equivalent of sum(), finds the total temperature over the year
    total_temp = 0
    for data in year_data:
        total_temp = total_temp + data[2]
    
    # Add the extracted data to the new year_averages dictionary
    year_averages[year] = total_temp / len(year_data)

    # Extract the max_temp values from the data and find the maximum
    year_maximums[year] = max([data[1] for data in year_data])



from matplotlib import pyplot as plt

# Bar chart of average yearly temperatures
plt.bar(year_averages.keys(), year_averages.values())
# Line showing maximum temperature per year
plt.plot(list(year_maximums.keys()), list(year_maximums.values()))
print(year_maximums)
# Set the limits of the y-axis. Just the make the plot look a little nicer
# plt.ylim(0, 30)
plt.savefig("graph.png")
