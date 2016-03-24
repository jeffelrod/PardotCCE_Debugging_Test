from twython import Twython, TwythonError
import time
#Api info goes here
APP_KEY = 'XXXXX'
APP_SECRET = 'XXXXX'
OAUTH_TOKEN = 'XXXXX'
OAUTH_TOKEN_SECRET = 'XXXXX'
#Use Twython to set up api access to twitter
api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#Read the things we need to tweet
with open('tweets.txt', 'r+') as tweetsfile:
	tweets = tweetsfile.readlines()

#Loop through all the tweets
for line in tweets[:]: 
	try:
			#What are we tweeting
			print ("Trying to tweet:\n" + line)
			#DEBUG
			#length = str(len(line))
			#print ("Line length: " + length)
			#Attempt to send the tweet - exception will show & we'll move on.
			api.update_status(status=line)
			#Debug
			print("Successfully tweeted:\n" + line) 
	#OHNOES!
	except TwythonError as e:
		#in case it didn't work
		error = str(e)
		print("Something went wrong :( \nError message: " + error + "\n")
		pass
	#Rate limit 
	time.sleep(5)
#Yey it worked
print ("I have tweeted AllTheThings fit to tweet!")
	