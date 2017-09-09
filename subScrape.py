import praw

reddit = praw.Reddit(client_id='my client id',
                     client_secret='my client secret',
                     user_agent='my user agent')


# New way of getting submissions from the subbreddits
class subScrape(object):
        """
        Takes 2 arguments:
        subreddit = string
        limit  =  integer
        Then it will go to the subreddit and search through all the submissions until it reaches the value of limit. Outputs 2 strings containing the author(username) and also the title of the post.
        """

    def __init__(self, subreddit, limit):
        super(subScrape, self).__init__()
        self.subreddit = subreddit
        self.limit = limit

    def get_submission(arg):
        for submission in reddit.subreddit(this.subreddit).hot(limit=limit):
            # Save the user, title and download the image
            submission.author.name
            submission.title
            submission.url

for submission in reddit.subreddit('MechanicalKeyboards').hot(limit=10):
    print(submission.title)
