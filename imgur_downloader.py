import os
from urllib.request import urlopen
import urllib.request
import re
from bs4 import BeautifulSoup

"""this code is just some ideas I had early on in the project, probably wont
use any of these functions"""


class imgDownloader(object):
    """docstring for imgDownloader."""

    def __init__(self, link):
        super(imgDownloader, self).__init__()
        self.link = link
        self.albumUrls = []

    # should make the save place somethig different. Like a folder with TODO  also scrape the username and caption
    def downloadImage(self):
        # if album
        if self.albumUrls:
            for img in self.albumUrls:
                urllib.request.urlretrieve(img, os.path.basename(img))

    def getAlbumUrls(self):
        html = urlopen(self.link)
        soup = BeautifulSoup(html, "lxml")
        for img in soup.find_all('img', {'class': 'post-image-placeholder'}):
            print(img)
            self.albumUrls.append('https:' + img['src'])
        return self.albumUrls

    def linkId(self):
        # Must distinguish from all the different links
        # First type i.imgur   second imgur.com/a/  and just a normal picture
        if '/a/' in self.link:
            # its a album
            self.getAlbumUrls()
        elif 'i.i' in self.link:
            return self.link
        else:
            imgLink = self.link[:8] + 'i.' + self.link[8:] + '.jpg'
            self.link = imgLink
            return self.link

        self.downloadImage()
