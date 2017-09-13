from database_manager import db_manager
from json_loader import *
import praw

reddit_account = get_reddit()

reddit = praw.Reddit(client_id=reddit_account["client_id"],
                     client_secret=reddit_account["client_secret"],
                     user_agent="subbreddit scraper v0.1 by /u/isThisWhatIDo")

db_directory = "/home/lqa/Databases/test/mk.db"
db = db_manager(db_directory)
conn = db.create_connect()
db.create_table(conn, "top")


def get_hot(sub, limit):
    """Retrives the subbmissions in hot.

    Returns user, title, url, number of comments
    """
    for submission in reddit.subreddit(sub).top(limit=limit):
        if submission.author is None:
            continue
        else:
            result = eval_submission(submission)
            if result > 20:
                title = submission.title
                user = submission.author.name
                url = submission.url
                row = (title, user, url)
                db.create_row(conn, row)


def eval_submission(submission):
    """Rate current submission."""
    comments = submission.num_comments
    ratio = submission.upvote_ratio
    result = comments * ratio
    return result


def main():
    get_hot('MechanicalKeyboards', 20)


main()
