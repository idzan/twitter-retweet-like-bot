import tweepy
import time
from multiprocessing import Process

""" Auth Tokens from developer.twitter.com """
auth = tweepy.OAuthHandler('pCOCxbVpve2OYXE5nOL2IFo27','0qJNJEf6Kt8cgc7xVbtd6D2EK493jNX0hI49KSBcF0AGuYFRM5')
auth.set_access_token('1221811184741036032-iOh87phfH7Lp2td3nqugBg2IynsfAz','oCjLvx1Ta14P8PLwu0eiFzaFEs8K8mRzqQjIBmMbxt2ZD')
""" Basic setup wth rate limiters online """
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
""" Running as my personal account created for this code """
user = api.me()
""" Search Terms """
s1 = 'Web Design'
s2 = 'html'
s3 = 'css'
s4 = 'javascript'
s5 = 'wordpress'

""" Limiting nr of Tweets """
nrTweets = 250

""" Loop for search term """
def sterm1():
    for tweet in tweepy.Cursor(api.search, s1).items(nrTweets):
        try:
            print('Tweet Retweeted')
            tweet.retweet()
            time.sleep(10)
        except tweepy.TweepError as e1:
            print(e1.reason)
        except StopIteration:
            break
def sterm2():
    for tweet in tweepy.Cursor(api.search, s2).items(nrTweets):
        try:
            print('Retweeted')
            tweet.retweet()
            time.sleep(10)
        except tweepy.TweepError as e2:
            print(e2.reason)
        except StopIteration:
            break
def sterm3():
    for tweet in tweepy.Cursor(api.search, s3).items(nrTweets):
        try:
            print('Retweeted This')
            tweet.retweet()
            time.sleep(10)
        except tweepy.TweepError as e3:
            print(e3.reason)
        except StopIteration:
            break
def sterm4():
    for tweet in tweepy.Cursor(api.search, s4).items(nrTweets):
        try:
            print('Did I Retweeted This')
            tweet.retweet()
            time.sleep(10)
        except tweepy.TweepError as e4:
            print(e4.reason)
        except StopIteration:
            break
def sterm5():
    for tweet in tweepy.Cursor(api.search, s5).items(nrTweets):
        try:
            print('Retweeted That')
            tweet.retweet()
            time.sleep(10)
        except tweepy.TweepError as e5:
            print(e5.reason)
        except StopIteration:
            break

""" Looping trough search terms and running loops with Multiprocessing """
if __name__ == "__main__":
    Process(target=sterm1).start()
    Process(target=sterm2).start()
    Process(target=sterm3).start()
    Process(target=sterm4).start()
    Process(target=sterm5).start()