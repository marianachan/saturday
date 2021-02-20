import os
import requests
import numpy as np
import matplotlib.pyplot as plt
from csv_process import process_csv


url = "https://gist.githubusercontent.com/tt-n-walters/1bc3cabf0580e5ae0ed91fc8554a4566/raw/139d29b50e1065419f9c14cd15f5efdae1f0c407/us_presidents.csv"
response = requests.get(url)

if not response.status_code == 200:
    exit("Failed to download.")
else:
    filename = "us_presidents.csv"
    with open(filename, "w") as file:
        file.write(response.text)
exit()
presidents = { "order": [], "name": [], "height": [] }
converters = { "order": int, "name": str, "height": int }
process_csv(filename, presidents, converters)

heights = np.array(presidents["height"])

shortest = np.min(heights)
shortest_president = presidents["name"][np.argmin(heights)]
tallest = np.max(heights)
tallest_president = presidents["name"][np.argmax(heights)]
average = np.mean(heights)

print(f"""The shortest president {shortest_president} was {shortest} cm
The tallest {tallest_president} was {tallest} cm
The average height of all presidents is {round(average, 1)} cm""")

print(heights)

# Delete the downloaded data, because why not
os.remove(filename)

plt.style.use("ggplot")
plt.hist(heights)
plt.xticks(list(set(heights)), set(heights))
plt.show()
# plt.savefig("us_president_heights.png")