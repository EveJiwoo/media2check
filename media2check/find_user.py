#Function to find user id from tweet id
# Twitter API tweepy used, credential and authenticate here removed for security reasons

def get_original_poster_user_id(tweet_id):
    try:
        tweet = api.get_status(tweet_id)
        user_id = tweet.user.id_str  # Get the user's ID as a string
        return user_id
    except tweepy.TweepError as e:
        print(f"Error: {e}")
        return None

# Input the tweet ID
tweet_id = input("Enter the tweet ID: ")

# Get the user ID of the original poster of the tweet
user_id = get_original_poster_user_id(tweet_id)

if user_id:
    print(f"The user ID of the original poster is: {user_id}")
else:
    print("Unable to retrieve the user ID.")
