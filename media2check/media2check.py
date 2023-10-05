from fetch_trending import fetch_and_print_most_retweeted_tweets
from original_post import get_original_post

    '''
    Team M2C(Media2Check) wanted to apply filter model to all SNS platforms, 
    but some platforms do not provide API to access their data and we also
    have excluded platforms using image and video for future development.

    Twitter(currently X) is text-based platform which we had access and 
    were able to develop functions. Below is our approach to filter fake news.

    Prioritizing SNS posts to review will minimize resource input, thus M2C
    chose trending posts. 

    Then using user report system, if report rate is over 10% its up for
    review. Original post uploader is found and user is reviewed. API is 
    not provided by Twitter for this function so we assumed it will be provided 
    later. 

    User credibility is checked by credit scoring model and added bot upload 
    detection method by calculating upload time interval.

    Spread pattern is checked by looking at layers and number of retweets.

    Credibility score is set for each users for future analysis.  
    
    '''

def start():  # pylint: disable=too-many-return-statements,too-many-branches

    # Get the top trending topics
    trending_tweets = fetch_and_print_most_retweeted_tweets()
    
    result = get_original_post()
    print result
