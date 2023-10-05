# Twitter API tweepy used, credential and authenticate here removed for security reasons

# Replace 'retweet_id' with the ID of the retweet you want to find the original tweet for
retweet_id = 'your_retweet_id_here'

try:
    # Get the original tweet and the retweet using the retweet ID
    retweet = api.get_status(id=retweet_id, tweet_mode='extended', include_entities=True)

    # Check if the tweet is a retweet; if so, find the original tweet
    if hasattr(retweet, 'retweeted_status'):
        original_tweet = retweet.retweeted_status
        print("Original Tweet Text:", original_tweet.full_text)
        print("Original Tweet User:", original_tweet.user.screen_name)
        print("Retweet Text:", retweet.full_text)
        print("Retweet User:", retweet.user.screen_name)
    else:
        # If the tweet is not a retweet, it is already the original tweet
        print("Original Tweet Text:", retweet.full_text)
        print("Original Tweet User:", retweet.user.screen_name)
except tweepy.TweepError as e:
    print("Error: ", str(e))
