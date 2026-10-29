class Twitter:
    # Compared to our last solution, how can we improve our time complexity? In the last solution we had to go through eeeeevery tweet to find the ones relevant to a user.
    # So if we had 10000 tweets and none from the user or their followees, we would scan the entire array only to find nothing for that user.
    # I think we can switch up our last solution a bit. So instead of storing every tweet in one array and then fetching the top N when we want them,
    # We can do some of that hardwork upfront at the time of storing and store the tweets on a per user basis instead of one giant array

    def __init__(self):
        # For the users we can store a set of people they follow since that is what we really care about for this question
        # Note: Each user key does not really hold a list of who follows them. It only holds who they follow.
        # We are using a set here because we want to be able to do a quick lookup for if a user is one that we follow
        self.followees = defaultdict(set)


        self.tweets = defaultdict(list)
        # Basically, each user's tweets would look like this
        # tweets: {
        #    "userId": [tweet1, tweet2, tweet3]
        # }

        # Tweets from different users will now be in different arrays, so their order in their parent array cannot tell us which one is newer anymore
        # So we can make every tweet to just carry a timestamp field that goes up by 1 every time anybody posts. So basically a bigger timestamp means a newer tweet
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        # We can just add the new tweet to the end of the user's own tweets. 
        # We expect each tuple to be unique since the tweetIds are guaranteed to be different
        self.tweets[userId].append((userId, tweetId, self.timestamp))
        self.timestamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        # We want the 10 most recent tweets from me and everyone I follow
        # So we start by gathering all of my tweets, and then all the tweets of everyone I follow
        tweets = []
        tweets.extend(self.tweets[userId])

        for followee in self.followees[userId]:
            tweets.extend(self.tweets[followee])
        
        # Then sort them by the last element in the tuple ie the timestamp
        # A bigger timestamp means a newer tweet, so that's we sort in reverse to get the newest tweets at the front
        tweets.sort(key=lambda x: x[-1], reverse=True)

        # We only want the first 10, and from each tuple we only want the tweetId, not the userId or the timestamp
        return [el[1] for el in tweets[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # One of the constraints is that a user cannot follow themself
        if followerId == followeeId: return

        self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # One of the constraints is that a user cannot follow themself
        # We also don't want to try removing a followee if we aren't following them, to avoid a KeyError
        if followerId == followeeId or followeeId not in self.followees[followerId]: return

        self.followees[followerId].remove(followeeId)