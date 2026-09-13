class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # "Top K" is a question about counts, so before we can rank anything we need
        # the count of each element, and a map gives us that in one pass
        A = {}
        for num in nums: 
            A[num] = 1 + A.get(num, 0)
        
        # There are several ways we can go from here...
        # A not so efficient way to do this would be

        # To store every value/key pair as a tuple so we can then sort the list of tuples
        # We are not storing it as key/value and are instead using value/key because of how a tuple sorts:
        # a tuple sorts by x and only looks at y if there is a tie in x
        # So putting the count first means the sort ranks by count, which is the ranking we want

        pairs = [(value, key) for key, value in A.items()] # Create value/key pairs from our hashmap
        pairs = sorted(pairs)   # Sorting ascending means the biggest counts pile up at the end

        result = [el[1] for el in pairs[-k:]]  # So the last k tuples are the k most frequent, and we only want the element from each, not its count

        return result