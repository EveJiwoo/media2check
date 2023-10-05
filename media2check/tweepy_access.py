#Accessing Twitter(Currently X) API
import tweepy

#Twitter credentials to access API(not shown here for security reason)
consumer_key = 'our_key'
consumer_secret = 'our_consumer_secret'
access_token = 'our_access_token'
access_token_secret = 'our_access_token_secret'

# Authenticate process for Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
