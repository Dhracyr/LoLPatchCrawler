import os
import webbrowser
import requests
from bs4 import BeautifulSoup


def patch_finder(patch_notes_new):
    url_id = patch_notes_new[0].split()[1].replace('.', '-')
    url = "https://www.leagueoflegends.com/en-gb/news/game-updates/patch-" + url_id + "-notes/"
    return url

def check_if_new_patch():
    file_path = os.path.join("./", "already_crawled.txt")
    # Read saved file for comparison
    patch_notes_old = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            patch_notes_old = [line.strip() for line in file.readlines()]
    else:
        open(file_path, 'w').close()  # Create the file if it does not exist

    # Crawls and writes recent patchnotes.
    url = "https://www.leagueoflegends.com/en-gb/news/tags/patch-notes/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    patch_notes_new = []
    f = open("already_crawled.txt", "w")
    for quote in soup.find_all('h2'):
        f.writelines(quote.text + "\n")
        patch_notes_new.append(quote.text)
    f.close()

    # Checks if the recent patch_notes are newer than the saved ones.
    if patch_notes_old == [] or patch_notes_old[0] == patch_notes_new[1]:
        return patch_finder(patch_notes_new)


url = check_if_new_patch()
webbrowser.open(url, new=1)