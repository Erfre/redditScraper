from setuptools import setup

setup(
    name='Reddit scraper',
    version='0.2',
    description='Scrape pictures from subreddits and saves them to a database(only picture path)',
    url='https://github.com/Erfre/reddit_scraper',
    license='MIT',
    author='erfre',
    install_requires=['praw', 'beautifulsoup4', 'schedule', 'flask']
)