import praw
import database

REDDIT = praw.Reddit('joker')
SUBREDDIT = REDDIT.subreddit("Jokes")
jokes = []
for submission in SUBREDDIT.hot(limit=5):
    title = submission.title
    text = submission.selftext
    score = submission.score
    flair = submission.link_flair_text
    print("Title: ", title)
    print("Text: ", text)
    print("Score: ", score)
    print("Flair: ", flair)
    print("------------------------------\n")
    joke = title, text, score, flair
    jokes.append(joke)
database.save_reddit_jokes(jokes)
