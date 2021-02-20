import html.parser
from bs4 import BeautifulSoup


html_code = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta description="profile page of someone">
        <title>Profile Page</title>
    </head>
    <body>
        <div id="main">
            <aside id="menu">
                <div class="menu-option">Home</div>
                <div class="menu-option">About</div>
                <div class="menu-option">Contact</div>
            </aside>
            <div class="profile">
                <span class="profile-name">John Smith</span>
                <img src="https://www.imageofjohnsmith.co.uk" />
                <div class="profile-description">
                    Hi! Welcome to my profile page! Isn't it great!
                </div>
            </div>
        </div>
    </body>
</html>"""


soup = BeautifulSoup(html_code, features="html.parser")


















# Direct selection
# print(soup.title.text)


# Searching
# soup.find    soup.find_all

# Searching by class
results = soup.find_all(class_="menu-option")
print(results)

# Searching by attributes
results = soup.find(attrs={ "charset": "UTF-8" })
print(results)

# Searching by function
def text_contains_excl(tag):
    if "!" in tag.text:
        return True
    else:
        return False

results = soup.find_all(text_contains_excl)
print(results)



all_tags = soup.find_all(True)
for tag in all_tags:
    if text_contains_excl(tag) == True:
        print(tag)
