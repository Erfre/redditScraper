from bs4 import BeautifulSoup
import os
import urllib.request
from urllib.request import urlopen
from imgurDownloader import *


# This file will find all the links and then send them into the downloader class


def visitLink(link):
    url = link
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    return soup

def visitTop(link):
    link = link + "top/?sort=top&t=all"
    return visitLink(link)


def getImgurLinks(soup):
    imgurLink = []
    for link in soup.find_all('a', {'class': 'thumbnail invisible-when-pinned may-blank outbound'}):
        if link.get('href')[7] == 'i':
            imgurLink.append(link.get('href'))

    return imgurLink


def downloadImgurPics(listOfLinks):
    for link in listOfLinks:

        urllib.request.urlretrieve(link, os.path.basename(link))


# link = input("Link to subreddit:")
# link = 'https://www.reddit.com/r/MechanicalKeyboards/'
# print("visiting Link")
# link = visitLink(link)
# ar = getImgurLinks(link)
# downloadImgurPics(ar)
# print(ar)

o = imgDownloader('http://imgur.com/a/WexOb')
print(o.linkId())
