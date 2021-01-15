import requests
import os
from bs4 import BeautifulSoup

def initFBFiles():
    if not os.path.exists("Images"):
        os.mkdir("Images")


def getAllFBPhotos(url):
    URL = url

    response = requests.get(URL)

    if response.ok:
        soup = BeautifulSoup(response.text, "lxml")
        photos = soup.find_all("img", {"src":True})
        index = 1
        for data in photos:
            photo = data["src"]
            spPhoto = photo.split(".")
            exet = spPhoto[-1] if spPhoto[-1] == "png" or spPhoto[-1] == "jpg" or spPhoto[-1] == "gif" else "png"
            if not os.path.exists(spPhoto[-1]):
                photoContent = requests.get(photo)
                with open(f"Images/Photo{index}.{exet}","wb") as file:
                    file.write(photoContent.content)
            index += 1
