# Eliminate spamming accounts by calculating average upload time interval  
# Twitter API tweepy used, credential and authenticate here removed for security reasons
from datetime import datetime
from find_user import get_user_id_from_tweet_ids


user_ids = get_user_id_from_tweet_id(tweet_id)


# Function to check if a user's tweets are from a bot
def is_bot(user_ids):
    try:
        # Fetch the user's timeline
        tweets = api.user_timeline(user_id, count=20)  
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

# Check if the user is a bot
if is_bot(user_id):
    print(f"The user with ID {user_id} is a bot.")
else:
    print(f"The user with ID {user_id} is not a bot.")
