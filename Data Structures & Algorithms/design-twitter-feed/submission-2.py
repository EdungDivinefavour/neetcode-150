class Twitter:
    # Compared to solution 0, how can we improve our time complexity? In solution 0 we had to go through eeeeevery tweet to find the ones relevant to a user.
    # So if we had 10000 tweets and none from the user or their followees, we would scan the entire array only to find nothing for that user.
    # I think we can switch up solution 0 a bit. So instead of storing every tweet in one array and then fetching the top N when we want them,
    # We can do some of that hardwork upfront at the time of storing and store the tweets on a per user basis instead of one giant array

    def __init__(self):
        # For the users we can store a set of people they follow since that is what we really care about for this question
        # Note: Each user key does not really hold a list of who follows them. It only holds who they follow.
        # We are using a set here because we want to be able to do a quick lookup for if a user is one that we follow
        self.followees = defaultdict(set)

        # Basically, each user's tweets would look like this
        # tweets: {
        #    "userId": [tweet1, tweet2, tweet3]
        # }
        self.tweets = defaultdict(list)

        # Tweets from different users will now be in different arrays, so their order in their parent array cannot tell us which one is newer anymore
        # So we can make every tweet to just carry a timestamp field that goes up by 1 every time anybody posts. So basically a bigger timestamp means a newer tweet
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        # We can just add the new tweet to the end of the user's own tweets. 
        # We expect each tuple to be unique since the tweetIds are guaranteed to be different
        # Storing using timestamp first to make our lives easier when we want to build the heap
        self.tweets[userId].append((self.timestamp, userId, tweetId))
        self.timestamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        # I see a lot of unnecessary work in this method in solution 1. We can just use a heap to store all tweets from the relevant sources
        # We want the 10 most recent tweets from (me and everyone I follow)
        # Python's heap is a min heap, so the smallest value is always considered the largest. But we want the newest tweet(biggest timestamp) at the top
        # So we store the negative of every timestamp, which flips it around so that the newest tweet looks like the smallest value
        # So we start by gathering all of my tweets
        tweets = [(-ts, uid, tid) for ts, uid, tid in self.tweets[userId]]

        # and then all the tweets of everyone I follow
        # These have to be negated too. If we didn't, we would be mixing negative and positive timestamps in one heap and the order would make no sense
        for followee in self.followees[userId]:
            tweets.extend((-ts, uid, tid) for ts, uid, tid in self.tweets[followee])
        
        # Turn our list into a heap in one go. This is O(n) which is better than pushing the tweets in one by one
        heapq.heapify(tweets)

        # Now the newest tweet is at the top, so popping gives us the tweets from newest to oldest
        # The tweetId is the last element of the tuple, and that is the only thing we want to return
        out = []
        while tweets:
            out.append(heapq.heappop(tweets)[-1])

            # We only want the 10 most recent, so once we have 10 here is no need to pop the rest
            if len(out) == 10: break
        
        return out
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # One of the constraints is that a user cannot follow themself
        if followerId == followeeId: return

        self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # One of the constraints is that a user cannot follow themself
        # We also don't want to try removing a followee if we aren't following them, to avoid a KeyError
        if followerId == followeeId or followeeId not in self.followees[followerId]: return

        self.followees[followerId].remove(followeeId)