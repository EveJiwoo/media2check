import tweepy

#Twitter API credentials to access
consumer_key = 'our_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to search for the original post by a specific user
def find_original_post(screen_name, keyword):
    # Search for tweets containing the keyword
    tweets = api.search(q=keyword, lang="en", result_type="recent")

    for tweet in tweets:
        if tweet.user.screen_name == screen_name:
            # This tweet was posted by the user you're interested in
            return tweet

    return None

# Example usage
original_tweet = find_original_post('original_account_name', 'your_keyword')

if original_tweet:
    print(f"Original post by @{original_tweet.user.screen_name}: {original_tweet.text}")
else:
    print("Original post not found.")
