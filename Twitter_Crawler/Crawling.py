import tweepy

class CrawlingTwitter:

    def __init__(self):
        self.consumer_key = 'NpGs7OhqboYu7IxDIWw5drDSr'
        self.consumer_secret = 'WA3L6YYd76GvGzMzFqAhP2RkqPXpFFHxuM1k9OUxThvStjShwr'
        self.access_token = '1951831687-o0wQNmWLFqskWM7LrZqadRp6ZKfbR9cgywDfYaH'
        self.access_secret = 'qnDAb3C4W3f1JHw46i01KTjxxVKloOgxLXmfsXpq0JaAU'
        self.tweetsPerQry = 100
        self.maxTweets = 1000
        self.api = self.authToAPITwitter()
    
    def authToAPITwitter(self):
        authentication = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        authentication.set_access_token(self.access_token, self.access_secret)
        return tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def getCrawling(self, hashtag):
        maxId = -1
        tweetCount = 0
        tweets = []
        while tweetCount < self.maxTweets:
            if(maxId <= 0):
                newTweets = self.api.search(q=hashtag, count=self.tweetsPerQry, result_type="recent", tweet_mode="extended")
            else:
                newTweets = self.api.search(q=hashtag, count=self.tweetsPerQry, max_id=str(maxId - 1), result_type="recent", tweet_mode="extended")

            if not newTweets:
                print("Tweet Habis")
                break
            
            for tweet in newTweets:
                tweets.append(tweet.full_text.encode('utf-8'))
            tweetCount += len(newTweets)
            maxId = newTweets[-1].id
        self.saveData(hashtag, tweets)
    
    def saveData(self, hashtag, tweets):
        f = open('tweets_'+hashtag+'.txt','w')
        for tweet in tweets:
            f.write(str(tweet)+'\n')
        f.close()

crawler = CrawlingTwitter()
crawler.getCrawling("#papua")