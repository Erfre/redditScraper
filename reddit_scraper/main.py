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

def first_run(time_filter):
    get_posts(time_filter)


def get_posts(time_filter):
    reddit_account = get_reddit()
    subreddit, db_dir, img_path = get_settings()
    print("Started\n Getting top posts from {} {}...".format(time_filter, subreddit))
    scraper = sub_scrape(subreddit, reddit_account)
    db = db_manager(db_dir)
    conn = db.create_connect()
    db.create_table(conn, subreddit) #Table name is the name of the subreddit
    img_handler = img_url_handler(subreddit, img_path)
    scraper.get_posts(time_filter, db, conn, img_handler)
    conn.close()

# get_posts('all')

today = datetime.date.today()
days_in_month = calendar.monthrange(today.year, today.month)[1]

def date_check():
    if str(today) == '1':
        get_posts('month')
    else:
        print('Time left till next reddit scrape: ', days_in_month - today.day)
    return

schedule.every().day.at('12:00').do(date_check)

while True:
    schedule.run_pending()
    app.run()
    time.sleep(1)
