import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = '5xsAm0kwO081GICB7XlUzv0Wg'
consumer_secret = 'wHO0215esMPxRj8aczyLedy7DevwuJIs3uhDfQqCsiDVJCJMn4'
access_token = '94841462-20r265kSDWnxohzq2P8e53NGNw4H6DATSVnxF6UIr'
access_token_secret = 'CWwOtlp3ApHhJzNkHYXPzHQRABZ2lemjrhdkUSGaw0W4t'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('nba.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#NBAFinals",count=50,
                           lang="en",
                           since="2019-05-26").items():
    #print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])