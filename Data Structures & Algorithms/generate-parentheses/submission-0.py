class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # At every position in the string we only have two choices.. we either put an open bracket or a closing one
        # The only thing that makes it interesting is that not every string we can build is actually valid,
        # so we need some way to throw away the bad ones before we waste time going deeper down them

        output = []
        def dfs(opens, closes, acc):
            # Two ways we can already know this path is invalid..
            # If we have closed more than we have opened then we have a ")" and nothing we add later can fix that
            # And if we have opened more than n then we have already used up more brackets than we are allowed to
            if opens < closes or opens > n: return

            if len(acc) == n*2:
                # By the time we have a string the length of a pair ie 2n, we either have a valid set of opens and closes or not... If we do, we can add it to the array, if not we can ignore this path
                if opens == closes: 
                    output.append(acc)
                return
            
            # Explore the path where we put an open bracket, then the path where we put a closing one
            dfs(opens+1, closes, acc+"(")
            dfs(opens, closes+1, acc+")")

        dfs(0, 0, "")
        return output