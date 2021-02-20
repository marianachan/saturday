import csv
import time
import itertools

import requests
from bs4 import BeautifulSoup


number_of_years = 30
number_of_pages = 2
starting_year = 1990
results_per_page = 250
data = []

# Download 10 pages
for y, p in itertools.product(range(number_of_years), range(number_of_pages)):
    base_url = "https://www.imdb.com/search/title/?title_type=feature&release_date={}-01-01,{}-12-31&sort=num_votes,desc&start={}&count={}"
    year = 1 * y + starting_year
    page_number = results_per_page * p + 1
    url = base_url.format(year, year, page_number, results_per_page)
    print("Downloading:", url)
    
    # Specifying custom headers to sent with our request, extra information
    custom_headers = { "Accept-Language": "en-GB,en;q=0.5" }
    response = requests.get(url, headers=custom_headers)

    if not response.status_code == 200:
        print("Error downloading,", response.status_code)
        exit()
    else:
        print("Downloaded successfully.")

        # print("Our headers:", response.request.headers)
        # print()
        # print("IMDB headers:", response.headers)


    soup = BeautifulSoup(response.text, features="html.parser")
    results = soup.find_all(class_="lister-item mode-advanced")

    # Process the 50 films in the response
    for result in results:
        # Find film title
        a_tags = result.find_all("a")
        title = a_tags[1].text

        # Scores
        imdb_score = float(result.find(class_="inline-block ratings-imdb-rating")["data-value"])
        try:
            metascore = int(result.find(class_="inline-block ratings-metascore").span.text.strip())
        except AttributeError:
            metascore = -1

        # Gross/money
        nv_spans = result.find_all("span", attrs={ "name": "nv" })
        try:
            # Find number on page, and remove commas from number, and convert to int
            gross = int(nv_spans[1]["data-value"].replace(",", ""))
        except IndexError:
            # Otherwise, use -1
            gross = -1
        
        # print(f"{title} scored {imdb_score} and {metascore} and grossed ${gross}.")
        data.append([title, year, imdb_score, metascore, gross])
    
    # Pause for 1 second
    print("Delaying next download by 1 second.")
    time.sleep(1)



# Open a csv file. For symbols, set the encoding to utf8. Set newline to an empty string,
# as the csv writer adds new lines automatically.
with open("film_data.csv", "w", encoding="utf-8", newline="") as file:
    # CSV writer is an object that can formats csv data for us
    # Quoting specifies how to quote data. In this case, quote everything that isn't a number.
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)

    # Write the column names to the file, and loop through all the data and
    # write each row.
    column_names = ["title", "year", "imdb", "metascore", "gross"]
    writer.writerow(column_names)
    for row in data:
        writer.writerow(row)
