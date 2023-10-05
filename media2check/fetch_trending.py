# Function to fetch top 100 trending twitter posts and 
# Twitter API tweepy used, credential and authenticate here removed for security reasons
import tweepy


# Define the WOEID for the United States
woeid_usa = 23424977

# Function to fetch trending tweets and their Tweet IDs
def fetch_trending_tweets(woeid, count):
    trending_tweets = []
    
    # Twitter's API returns trends in batches of 50, so we need to make multiple requests
    num_batches = count // 50
    for _ in range(num_batches):
        trends = api.get_place_trends(id=woeid)
        for trend in trends[0]['trends']:
            tweet_id = trend['tweet_volume']  # Tweet ID is stored in the 'tweet_volume' field
            tweet_text = trend['name']
            trending_tweets.append((tweet_id, tweet_text))
    
    return trending_tweets

# Get the top 100 trending tweets and their Tweet IDs for the specified location
trending_tweets = fetch_trending_tweets(woeid_usa, count=100)

# Print the trending tweets and their Tweet IDs
for i, (tweet_id, tweet_text) in enumerate(trending_tweets):
    print(f"{i + 1}. Tweet ID: {tweet_id}, Tweet Text: {tweet_text}")
