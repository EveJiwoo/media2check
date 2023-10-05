# Twitter API tweepy used, credential and authenticate here removed for security reasons
from datetime import datetime

# Function to check if a user's tweets are from a bot
def is_bot(user_id):
    try:
        # Fetch the user's timeline
        tweets = api.user_timeline(user_id, count=200)  # You can adjust the count as needed

        # Calculate the time difference between consecutive tweets
        time_diffs = []
        for i in range(len(tweets) - 1):
            current_tweet = tweets[i]
            next_tweet = tweets[i + 1]
            time_diff = (next_tweet.created_at - current_tweet.created_at).total_seconds()
            time_diffs.append(time_diff)

        # Calculate the average time difference
        average_time_diff = sum(time_diffs) / len(time_diffs)

        # Define a threshold for upload time (5 minutes)
        threshold_seconds = 60 * 5  

        # Check if the average time difference is below the threshold
        if average_time_diff < threshold_seconds:
            return True
        else:
            return False

    except tweepy.TweepError as e:
        print(f"Error: {e}")
        return False

# User ID of the Twitter account you want to check
user_id = 'twitter_user_id'

# Check if the user is a bot
if is_bot(user_id):
    print(f"The user with ID {user_id} is a bot.")
else:
    print(f"The user with ID {user_id} is not a bot.")
