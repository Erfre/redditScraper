from setuptools import setup

setup(
    name='Reddit scraper',
    version='0.1',
    description='Scrape pictures from subreddits and saves them to a database(only picture path)',
    url='https://github.com/Erfre/reddit_scraper',
    license='MIT',
    install_requires=['praw', 'beautifulsoup4', 'schedule']
)