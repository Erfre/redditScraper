"""The main file."""
from database_manager import db_manager
from json_loader import get_reddit
from sub_scrape import sub_scrape


def init():
    """Retrives inputs from user.

    :param subreddit: The subreddit name e.g funny
    :param db_directory: directory for database e.g /home/user/database/funn.db
    """
    reddit_account = get_reddit()
    print("This program saves image-posts from a subreddit into a database")
    subreddit = input("Enter what subreddit you want to scrape /r/")
    db_directory = input("Enter directory and name for database: ")
    time_filter = input("Enter time filter(all,month,week,day,hour): ")
    limit = int(input("Enter amount of posts to fetch(Max: 1000): "))
    scraper = sub_scrape(subreddit, reddit_account, limit)
    return subreddit, db_directory, scraper, time_filter


def main():
    """Start program."""
    subreddit, db_dir, scraper, time_filter = init()
    db = db_manager(db_dir)
    conn = db.create_connect()
    db.create_table(conn, "top")
    scraper.get_posts(time_filter, db, conn)
    print("Done.")
    conn.close()

main()
