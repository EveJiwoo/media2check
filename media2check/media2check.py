from fetch_trending import trending_tweets
from original_post import get_original_post_user_id
from report_rate import check_report_rate
from propagation_layer import get_propagation_layer
    '''
    Team M2C(Media2Check) wanted to apply filter model to all SNS platforms, 
    but some platforms do not provide API to access their data and we also
    have excluded platforms using image and video for future development.

    Twitter(currently X) is text-based platform which we had access to and 
    were able to develop functions. Down below is our approach to distingush 
    fake news from reliable news.

    Prioritizing SNS posts to review will minimize resource input, thus M2C
    chose trending posts. 

    Then using user report system, if report rate is over 10%, it is processed for
    review. In this step, the original post uploader is found and user is reviewed. 
    API is not provided by Twitter for this function, so we assumed it will be 
    provided later. 

    User credibility is checked by the credit scoring model and added bot upload 
    detection method by calculating upload time interval.

    Spread pattern is checked by looking at layers and number of retweets.

    Credibility score is set for each users for future analysis.  
    
    '''

def start():  # pylint: disable=too-many-return-statements,too-many-branches

    # Getting the top trending topics tweets
    trending_tweet_ids = trending_tweets()
   
    # Showing the trending tweet's id and text
    for i, (tweet_id, tweet_text) in enumerate(trending_tweets):
    print(f"{i + 1}. Tweet ID: {tweet_id}, Tweet Text: {tweet_text}")

    # Finding tweet id of report rate over 10% 
    suspicious_tweets  = check_report_rate(tweet_id)

    # Finding original uploader of trending posts
    original_upload = get_original_post_user_id(suspicious_tweets)
    print original_upload

    propagation_layer = get_propagation_layer(original_upload, max_depth=2)
    print(f"Propagaion Layer for {original_upload}:")
    for i, original_upload in enumerate(propagation_layer, 1):
        user = api.get_user(id=original_upload)
        print(f"{i}. {user.screen_name}")

    





    


    




