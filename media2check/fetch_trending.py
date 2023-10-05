# Function to fetch top 100 trending twitter posts and 
# Twitter API tweepy used, credential and authenticate here removed for security reasons
import tweepy
from tweepy import Cursor
import datetime
import schedule
import time

def get_trending_topics():
    try:
        trending_topics = api.get_place_trends(id=1)  # Using WOEID 1 for global trends
        return trending_topics[0]['trends'][:10]  # Get the top 10 trending topics
    except tweepy.TweepError as e:
        print(f"Error fetching trending topics: {e}")
        return []

def get_recent_tweets_for_topic(topic):
    try:
        tweets = api.search(q=topic, count=100)  
        return tweets
    except tweepy.TweepError as e:
        print(f"Error fetching tweets for {topic}: {e}")
        return []


# Define the search query for tweets with a specific hashtag or keyword
search_query = get_recent_tweets_for_topic()

def fetch_and_print_most_retweeted_tweets():
    # Get the current time
    current_time = datetime.datetime.now()
    
    # Calculate the start and end times for the previous hour
    end_time = current_time - datetime.timedelta(minutes=current_time.minute, seconds=current_time.second)
    start_time = end_time - datetime.timedelta(hours=1)
    
    # Create a list to store the most retweeted tweets
    most_retweeted_tweets = []

    # Iterate through tweets matching the search query and filter by the specified hour
    for tweet in Cursor(api.search, q=search_query, lang='en', tweet_mode='extended').items():
        tweet_time = tweet.created_at
        if start_time <= tweet_time <= end_time:
            most_retweeted_tweets.append(tweet)

    # Sort the list of tweets by the number of retweets in descending order
    most_retweeted_tweets.sort(key=lambda x: x.retweet_count, reverse=True)

    # Print the top 100 most retweeted tweets in the specified hour
    for i, tweet in enumerate(most_retweeted_tweets[:100]):
        print(f"{i + 1}. {tweet.user.screen_name}: {tweet.full_text} (Retweets: {tweet.retweet_count})")

# Schedule the job to run every hour
schedule.every().hour.do(fetch_and_print_most_retweeted_tweets)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
