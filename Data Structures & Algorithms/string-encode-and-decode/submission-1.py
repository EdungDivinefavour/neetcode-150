class Solution:
    # Okay I lied. It won't work for all cases.. It especially won't work for a case where
    # The length of the string is more than a single digit.
    # Eg assuming the string length is say 20, our previous algorithm won't work because
    # It will only pick the first char ie '2' once it encounters it, and it will use that to get the next length

    # We could instead, add some sort of delimeter after the length while encoding
    # So that we know when we have stopped reading the length..... 
    # Dang! I ended up needing the freakin delimeter : /
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        delim = "#"

        for s in strs:
            encoded = encoded + str(len(s)) + delim + s
        return encoded

    # And during decoding, we expect that we will be receiving a string that was encoded using our algorithm
    # Meaning the very first char will be the length of our first string
    # Buuuuuuuutttt... we have to know when we are done reading the string's length incase its a multiple digit number
    # So we can keep reading the encoded string until we hit our delimeter and then we can stop reading for length

    # At this point, we can just start our splicing of the encoded string from the char immediately after our first string's length
    # Down till the char at our starting position + its length
    # This should successfully give us our first string... And now that we have that, 
    # We know that if we simply jump our pointer to the index where we ended our last splice
    # We will get to the index of our next string's length counter
    # So we can just rinse and repeat till the end of our string
    def decode(self, s: str) -> List[str]:
        decoded = []
        delim = "#"
        
        p = 0
        lengthStr = ""

        while p < len(s):
            # If we are still reading the string length, keep adding it to the lengthStr variable
            if s[p].isdigit():
                lengthStr = lengthStr + s[p]
                p += 1 # Move p forward
                continue
            
            # If we are done reading the string length, this means we are at the delimeter
            if s[p] ==  delim:
                start = p + 1
                end = start + int(lengthStr)

                newString = s[start: end]
                decoded.append(newString)

                p = end
                lengthStr = ""
        
        return decoded


