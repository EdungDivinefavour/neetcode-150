class TimeMap:
        # Our data structure will look something like this
        # {
        #     "key1": [
        #         (100, "dog"),
        #         (200, "cat"),
        #         (300, "eye"),
        #         (400, "fat"),
        #         (500, "goat"),
        #     ],

        #     "key2": [
        #         (600, "height")
        #     ]
        # }

    def __init__(self):
        self.data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Since we are guaranteed that set will always be called with strictly increasing timestamps,
        # We just end up with an array of values for a given key, sorted by timestamp
        # Which means we never have to sort anything ourselves.. the order of timestamps for a given key comes for free
        self.data[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        # Now we have a list of all the values we had stored for that key
        values = self.data[key]

        # There are two ways that we could end up having nothing to return..
        # Either we never stored anything for this key at all, or we don't have any records that were stored before the requested timestamp
        if not values or values[0][0] > timestamp: return ""


        # At this point, we basically want to find all elements in the array that are less than or equal to our requested timestamp eg given [100, 200, 300, 400, 500, 600, 700, 800]
        # And we want to find everything before 600, technically we could do an O(n) but the constraints say that our get should not exceed O(logn)
        # So that should ring binary search!!
        # Now, lower bounds will be a bad idea here because we are not looking for the first value that meets our condition... 
        # Because if we use our first yes, that will be index 0. Doesn't really tell us anything useful. 
        # So we infact want our first "not yes" ie the first value that is bigger so that we know to start looking from just before it

        l, r = 0, len(values)
        while l < r:
            mid = l + (r-l)//2
            if values[mid][0] > timestamp:
                r = mid
            else:
                l = mid + 1
        
        # At this point l is at the first index that does not meet our requirement
        # Actually that will tell us the number of elements that meet our requirements 
        # ie if l landed at index 6, there's actually 6 elements behind index 6 since the array is 0 indexed

        return values[l - 1][1]
