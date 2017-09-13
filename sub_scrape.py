from json_loader import *
import praw

reddit_account = get_reddit()

reddit = praw.Reddit(client_id=reddit_account["client_id"],
                     client_secret=reddit_account["client_secret"],
                     user_agent="subbreddit scraper v0.1 by /u/isThisWhatIDo")

#this does not need to be a class TODO just add to main
# New way of getting submissions from the subbreddits
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

    def __init__(self, subreddit, limit):
        """Initilize."""
        super(sub_scrape, self).__init__()
        self.sub = subreddit
        self.limit = limit

    def get_hot(self):
        """Retrives the subbmissions in hot.

        Returns user, title, url, number of comments
        """
        for submission in reddit.subreddit(self.sub).top(limit=self.limit):
            if submission.author is None:
                continue
            else:
                result = self.eval_submission(submission)
                if result > 20:
                    title = submission.title
                    user = submission.author.name
                    url = submission.url
                    print(user, title, url)
                    # send into db {"title": title, "user": user, "link": url}

    def eval_submission(self, submission):
        """Rate current submission."""
        comments = submission.num_comments
        ratio = submission.upvote_ratio
        result = comments * ratio
        return result

a = sub_scrape('MechanicalKeyboards', 100)
print(a.get_hot())
