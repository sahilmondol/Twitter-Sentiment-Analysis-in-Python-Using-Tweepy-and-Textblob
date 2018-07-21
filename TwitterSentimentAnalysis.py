#Dependencies which we are going to use
from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt

#Function to calculate the percentage
def percentage(part, whole):
    return 100 * float(part)/float(whole)

#All of these are taken from own twitter app
consumerKey = 'Your Consumer Key'
consumerSecret = 'Your ConsumerSecret'
accessToken = 'AccessToken'
accessTokenSecret = 'accessTokenSecret'

#Establishing the connection with the API
auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessToken , accessTokenSecret)
api = tweepy.API(auth)

#Searching the tweets
searchTerm = input("Enter the Keyword or the Hashtag to search about: ")
noOfSearchTerms = int(input("Enter the number of tweets to analyze: "))

#Establishing the connection
tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)

#Values going to used in TextBlob analysis
positive = 0
negative = 0
neutral = 0
polarity = 0

#Checking the Polarities
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity == 0):
        neutral += 1
    if (analysis.sentiment.polarity > 0.00):
        positive += 1
    if (analysis.sentiment.polarity < 0.00):
        negative += 1

# calculating the percentages
positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)

# percentages only upto two decimal places
positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')


print("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms) + " tweets.")

#Conditions based on the polarities
if(polarity == 0):
    print("Neutral")
elif(polarity < 0.00):
    print("Negative")
elif(polarity > 0.00):
    print("Positive")

#Creating the Graphical Result
labels = ['Positive['+str(positive)+'%]', 'Neutral['+str(neutral)+'%]', 'Negative['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellow', 'green', 'red']
patches , texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()