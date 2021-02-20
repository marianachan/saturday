import csv
import numpy as np


def create_empty(data_type, size):
    return np.zeros(shape=(size), dtype=data_type)


def process_csv(filename, data, converters, size=10):
    # "with" context manager as:
    #  1. it is safer and can avoid errors
    #  2. is generally a better idea to use than opening a file manually
    with open(filename, "r") as file:
        # csv module reader as it does a lot of processing for us automatically
        # and is a lot more efficient.
        contents = csv.reader(file)

        # next() instead of pop() when working with the csv reader rather than a list
        column_names = next(contents)

        # Loop through the data and create starting np.arrays to hold the data
        for d in data:
            data_type = data[d]
            data[d] = create_empty(data_type, size)


        # Counter to keep track of the number of rows processed
        counter = 0

        # Loop through the rows of the data
        for i, values in enumerate(contents):

            if len(values) == 0 or len(values) == 1:
                continue
            
            # Check if we have filled all empty spaces in the array, if so
            # add more empties and reset counter
            if counter == size:
                counter = 0
                # Loop through all columns in the data
                for d in data:
                    # Create new empty space for each.
                    data_type = data[d].dtype
                    new_space = create_empty(data_type, size)  # Create the new spaces
                    extended_array = np.concatenate([data[d], new_space])  # Add the new spaces to the old array
                    data[d] = extended_array

            # Loop through all column names, check if the column is present in our
            # data structure. If so, apply the converter function and save into the data.
            for name, value in zip(column_names, values):
                if name in data.keys():
                    converting_function = converters[name]

                    converted_value = converting_function(value)

                    # data[name].append(converted_value)
                    
                    data[name][i] = converted_value
            
            counter += 1




data = {
    "order": "int32",
    "name": "<U32",
    "height": "int32"
}
converters = {
    "name": str,
    "order": int,
    "height": int
}
process_csv("us_presidents.csv", data, converters)
print(data)