import os
from urllib.request import urlopen
import urllib.request
import re
from bs4 import BeautifulSoup

# Here is the downloader class which will contain the download id and saving of the images\


class imgDownloader(object):
    """docstring for imgDownloader."""

    def __init__(self, link):
        super(imgDownloader, self).__init__()
        self.link = link
        self.albumUrls = []

    # should make the save place somethig different. Like a folder with maybe date as name
    def downloadImage(self):
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
