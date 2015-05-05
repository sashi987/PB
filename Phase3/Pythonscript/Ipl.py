#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#This is a basic listener class that just prints received tweets data to file/standardoutoutput.
class Tweet_Download(StreamListener):

    def on_data(Id, tweet_data):
        print (tweet_data)
        return True

    def on_error(Id, status_Content):
        print (status_Content)


# Go to http://dev.twitter.com and create an app to get authentication keys for getting tweets.
# Below are keys given by to user for developing application
consumer_key_Given_By_Twiter = "nlnuMkd5AFe7WKrdnqFoNH6Qm"
consumer_secret_Given_By_Twiter = "ozz3x536FnmpAHuBIYi7DwJgwvLNuSreQPaGYLudXgoAnw7oqB"
		
#Below are access keys for our application to login into twitter to get tweets 
access_token_Given_By_Twiter = "136895952-4gOLa18nHJfqAMovCETZGQAtbtt7CzDty6eXwOeX"
access_token_secret_Given_By_Twiter = "S7R72kLNjs7HdUMjvA4ThMEmz21dAhOPB1rFGqFtHNgOI"
		

if __name__ == '__main__':

    #This handles Twitter authentication and the connection to Twitter Streaming API
	#Initiating an instance
    Tweet_download_Instance = Tweet_Download()
	# by using tweepy api we are handling authentication
    authenticatio_Instance = OAuthHandler(consumer_key_Given_By_Twiter, consumer_secret_Given_By_Twiter)
    authenticatio_Instance.set_access_token(access_token_Given_By_Twiter, access_token_secret_Given_By_Twiter)
	# Downloading streaming Tweets by initiating instance
    stream_Instance = Stream(authenticatio_Instance, Tweet_download_Instance)

    #Geting tweets based on hashtags
    stream_Instance.filter(track=['IPL2015','RCB','KKR','Kohli','ABD','Ghambir','RCBVSKKR','Virat','Uthappa'])