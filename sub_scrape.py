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

    def __init__(self, subreddit, account, limit):
        """Initilize."""
        super(sub_scrape, self).__init__()
        self.sub = subreddit
        self.account = account
        self.reddit = praw.Reddit(
            client_id=self.account["client_id"],
            client_secret=self.account["client_secret"],
            user_agent="subbreddit scraper v0.1 by /u/isThisWhatIDo")
        self.limit = limit

    def get_posts(self, time_filter, db, conn, url_handler):
        """Retrives the subbmissions in hot.

        Returns user, title, url, number of comments
        """
        count = 0

        for submission in self.reddit.subreddit(self.sub).top(time_filter):
            if submission.author is None:
                continue
            elif count == self.limit:
                return
            else:
                result = self.eval_submission(submission)
                url = submission.url
                if result > 20 and self.is_picture(url):
                    count += 1
                    title = submission.title
                    user = submission.author.name
                    desc = self.create_simple_description(title, user)
                    path = url_handler.download(url, user)
                    data = (path, desc, 0, url)
                    db.create_row(conn, data)
                    print("Submissions left: ", (self.limit - count))

    def create_simple_description(self, title, user):
        """Give post a simple description."""
        description = title + '\n\n\n\n' + 'credit: /u/' + user
        return description

    def eval_submission(self, submission):
        """Rate current submission.

        Evalualte the submissions, not really used atm.
        """
        comments = submission.num_comments
        ratio = submission.upvote_ratio
        result = comments * ratio
        return result

    def is_picture(self, url):
        """Check url for common image url."""
        if 'gfycat' in url:
            return False
        elif '.jpg' or '.png' or '/a/' in url:
            return True
        else:
            return False
