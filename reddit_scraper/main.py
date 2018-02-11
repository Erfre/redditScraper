"""The main file."""
from views import *
from database_manager import db_manager
from img_download import img_url_handler
from json_loader import get_reddit
from json_loader import get_settings
from sub_scrape import sub_scrape
import datetime
import calendar
import schedule
import time
import os

subreddit, db_path, img_path = get_settings()
db_m = db_manager(db_path)
reddit_account = get_reddit()

def get_posts(db):
    scraper = sub_scrape(subreddit, reddit_account)
    conn = db.create_connect()
    time_filter = db_check(db, conn, db_path)
    print("Started\n Getting top posts from {} {}...".format(time_filter, subreddit))
    img_handler = img_url_handler(subreddit, img_path)
    scraper.get_posts(time_filter, db, conn, img_handler)
    conn.close()


def db_check(db, conn, db_path):
    """ Checks if the database file exist and if it contains any
        data. If not it will start creating a db and download posts
        from all."""

    db_exist = db_path + subreddit + '.db'
    if not os.path.exists(db_exist):
        db.create_table(conn, subreddit)
        return 'all'
    else:
        rows = db.count_row(conn)
        if not rows:
            return 'all'
        else:
            return 'month'

def date_check():
    today = datetime.date.today()
    days_in_month = calendar.monthrange(today.year, today.month)[1]
    if str(today) == '1':
        get_posts(db_m)
        print('Time left till next reddit scrape: ', days_in_month - today.day)
        return
    else:
        pass


schedule.every().day.at('12:00').do(date_check)

while True:
    schedule.run_pending()
    app.run()
    time.sleep(2)
