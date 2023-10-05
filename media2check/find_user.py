#Function to find user id from tweet id
# Twitter API tweepy used, credential and authenticate here removed for security reasons
import tweepy

def get_user_ids_from_tweet_ids(tweet_ids):
    user_ids = []
    for tweet_id in tweet_ids:
        user_id = get_user_id_from_tweet_id(tweet_id)
        if user_id:
            user_ids.append(user_id)
    return user_ids
