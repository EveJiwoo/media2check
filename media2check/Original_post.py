#Function to find whether the post is the original and if not, find the original post.
# Twitter API tweepy used, credential and authenticate here removed for security reasons

# Insert twitter ID for checkup on 'id_to_check' to find the original tweet
retweet_id = 'id_to_check'

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
