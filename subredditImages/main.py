"""The main file."""
from database_manager import db_manager
from img_download import img_url_handler
from json_loader import get_reddit
from json_loader import get_settings
from sub_scrape import sub_scrape
import schedule
import time

def first_run(time_filter):
    get_posts(time_filter)
    return schedule.CancelJob

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
    print("Next run:", schedule.next_run())




schedule.every().seconds.do(first_run, 'all')
schedule.every(4).weeks.do(get_posts, 'month')


while True:
    schedule.run_pending()
    time.sleep(10)
