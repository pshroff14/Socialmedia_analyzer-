#Poras Shroff 2020 
#DataFraming from LucidProgramming https://www.youtube.com/watch?v=WX0MDddgpA4
#Twitter API library from https://github.com/bear/python-twitter
import twitter
import requests
from google.cloud import language
from google.cloud.language import enums, types
import pandas #for data framing




r=requests.get('https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSentiment#http-request')



from searchtweets import collect_results


consumer_key = 'Enter Here'
consumer_secret = 'Enter Here'
access_token = 'Enter Here'
access_secret = 'Enter Here'


# Authenticate to Twitter
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_secret)

#Authentication to Google NLP
from gcloud.aio.auth import IamClient
from gcloud.rest.auth import Token
client = IamClient()
pubkeys = await client.list_public_keys()
token = Token()
print(token.get())
print("-----------------")


(api.VerifyCredentials())

#Sentiment Function
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

#Json tweet to data frame function
def tweets_to_data_frame(self,tweets):
    df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
    return df



#GetCurrentTrends
gtrends=api.GetTrendsCurrent(exclude=None)
print("Current Global Trends:  " ,gtrends)
print("---------------------------------------------------")

#data framing
df = tweets_to_data_frame(gtrends)

#Sentiment of GetCurrentTrends from the data framing
analyze_text_sentiment(df)









