class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # At every position in the string we only have two choices.. we either put an open bracket or a closing one
        # The only thing that makes it interesting is that not every string we can build is actually valid,
        # so we need some way to throw away the bad ones before we waste time going deeper down them

        output = []
        def dfs(opens, closes, acc):
            if len(acc) == n*2:
                # By the time we have a string the length of a pair ie 2n, we would have a valid combination of parenthesis
                # Unlike the last solution where we had to check here for if it was valid or not, in this solution we never even built an invalid combination to start with
                output.append(acc)
                return
            

            # There is some cleanup we can do to our previous solution.. ie
            # We can just not bother calling dfs on an invalid path eg.. 
            # If we have fully exhausted our opens there is no need to bother calling it.. so we only call when we still have some opens to use
            if opens < n:
                # Explore the path where we put an open bracket
                dfs(opens+1, closes, acc+"(")
            
            # If we still have valid closes.. ie we have some opens that are still waiting to be closed
            if closes < opens:
                # Explore the path where we put a closing
                dfs(opens, closes+1, acc+")")

        dfs(0, 0, "")
        return output