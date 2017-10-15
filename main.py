"""The main file."""
from database_manager import db_manager
from img_download import img_url_handler
from json_loader import get_reddit
from json_loader import get_settings
from sub_scrape import sub_scrape
import schedule
import time

def init():
    """Retrives inputs from user."""
    reddit_account = get_reddit()
    print("This program saves image-posts from a subreddit into a database")
    subreddit, db_directory, time_filter, img_path = get_settings()
    limit = 1000
    scraper = sub_scrape(subreddit, reddit_account, limit)
    time_filter = "all"
    return subreddit, db_directory, scraper, time_filter, img_path


def main():
    conn.close()

    """Start program."""
    subreddit, db_dir, scraper, time_filter, img_path = init()
    db = db_manager(db_dir)
    conn = db.create_connect()
    db.create_table(conn, subreddit + time_filter)
    img_handler = img_url_handler(subreddit, img_path)
    scraper.get_posts(time_filter, db, conn, img_handler)
    print("Done.")



def month_top():
    reddit_account = get_reddit()
    limit = 1000
    subreddit, db_dir, time_filter, img_path = get_settings()
    scraper = sub_scrape(subreddit, reddit_account, limit)
    db = db_manager(db_dir)
    conn = db.create_connect()
    db.create_table(conn, subreddit + time_filter)
    img_handler = img_url_handler(subreddit, img_path)
    scraper.get_posts(time_filter, db, conn, img_handler)
    conn.close()

schedule.every(4).week.do(month_top)

main()

while True:
    schedule.run_pending()
    time.sleep(1)



# Fix a checker for the image so it saves as a jpg format, then move on to the bot