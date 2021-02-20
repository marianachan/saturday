import csv


filename = "../web_scraping/film_data.csv"
with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    lines = list(reader)
    lines.pop(0)


counter = 0
def linear_search(data, needle):
    global counter
    for line in data:
        counter += 2
        if needle(line) == True:
            counter += 1
            return line
        else:
            pass


data = ["c", "d", "f", "j", "k", "m", "n", "p", "r", "s", "v", "y"]
def binary_search(data, x):
    left = 0
    right = len(data)

    while (right - 1) > left:
        midpoint = left + (right - left) // 2
        print(f"{left = }, {right = }, {midpoint = }")
        item = data[midpoint]
        print(f"{item = }, {x = }")
        if item == x:
            print(f"Found at {midpoint}!")
            return midpoint
        elif item < x:
            left = midpoint
        elif item > x:
            right = midpoint

    return midpoint



result = binary_search(data, "v")
print(result)

exit()







def find_2016_81(row):
    title, year, imdb, metascore, gross = row
    if year == "2016" and imdb == "8.1":
        return True


def find_10000000(row):
    title, year, imdb, metascore, gross = row
    if 9999000 < int(gross) < 10001000:
        return True
    else:
        return False


def find_homealone(row):
    title, year, imdb, metascore, gross = row
    if title == "Home Alone":
        return True


def key_10000000(row):
    title, year, imdb, metascore, gross = row
    if 9999000 < int(gross) < 10001000:
        return True
    else:
        return False



result = linear_search(lines, find_2016_81)
print(f"Result: {result},  Took {counter} operations")
