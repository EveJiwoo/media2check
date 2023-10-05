# Function to fetch top 100 trending twitter posts 
# Twitter API tweepy used, credential and authenticate here removed for security reasons

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

# Get the top trending topics
trending_topics = get_trending_topics()

if trending_topics:
    print("Top Trending Topics:")
    for i, topic in enumerate(trending_topics, 1):
        print(f"{i}. {topic['name']}")
        print("   Recent Tweets:")
        recent_tweets = get_recent_tweets_for_topic(topic['name'])
        for j, tweet in enumerate(recent_tweets, 1):
            print(f"   {j}. {tweet.text}\n")
else:
    print("No trending topics found.")