import requests

url = "https://gist.githubusercontent.com/tt-n-walters/837d9828dcb5aaa296a33c93d8d3af03/raw/6af7a2c82f08724e72f74e70472929c334767fa2/madrid-weather-19972015"

# Download the data from the endpoint
r = requests.get(url)

# Open a file pointer
file = open("data.csv", "w")
file.write(r.text)
file.close()
