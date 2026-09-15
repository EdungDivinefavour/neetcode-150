class Solution:
    # I think there is a way to do this without using any super special delimeter
    # If during encoding, we simply take store each strings length right before it
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + s
        return encoded

    # And during decoding, we expect that we will be receiving a string that was encoded using our algorithm
    # Meaning the very first char will be the length of our first string
    # So we can just start our splicing of the encoded string from the char immediately after our first string's length
    # Down till the char at our starting position + its length 
    # This should successfully give us our first string... And now that we have that, 
    # We know that if we simply move our pointer to the index where we ended our last splice
    # We will get to the index of our next string's length counter
    # So we can just rinse and repeat till the end of our string
    def decode(self, s: str) -> List[str]:
        decoded = []
        p = 0

        while p < len(s):
            start = p + 1
            end = start + int(s[p])

            newString = s[start: end]
            decoded.append(newString)

            p = end
        
        return decoded