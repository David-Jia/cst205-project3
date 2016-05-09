import tweepy

#Personal to complete later
api_key = ""
api_secret = ""
oauth_token = ""   
oauth_token_secret = ""

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(oauth_token, oauth_token_secret)
api = tweepy.API(auth)

def tweetpicture(filename, message)
	#Tweet the picture with given file name
	api.update_with_media(filename, status=message)
	
	
