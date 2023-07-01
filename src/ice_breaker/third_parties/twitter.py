import logging
import os
from datetime import datetime, timezone
from typing import Dict, List

import tweepy

logger = logging.getLogger("twitter")

auth = tweepy.OAuthHandler(
    os.environ.get("TWITTER_API_KEY"), os.environ.get("TWITTER_API_KEY_SECRET")
)

auth.set_access_token(
    os.environ.get("TWITTER_ACCESS_TOKEN"),
    os.environ.get("TWITTER_ACCESS_TOKEN_SECRET"),
)

api = tweepy.API(auth)


def scrape_user_tweets(username: str, num_tweets: int = 10000):
    """Scrapes a Twitter user's origianl tweets (i.e., not rewteets or replies) and
    returns them as a list of dictionaries. Each dictionary has three fields:
    "time_posted" (relative to now), "text", and "url"

    Args:
        username (str): user name
        num_tweets (int, optional): number of tweets. Defaults to 5.
    """

    tweets = api.user_timeline(screen_name=username, count=num_tweets)

    tweet_list: List = []
    tweet_dict: Dict = {}
    for tweet in tweets:
        if "RT @" not in tweet.text and not tweet.text.startswith("@"):
            tweet_dict = {}
            tweet_dict["time_posted"] = str(
                datetime.now(timezone.utc) - tweet.created_at
            )

            tweet_dict["text"] = tweet.text
            tweet_dict[
                "url"
            ] = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
            tweet_list.append(tweet_dict)

    return tweet_dict


if __name__ == "__main__":
    scrape_user_tweets(username="elonmusk")
