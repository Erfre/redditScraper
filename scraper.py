from bs4 import BeautifulSoup
import os
import urllib.request
from urllib.request import urlopen
from imgurDownloader import *


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

def getUser(link):
    # get the p class tag line
    soup = visitLink(link)
    for link in soup.find_all('p', {'class': 'tagline'}):
        # print (link.get('title'))
        user = link.find('a',{'class': 'author'})
        print (user.get('href'))

# link = input("Link to subreddit:")
# link = 'https://www.reddit.com/r/MechanicalKeyboards/'
# print("visiting Link")
# link = visitLink(link)
# ar = getImgurLinks(link)
# downloadImgurPics(ar)
# print(ar)
getUser('https://www.reddit.com/r/MechanicalKeyboards/')

# o = imgDownloader('http://imgur.com/a/WexOb')
# print(o.linkId())
