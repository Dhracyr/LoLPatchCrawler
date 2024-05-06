import webbrowser
import requests
from bs4 import BeautifulSoup


def patch_finder(patch_notes_new):
    url_id = patch_notes_new[0].split()[1].replace('.', '-')
    url = "https://www.leagueoflegends.com/en-gb/news/game-updates/patch-" + url_id + "-notes/"
    return url


def check_if_new_patch():
    # Read saved file for comparison
    patch_notes_old = []
    with open("./save_data/already_crawled.txt", "r") as file:
        for line in file:
            text = line.replace('\n', '')
            patch_notes_old.append(text)

    # Crawls and writes recent patchnotes.
    url = "https://www.leagueoflegends.com/en-gb/news/tags/patch-notes/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    patch_notes_new = []
    f = open("/save_data/already_crawled.txt", "w")
    for quote in soup.find_all('h2'):
        f.writelines(quote.text + "\n")
        patch_notes_new.append(quote.text)
    f.close()

    # Checks if the recent patch_notes are newer than the saved ones.
    if patch_notes_old[0] == patch_notes_new[1]:
        print("We have a new Patch!")
        return patch_finder(patch_notes_new)
    else:
        print("Sadly no new patch")
        input("Press enter and exit")



url = check_if_new_patch()
webbrowser.open(url, new=1)
