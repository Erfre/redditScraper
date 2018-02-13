# Subreddit post saver

A scraper whom goes into user specified subreddits and looks for images to download.
The image path is saved into an database together with a description.
It then uses flask to host a local webserver where the user can enter each subreddits images
randomly and choose to change the description or delete them.

## Installation

1. Clone or download.
2. Fill in the accounts.json file with reddit user and settings.
3. Fill in what subreddits to scrape and where to store the database.
3. Run setup.py in terminal.
4. Run main.py
6. Wait for flask server to start and goto the http.

### History/Goal

I made this to learn more about how databases work and how to use them.
Also because I wanted to learn more about python.

### License

MIT License

Copyright (c) [2017] [Erik]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
