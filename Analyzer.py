#Poras Shroff 2020 
#DataFraming from LucidProgramming https://www.youtube.com/watch?v=WX0MDddgpA4
#Twitter API library from https://github.com/bear/python-twitter
import twitter
import tweepy
import json
# from google.cloud import enum
from google.cloud import storage
import google.oauth2.credentials
from google.cloud import language_v1

# from google.cloud import types
# from searchtweets import collect_results

consumer_key = 'KZczaCiFdUlLJkmautw7YGxf8'
consumer_secret = 'qyNgBrYrX0YC6qfHg4QDRENKNcAZQ6k47HCZEID1QKhlpOUeOW'
access_token = '1292600738456248326-DzFIuKrFAZGjYCXJcJx5Z9qF22dkAW'
access_secret = 'cvbj6jWExK7QUlunhmmz6mUJpfxs5awtSVr0vhxC6riwM'

# Authenticate to Twitter
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_secret)

# Authenticate to Google
import google.oauth2.credentials

credentials = google.oauth2.credentials.Credentials(
    'bPU6i9SaTJeOBn23ogPaG9ok')


# Get Trending Tweets from Specific Location Based on WOEID
def trend_location(woeid=0):
    # all = []
    if woeid == 0:
        woeid = 2367105
    tweet = api.GetTrendsWoeid(woeid, exclude=None)
    # print(tweet)
    return tweet


def add(num):
    result = 1 + num
    return result


# def clean_tweet(self, tweet):
#     return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
# print(clean_tweet(trend_location(0)))


# # TopTrendsinBoston (or any WOEID entry) LINK for WOEID:
# # https://gist.githubusercontent.com/lukemelia/353493/raw/98749866fce79b591e45fb3325c853b4306a8882/WOEIDs%2520for
# # %2520US%2520Cities%2520with%2520population%2520over%2520100K%2520as%2520of%25202008%2520(from%2520Wikipedia)
# woeid = 0
# print("ENTER WOEID OF CITY:   ", )
# input(woeid)
# if woeid == 0:
#     woeid = 2367105
# atrend = api.GetTrendsWoeid(woeid, exclude=None)
# print("TOP TRENDING IN WOEID CITY:   ", atrend)

print("---------------------------------------------------")


# Sentiment Function
def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = [
        ('text', text),
        ('score', sentiment.score),
        ('magnitude', sentiment.magnitude),
    ]
    for k, v in results:
        print('{:10}: {}'.format(k, v))






