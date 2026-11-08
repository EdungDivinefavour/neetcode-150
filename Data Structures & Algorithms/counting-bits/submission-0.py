class Solution:
    def countBits(self, n: int) -> List[int]:
        # Using the inbuilt library for converting to binary really helps us to cut down on some code
        # Except a question explicitly asks not to use the inbuild library, I don't see why not! Seeing as we use inbuilt sort for sorting, inbuilt add for adding etc etc

        # So for every number in our range, we can just convert it to binary and count the 1s in it

        out = []
        # We are doing n+1 because the question asks us to do it for every number in range [0, n] ie including n
        for i in range(n+1): 
            binary = str(bin(i))
            out.append(binary.count("1"))

        return out