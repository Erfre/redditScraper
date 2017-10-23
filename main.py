"""The main file."""
from database_manager import db_manager
from img_download import img_url_handler
from json_loader import get_reddit
from json_loader import get_settings
from sub_scrape import sub_scrape
import schedule
import time

def main():

    """Start program."""
    tf = input("what timefilter would you like to use: ")
    limit = input("how many posts:")
    get_posts(tf, limit)
    print("Done.")



def get_posts(time_filter, limit):
    reddit_account = get_reddit()
    subreddit, db_dir, img_path = get_settings()
    scraper = sub_scrape(subreddit, reddit_account, limit)
    db = db_manager(db_dir)
    conn = db.create_connect()
    table_name = subreddit + "/" + time_filter
    db.create_table(conn, table_name)
    img_handler = img_url_handler(subreddit, img_path)
    scraper.get_posts(time_filter, db, conn, img_handler)
    conn.close()

schedule.every(4).weeks.do(get_posts('month', 300))

main()

while True:
    schedule.run_pending()
    time.sleep(1)
