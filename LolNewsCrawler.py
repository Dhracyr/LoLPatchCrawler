from msvcrt import getch

import requests
from bs4 import BeautifulSoup


def patch_finder(patch_notes_new):
    url_id = patch_notes_new[0][-4:].replace('.', '-')
    url = "https://www.leagueoflegends.com/de-de/news/game-updates/patch-" + url_id + "-notes/"
    return url


def check_if_new_patch():
    # Read saved file for comparison
    patch_notes_old = []
    with open("./already_crawled.txt", "r") as file:
        for line in file:
            text = line.replace('\n', '')
            patch_notes_old.append(text)

    # Crawls and writes recent patchnotes.
    url = "https://www.leagueoflegends.com/de-de/news/tags/patch-notes/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    patch_notes_new = []
    f = open("already_crawled.txt", "w")
    for quote in soup.find_all('h2'):
        f.writelines(quote.text + "\n")
        patch_notes_new.append(quote.text)
    f.close()

    # Checks if the recent patchnotes are newer than the saved ones.
    if patch_notes_old[0] == patch_notes_new[1]:
        print("We have a new Patch!")
        return patch_finder(patch_notes_new)
    else:
        print("Sadly no new patch")
        input("Press enter and exit")


url = check_if_new_patch()
print(url)


"""

"""



"""
url = "https://www.leagueoflegends.com/de-de/news/game-updates/patch-14-9-notes/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

# print(soup.prettify())

for quote in soup.find_all('blockquote'):
    print(quote.text)
"""
"""
for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    print(heading.text)

for link in soup.find_all('a'):
    print(f"Text: {link.text.strip()}, URL: {link.get('href')}")
"""
