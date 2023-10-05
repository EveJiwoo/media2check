# Function to find user's most recent 10 post upload times and interval
# Twitter API tweepy used, credential and authenticate here removed for security reasons

from datetime import datetime

def get_user_recent_tweets(username, count=10):
    try:
        user_tweets = api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
        return user_tweets
    except tweepy.TweepError as e:
        print(f"Error fetching tweets for {username}: {e}")
        return []

def calculate_time_intervals(tweet_times):
    intervals = []
    for i in range(len(tweet_times) - 1):
        time_diff = tweet_times[i] - tweet_times[i + 1]
        intervals.append(abs(time_diff.total_seconds()))
    return intervals

# Replace 'twitter_username' with the username of the Twitter user you want to analyze
username = 'twitter_username'
tweet_count = 10  # Adjust the number of tweets to retrieve as needed

user_tweets = get_user_recent_tweets(username, tweet_count)

if user_tweets:
    print(f"Upload times of recent tweets by {username}:")
    tweet_times = [tweet.created_at for tweet in user_tweets]
    for i, tweet_time in enumerate(tweet_times, 1):
        print(f"{i}. {tweet_time}")
    
    time_intervals = calculate_time_intervals(tweet_times)
    
    print("\nTime Intervals (in seconds):")
    for i, interval in enumerate(time_intervals, 1):
        print(f"Interval {i}: {interval} seconds")
else:
    print(f"No tweets found for {username}.")
