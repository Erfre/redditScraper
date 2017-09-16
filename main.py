from database_manager import db_manager
from sub_scrape import sub_scrape
from json_loader import *
import praw

# def get_top(sub, limit, db, conn):
#     """Retrives the subbmissions in hot.
#
#     Sends user, title, url to a new row in the database
#     """
#     for count, submission in enumerate(reddit.subreddit(sub).top(limit=limit)):
#         if submission.author is None:
#             continue
#         else:
#             result = eval_submission(submission)
#             url = submission.url
#             if result > 20 and is_picture(url):
#                 title = submission.title
#                 user = submission.author.name
#                 data = (title, user, url)
#                 db.create_row(conn, data)
#                 print("Submissions left: ", (limit - count))


# def is_picture(url):
#     """Check url for common image url."""
#     if 'imgur' or 'i.reddit' in url:
#         return True
#     else:
#         return False
#
#
# def eval_submission(submission):
#     """Rate current submission.
#
#     Something for future use.
#     """
#     comments = submission.num_comments
#     ratio = submission.upvote_ratio
#     result = comments * ratio
#     return result
#

def init():
    """Retrives inputs from user.

    :param subreddit: The subreddit name e.g funny
    :param db_directory: directory for database e.g /home/user/database/funn.db
    """
    reddit_account = get_reddit()
    print("This program saves posts from a subreddit into a database")
    subreddit = input("Enter what subreddit you want to scrape /r/")
    db_directory = input("Enter directory and name for database: ")
    time_filter = input("Enter time_filter(all,month,week,day,hour): ")
    limit = int(input("Enter amount of posts to fetch(Max: 1000): "))
    scraper = sub_scrape(subreddit, reddit_account)
    return subreddit, db_directory, limit, scraper, time_filter


def main():
    """Start program."""
    subreddit, db_dir, limit, scraper, time_filter = init()
    db = db_manager(db_dir)
    conn = db.create_connect()
    db.create_table(conn, "top")
    scraper.get_posts(limit, time_filter, db, conn)
    print("Done.")
    db.close()

main()
