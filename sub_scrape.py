from json_loader import *
import praw

reddit = praw.Reddit(client_id='my client id',
                     client_secret='my client secret',
                     user_agent='my user agent')


# New way of getting submissions from the subbreddits
class subScrape(object):
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
        super(subScrape, self).__init__()
        self.subreddit = subreddit
        self.limit = limit

    def get_hot(arg):
        """Retrives the subbmissions in hot.

        Returns user, title, url, number of comments
        """
        for submission in reddit.subreddit(self.subreddit).hot(limit=self.limit):
            # Save the user, title and download the image
            user = submission.author.name
            title = submission.title
            url = submission.url
            num_comments = submission.num_comments

for submission in reddit.subreddit('MechanicalKeyboards').hot(limit=10):
    print(submission.title)

print(get_reddit())
