# Getting User Timeline through entry of twitter handle 
# Using Python-Twitter https://github.com/twitterdev/search-tweets-python

import twitter
from searchtweets import collect_results


consumer_key = '<Enter Here>'
consumer_secret = '<Enter Here>'
access_token = '<Enter Here>'
access_secret = '<Enter Here>'


# Authenticate to Twitter
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_secret)


(api.VerifyCredentials())

#GetUserTimeline
x = 0
print("Enter Twitter Handle:   ")

user=api.GetUserTimeline(
                         user_id= None,
                         screen_name= input(x),
                         max_id=None,
                         count=None,
                         include_rts=True,
                         trim_user=False,
                         exclude_replies=False)
print("User TimeLine:   ", user)
print("---------------------------------------------------")

#GetCurrentTrends
gtrends=api.GetTrendsCurrent(exclude=None)
print("Current Global Trends:  " ,gtrends)
print("---------------------------------------------------")

#TopTrendsinBoston (or any WOEID entry)
#LINK for WOEID: https://gist.githubusercontent.com/lukemelia/353493/raw/98749866fce79b591e45fb3325c853b4306a8882/WOEIDs%2520for%2520US%2520Cities%2520with%2520population%2520over%2520100K%2520as%2520of%25202008%2520(from%2520Wikipedia)
woeid = 0
print("ENTER WOEID OF CITY:   ",)
input(woeid)
if woeid == 0:
    woeid= 2367105
atrend=api.GetTrendsWoeid(woeid,exclude=None)
print("TOP TRENDING IN WOEID CITY:   ", atrend)

print("---------------------------------------------------")
