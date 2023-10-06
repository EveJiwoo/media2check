# Receive tweet report number using tweepy and return tweets with more than 10% report rates
# Twitter API tweepy used, credential and authenticate here removed for security reasons
import tweepy

def check_report_rate(tweet_id):
    try:
        tweet = api.get_status(tweet_id)
        num_reports = tweet.user_reports + tweet.reports # Get the number of reports
        total_interactions = tweet.favorite_count + tweet.retweet_count + tweet.reply_count # Calculate total interactions
        
      # Calculate the report rate as a percentage
        report_rate = (num_reports / total_interactions)  
      

        return report_rate > .1  # Check if the report rate is greater than 10%
    except tweepy.TweepError as e:
        print(f"Error: {e}")
        return False
