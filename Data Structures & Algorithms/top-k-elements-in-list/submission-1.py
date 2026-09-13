class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # freq[i] = list of elements that appear exactly i times.
        # Size n+1 because a count can be anywhere from 0 to n, and we want
        # to index straight into it without any offset math.
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Flip the map inside out: instead of asking "how often is this element?"
        # we can now ask "which elements occur this often?"
        for num, cnt in count.items():
            freq[cnt].append(num)

        # The highest counts will be at the high indices, so walking backwards
        # visits elements in descending frequency order for free... We won't need to sort or even use a heap!.
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:  # Now we have our k, everything below is smaller
                    return result