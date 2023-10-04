# Twitter API tweepy used, credential and authenticate here removed for security reasons

# Function to search for the original post by a specific user
def find_original_post(screen_name, keyword):
    # Search for tweets containing the keyword
    tweets = api.search(q=keyword, lang="en", result_type="recent")

    for tweet in tweets:
        if tweet.user.screen_name == screen_name:
            # This tweet was posted by the user you're interested in
            return tweet

    return None

# Tracking original tweet information
original_tweet = find_original_post('original_account_name', 'your_keyword')

if original_tweet:
    print("Original post by @{original_tweet.user.screen_name}: {original_tweet.text}")
else:
    print("Original post not found.")
