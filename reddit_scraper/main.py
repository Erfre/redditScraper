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
from _thread import start_new_thread
import schedule


reddit_account = get_reddit()

def get_posts(db, subreddit):
    img_path = 'static/images/' + subreddit + '/'
    scraper = sub_scrape(subreddit, reddit_account)
    conn, time_filter = db_check(db, db_path, subreddit)
    print("Started\n Getting top posts from {} {}...".format(time_filter, subreddit))
    img_handler = img_url_handler(subreddit, img_path)
    scraper.get_posts(time_filter, db, conn, img_handler)
    conn.commit()
    conn.close()
    print('Time for next subreddit \n\n')
    return


def db_check(db, db_path, subreddit):
    """ Checks if the database file exist and if it contains any
        data. If not it will start creating a db and download posts
        from all."""
    if not Path(db_path).is_file():
        conn = db.create_connect()
        db.create_table(conn, subreddit)
        return conn, 'all'
    else:
        conn = db.create_connect()
        db.table = subreddit
        db.create_table(conn, subreddit)
        print(db.table, subreddit)

        rows = db.count_row(conn)
        if not rows:
            return conn, 'all'
        else:
            return conn, 'month'

def date_check(db):
    today = date.today()
    days_in_month = monthrange(today.year, today.month)[1]
    if str(today.day) == '1':
        for each in subreddits:
            get_posts(db, each)
    else:
        print('Time left till next reddit scrape: ', days_in_month - today.day)
    return

def flaskThread():
        app.run(host='0.0.0.0', use_reloader=False, debug=False, threaded=True)


for each in subreddits:
    get_posts(db_m, each)
    sleep(2)

schedule.every().day.at('12:00').do(date_check, db_m)
start_new_thread(flaskThread, ())

while True:
    schedule.run_pending()
    sleep(1)
