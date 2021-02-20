import requests


session_token = "53616c7465645f5f9770f2a6d442b078b2c39b3568295edd649637e2ad5dd3faaf129e87590a51941376aaae55ab5243"


def download(day_number):
    url = "https://adventofcode.com/2020/day/{}/input".format(day_number)
    cookies = {
        "session": session_token
    }
    print("Downloading day {} from {}".format(day_number, url))
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.text
    else:
        print("Download error. {}\n{}".format(response.status_code, response.text))
        exit()


if __name__ == "__main__":
    import sys
    day_number = sys.argv[1]
    inputs = download(day_number)
    filename = "day{}inputs".format(day_number)
    with open(filename, "w") as file:
        file.write(inputs)
