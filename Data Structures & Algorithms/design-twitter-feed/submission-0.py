class Twitter:
    # Normally when I think to find the most recent N elements, the first thought that comes to mind is a heap
    # However I think for the sake of simplicity, we can first try with an array based approach
    # We need a way to store info about the tweets and about the users and the tweets

    def __init__(self):
        # For the users we can store a list of people they follow since that is what we really care about for this question
        # Each user doesn't really hold a list of who follows them. It only knows who they follow
        # We are using a set here because we want to be able to do a quick lookup for if a user is one that I follow
        self.users = defaultdict(set)

        # We can now hold an array of tweets of type (userId, tweetId)
        # And because we only ever add to the back, the array will always be sorted from the oldest tweet to the newest tweet
        self.tweets = []


    def postTweet(self, userId: int, tweetId: int) -> None:
        # We can just add the new tweet to the end of the tweets array. 
        # We expect each tuple to be unique since the tweetIds are guaranteed to be different
        self.tweets.append((userId, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        # We want the 10 most recent tweets, and because our array is sorted oldest to newest, 
        # we can walk it from the back so that we always see the newest tweets first
        tweets = []
        for i in range(len(self.tweets)-1, -1, -1):
            uid, tid = self.tweets[i]

            # If I am the user who posted the tweet, or the poster of the tweet is a user in the list of users I follow
            if uid == userId or uid in self.users[userId]:
                tweets.append(tid)

            # Since we started from the newest tweet, the first 10 we find are the 10 most recent
            # So if we have gotten enough tweets, there is no need to keep looking
            if len(tweets) == 10: break

        return tweets
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # One of the constraints is that a user cannot follow themself
        if followerId == followeeId: return

        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # One of the constraints is that a user cannot follow themself
        # We also don't want to try removing a followee if we aren't following them, to avoid a KeyError
        if followerId == followeeId or followeeId not in self.users[followerId]: return

        self.users[followerId].remove(followeeId)