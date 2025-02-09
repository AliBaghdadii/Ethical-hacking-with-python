import tweepy

def search_twitter(query, count=10):
    # Replace these with your own Twitter API credentials
    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    try:
        tweets = api.search_tweets(q=query, count=count)
        for tweet in tweets:
            print(f"User: {tweet.user.screen_name}")
            print(f"Tweet: {tweet.text}")
            print(f"Creaed at: {tweet.created_at}")
            print("---")
    except tweepy.TweepError as e:
        print(f"Error: {e}")

search_twitter("Cybersecurity", count=5)