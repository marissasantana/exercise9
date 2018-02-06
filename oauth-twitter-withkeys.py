from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.CONSUMER_KEY
client_secret = secrets.CONSUMER_SECRET

resource_owner_key = secrets.ACCESS_KEY
resource_owner_secret = secrets.ACCESS_SECRET

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

r = oauth.get(protected_url)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
tweets = json.loads(r.text)

print("LIST OF TWEETS")
for each_tweet in tweets["statuses"]:
    print(each_tweet["user"]["name"])
    print(each_tweet["text"])
