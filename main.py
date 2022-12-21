import tweepy
import os
import time, datetime

my_api_key = os.environ['api_key']
my_api_secret_key = os.environ['api_secret']
my_access_token = os.environ['access_token']
my_secret_access_token = os.environ['access_token_secret']
my_bearer_token = os.environ['bearer_token']
"""
def api():
  auth = tweepy.OAuthHandler(my_api_key, my_api_secret_key)
  auth.set_access_token(my_access_token, my_secret_access_token)

  return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path=None):
  if image_path:
    api.update_status_with_media(message, image_path)

  else:
    api.update_status(message)

  print('Tweeted successfully!')


if __name__ == '__main__':
  api = api()
  tweet(api, '해찬봇 시작!', 'Haechan2.jpg')
  tweet(api, 'HaeChan Bot is Online!', 'haechan.jpg')
"""

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(my_bearer_token, my_api_key, my_api_secret_key,
                       my_access_token, my_secret_access_token)

auth = tweepy.OAuth1UserHandler(my_api_key, my_api_secret_key, my_access_token,
                                my_secret_access_token)
api = tweepy.API(auth)


# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

  # This function gets called when a tweet passes the stream
  def on_tweet(self, tweet):

    # Retweeting the tweet
    try:
      # Retweet
      client.retweet(tweet.id)

      # Printing Tweet
      print(tweet.text)

      # Delay
      time.sleep(300)

    except Exception as error:
      # Error
      print(error)


# Creating Stream object
stream = MyStream(bearer_token=my_bearer_token)
stream.add_rules(
  tweepy.StreamRule("#HAECHAN OR #해찬 AND from:NCTsmtown -is:reply"))
stream.filter()
