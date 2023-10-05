#Function to find user id from tweet id
# Twitter API tweepy used, credential and authenticate here removed for security reasons

def get_user_id_from_tweet_id(tweet_id):
    try:
        # Get the tweet object
        tweet = api.get_status(tweet_id)
        # Extract the user ID from the tweet
        user_id = tweet.user.id_str
        return user_id
    except tweepy.TweepError as e:
        print(f"Error: {e}")
        return None
