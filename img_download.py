from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
from urllib.request import urlretrieve


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

        self.get_img_urls(url)

        if self.img_url:
            for count, img in enumerate(self.img_url):
                urlretrieve(img, full_file_path + str(count) + '.jpg')
        else:
            urlretrieve(url, full_file_path + '1.jpg')

        return full_file_path

    def get_img_urls(self, url):
        """Fetcing all the images from the link."""
        self.img_url = []
        if '/a/' or '/gallery/' in url:
            html = urlopen(url)
            soup = BeautifulSoup(html, "lxml")
            for img in soup.find_all(
                    'img', {'class': 'post-image-placeholder'}):
                self.img_url.append('https:' + img['src'])

            return self.img_url
        else:
            return
