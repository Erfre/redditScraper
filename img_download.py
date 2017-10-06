from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from PIL import Image

class img_url_handler(object):
    """docstring for img_url_handler."""

    def __init__(self, subreddit, path):
        """Initilize."""
        super(img_url_handler, self).__init__()
        self.subreddit = subreddit
        self.path = path
        self.save_path = self.path + self.subreddit
        self.img_url = []

    def download(self, url, user):
        """Download image to path.

        Downloads all images in img_url or just the img in url.
        And saves them into path/subreddit/user/(number).jpg
        """
        full_file_path = os.path.join(self.save_path, user + '/')

        if not os.path.exists(full_file_path):
            os.makedirs(full_file_path)

        self.album_check(url)
        if is_not_gif(url):
            if self.img_url:
                for count, img in enumerate(self.img_url):
                    self.save_img(img, full_file_path, str(count))

            else:
                print(url)
                self.save_img(url, full_file_path, '0')


            return full_file_path

    def save_img(self, url, path, img_name):
        """Convert file to jpg."""
        pic = (path+img_name + '.jpg')
        urlretrieve(url, pic)

    def is_not_gif(self, url):
        """Make sure the url is not a gif"""
        if 'gif' not in url:
            return True

    def album_check(self, url):
        """Fetching all the images from the link."""
        self.img_url = []
        if '/a/' or '/gallery/' in url:
            html = urlopen(url)
            soup = BeautifulSoup(html, "lxml")
            for div_img in soup.find_all(
                    'div', {'class': 'post-image'}):
                img = div_img.find('img')       # Finds the img inside of the div
                self.img_url.append('https:' + img['src'])

            return self.img_url
        else:
            return False
