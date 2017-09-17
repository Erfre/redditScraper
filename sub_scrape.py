"""This class goes through reddit submissions."""
import praw


class sub_scrape(object):
    """Scrape a subbreddit for pictures.

    Keyword arguments:
    subreddit = string
    limit     = integer

    Then it will go to the subreddit and search through all the
    submissions until it reaches the value of limit.
    Outputs 2 strings containing the author(username)
    and also the title of the post.
    """

    def __init__(self, subreddit, account):
        """Initilize."""
        super(sub_scrape, self).__init__()
        self.sub = subreddit
        self.account = account
        self.reddit = praw.Reddit(
            client_id=self.account["client_id"],
            client_secret=self.account["client_secret"],
            user_agent="subbreddit scraper v0.1 by /u/isThisWhatIDo")

    def get_posts(self, limit, month, db, conn):
        """Retrives the subbmissions in hot.

        Returns user, title, url, number of comments
        """
        for count, submission in enumerate(self.reddit.subreddit(self.sub).top(month)):
            if submission.author is None:
                continue
            else:
                result = self.eval_submission(submission)
                url = submission.url
                if result > 20 and self.is_picture(url):
                    title = submission.title
                    user = submission.author.name
                    data = (title, user, url)
                    db.create_row(conn, data)
                    print("Submissions left: ", (limit - count))

    def eval_submission(self, submission):
        """Rate current submission.

        Something for future use.
        """
        comments = submission.num_comments
        ratio = submission.upvote_ratio
        result = comments * ratio
        return result

    def is_picture(self, url):
        """Check url for common image url."""
        if 'imgur' or 'i.reddit' in url:
            return True
        else:
            return False
