from database_manager import db_manager
from json_loader import *
import praw

reddit_account = get_reddit()

reddit = praw.Reddit(client_id=reddit_account["client_id"],
                     client_secret=reddit_account["client_secret"],
                     user_agent="subbreddit scraper v0.1 by /u/isThisWhatIDo")


def get_hot(sub, limit, db, conn):
    """Retrives the subbmissions in hot.

    Sends user, title, url to a new row in the database
    """
    for count, submission in enumerate(reddit.subreddit(sub).top(limit=limit)):
        if submission.author is None:
            continue
        else:
            result = eval_submission(submission)
            if result > 20:
                title = submission.title
                user = submission.author.name
                url = submission.url
                data = (title, user, url)
                db.create_row(conn, data)
                print("Submissions left: ", (limit - count))


def eval_submission(submission):
    """Rate current submission.

    Something for future use.
    """
    comments = submission.num_comments
    ratio = submission.upvote_ratio
    result = comments * ratio
    return result


def init():
    """Retrives inputs from user.

    :param subreddit: The subreddit name e.g funny
    :param db_directory: directory for database e.g /home/user/database/funn.db
    """
    print("This program saves posts from a subreddit into a database")
    subreddit = input("Enter what subreddit you want to scrape /r/")
    db_directory = input("Enter directory and name for database: ")
    limit = input("Enter amount of posts to fetch(Max: 1000): ")
    return subreddit, db_directory, limit


def main():
    """Start program."""
    subreddit, db_dir, limit = init()
    db = db_manager(db_dir)
    conn = db.create_connect()
    db.create_table(conn, "top")
    get_hot(subreddit, limit, db, conn)
    print("Done.")

main()
