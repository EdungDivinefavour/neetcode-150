class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded, delim = "", "$"

        for s in strs:
            encoded += str(len(s)) + delim + s
        
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        delim = "$"
        p = 0
        lenStr = ""
    
        while p < len(s):
            if s[p].isnumeric():
                lenStr += s[p]
                p += 1
            
            elif s[p] == delim:
                p += 1
                decoded.append(s[p : p + int(lenStr)])
                p += int(lenStr)
                lenStr = ""
        
        return decoded
