class Solution:
    # I am very suspicious of this approach because the constraints already tell us that the length is small so this likely requires brute force but I still can't come up with a case that will fail yet.
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # So the first thing that comes to mind here is to store all the words in a dictionary.. then we can go through the string, and the moment we find a word that is in our dictionary, we cut it off and start looking for the next word
        # If we get to the end of the string having cut it up perfectly, then we would be able to build the string from the words in the dictionary : )

        # We want to use a set so that checking if a piece of the string is a word will be O(1)
        words = set(wordDict)

        # Let's use l and r to mark the start and end of the combo we are currently looking at
        l, r = 0, 0

        while r < len(s):
            # If the combo we have so far is a word, we can cut it here and start looking for the next word from the very next character
            if s[l:r + 1] in words:
                l = r + 1
                r = l
            # If it is not a word yet, we stretch the piece by one more character and try again
            else:
                r += 1

        # If we cut the string perfectly, we would have moved l all the way to the end
        # If we got stuck on a piece that never became a word, l would still be somewhere before the end
        return l == len(s)