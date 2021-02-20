data = {
    "date": [[1997, 1, 1], [1997, 1, 2], [1997, 1, 3], [1997, 1, 4], [1997, 1, 5]],
    "max_temp": [7, 7, 5, 7, 2],
    "avg_temp": [4, 3, 3, 3, 0],
    "min_temp": [2, 0, 2, -1, -1]
}


# https://repl.it/@NicoWalters/PyDS190920


data.transponse()

ordered_data = [[data[column][i] for column in data]
    for i in range(len(data["date"]))]



ordered_data = []
for i in range(len(data["date"])):
    new_row = []
    for column in data:
        new_row.append(data[column][i])
    ordered_data.append(new_row)



for row in ordered_data:
    print(row[0][0])


exit()


year_averages = {}
year_maximums = {}
for year in range(1997, 2016):
    print(year)
    # Predicate function to check if the data is the particular year
    def check_year(row):
        return row[0][0] == year

    # Extracting data for a particular year
    year_data = list(filter(check_year, ordered_data))




def filter(list_of_values):
    final_results = []
    for value in list_of_values:
        if value[0][0] == year:
            final_results.append(value)
    return final_results