from twitter import Api as twitter_api
from os import environ

TWITTER_CONSUMER_KEY = environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = environ['CONSUMER_SECRET']
TWITTER_ACCESS_TOKEN_KEY = environ['ACCESS_TOKEN_KEY']
TWITTER_ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

TWITTER = twitter_api(consumer_key=TWITTER_CONSUMER_KEY, consumer_secret=TWITTER_CONSUMER_SECRET,
                      access_token_key=TWITTER_ACCESS_TOKEN_KEY, access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)


def handler():
    borderlands_twitter_timeline = TWITTER.GetUserTimeline(screen_name="Borderlands")
