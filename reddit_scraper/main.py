"""The main file."""
from views import *
from database_manager import db_manager
from img_download import img_url_handler
from json_loader import get_reddit
from json_loader import get_settings
from sub_scrape import sub_scrape
from pathlib import Path
from datetime import date
from calendar import monthrange
from time import sleep
import schedule


subreddit, db_path, img_path = get_settings()
db_m = db_manager(db_path) # here the path for the data base is created
#db_m.table = subreddit
reddit_account = get_reddit()

def get_posts(db):
    scraper = sub_scrape(subreddit, reddit_account)
    conn, time_filter = db_check(db, db_path)
    print("Started\n Getting top posts from {} {}...".format(time_filter, subreddit))
    img_handler = img_url_handler(subreddit, img_path)
    scraper.get_posts(time_filter, db, conn, img_handler)
    conn.close()


def db_check(db, db_path):
    """ Checks if the database file exist and if it contains any
        data. If not it will start creating a db and download posts
        from all."""

    if not Path(db_path).is_file():
        conn = db.create_connect()
        db.create_table(conn, subreddit)
        return conn, 'all'
    else:
        conn = db.create_connect()
        rows = db.count_row(conn)
        if not rows:
            return conn, 'all'
        else:
            return conn, 'month'

def date_check():
    today = date.today()
    days_in_month = monthrange(today.year, today.month)[1]
    if str(today) == '1':
        get_posts(db_m)
        return
    else:
        print('Time left till next reddit scrape: ', days_in_month - today.day)
        return

get_posts(db_m)
schedule.every().day.at('12:00').do(date_check)
app.run()

while True:
    schedule.run_pending()
    sleep(2)
