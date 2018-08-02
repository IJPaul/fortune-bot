import twitter
import random
import fortunescraping
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# user specific information
CONSUMER_KEY = 'xxxx'
CONSUMER_SECRET = 'xxxx'
ACCESS_TOKEN_KEY = 'xxxx'
ACCESS_TOKEN_SECRET = 'xxxx'

# makes a call to tweet a fortune
fortuneCookieTweet()

def fortuneCookieTweet():
    api = twitter.Api(consumer_key = CONSUMER_KEY,
                      consumer_secret = CONSUMER_SECRET,
                        access_token_key = ACCESS_TOKEN_KEY,
                        access_token_secret = ACCESS_TOKEN_SECRET)
    
    html = urlopen('http://www.fortunecookiemessage.com/archive.php?start=0')
    bsObj = BeautifulSoup(html, 'lxml')
    
    all_quotes = []
    for internallink in fortunescraping.getInternalLinks(bsObj, 'http://www.fortunecookiemessage.com/archive.php'):
        quotes_on_page = fortunescraping.getPageElements(internallink, "a", {"href" : re.compile("^(\/cookie\/)")})
        for quote in quotes_on_page:
            all_quotes.append(quote)
    
    # set to true to enter while loop
    twitterError = True
    
    while twitterError:
        try:
            tweet = all_quotes[random.randint(0,len(all_quotes)-1)].get_text()
            status = api.PostUpdate(tweet)
            # set to False to exit loop if no error occurs
            twitterError = False
        # catches TwitterError potentially raised when posting
        # attempts to post another saying
        except twitter.error.TwitterError:
            twitterError = True
        except Exception as e:
            # see error in terminal
            print(e)
            pass




