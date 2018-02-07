"""This class goes through reddit submissions."""
import praw
import datetime
import sys

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
        self.account = account
        self.reddit = praw.Reddit(
            client_id=self.account["client_id"],
            client_secret=self.account["client_secret"],
            user_agent="subbreddit scraper v0.1 by /u/isThisWhatIDo")
        self.subreddit = self.reddit.subreddit(subreddit)

    def get_posts(self, time_filter, db, conn, url_handler):
        """Retrives the subbmissions in top of subreddit, current limit is 100

        Creates a new row in database containing Path to image, title of post,
        post username, url to link and a 0. The url is used for debugging.
        """
        for submission in self.subreddit.top(time_filter):
            if submission.author is None or self.is_picture(submission.url) is False:
                continue
            else:
                title = submission.title
                user = submission.author.name
                url = submission.url
                path, num_pics, formatEr = url_handler.download(url, user)
                if formatEr:
                    data = (path, title, user, url, num_pics, 0)

                    try:
                        # I should use a try except here, which tries to put it into a new row
                        db.create_row(conn, data)
                        print("New row created: {} \n".format(data))
                    except:
                        e = sys.exc_info()
                        print("%s" % e)
                else:
                    continue

    def is_picture(self, url):
        """Check url for string matches to qualify that it is a picture."""
        allowed_links = ['.jpg', '.png', '/a/', '/gallery/']
        for img_url in allowed_links:
            if url.find(img_url) != -1:
                return True
        return False


    def eval_submission(self, submission):
        """Rate current submission.

        Evalualte the submissions, not really used atm.
        """
        comments = submission.num_comments
        ratio = submission.upvote_ratio
        result = comments * ratio
        return result
