class Solution:
    def rob(self, nums: List[int]) -> int:
        # Aside the Top Down approach we used in the earlier problem, we can take another DP approach called the Bottom Up approach!
        # So unlike in Top Down where we ask, from this big problem, how do we solve it by breaking it into smaller pieces, eating it one chunk at a time,
        # The Bottom Up approach asks "what is the smallest version of this problem?" if I solved that, will it lead me to the full solution?

        # Now, one important thing to note with Top Down vs Bottom Up is that... for Top Down, the one who passed the baton over to you needs you to have completed your own computation before he can complete his.
        # However in Bottom Up, by the time we get to a given problem, the smaller problems it depends on would have already been solved.
        # So we can simply take those previously computed results and use them to solve our current, bigger problem.
        # That's why it works by solving the smallest problem first, storing the result in dp and using that to build the bigger ones...

        # Also, something interesting I realized about how we can think of our decisions in general...
        # Recall that in our original solution, when standing at a given house, we were using a for loop to explore EVERY possible house we could rob next.
        # But do we really need to explicitly consider every possible next house like that?

        # What if instead, we simply asked... "Will my optimal solution include the house I'm currently standing on or not?"
        # Think about it... for any given house, there are only two possibilities. Either we rob it, or we don't.
        # And EVERY possible valid combination of houses must belong to one of those two groups.
        # So rather than deciding WHICH house to rob next, we can just decide what to do with THIS house and let the remaining problem handle the rest.

        # If we rob this house, then we collect its money but are forced to skip the next house.
        # If we don't rob this house, then we collect nothing from it, but we're free to consider the very next house.
        # So we can compare the maximum profit from these two choices... and whichever is bigger becomes our answer for this position.

        # Now with that idea in mind... how do we approach this from Bottom Up?
        # Well given [2, 9, 8, 7, 6], let's imagine we only had the very last house to consider.
        # We can either rob it and get 6, or skip it and get 0... so obviously our max is 6.

        # Okay, now what if we had the last TWO houses instead? ie [7, 6]
        # We can either rob 7 and skip 6, or skip 7 and take the best result we already calculated for 6.
        # So our answer is simply the max of those two possibilities.

        # Now what if we had the last THREE houses? ie [8, 7, 6]
        # Again, we have the same two choices... rob 8 and take whatever maximum we can get from 6 onward,
        # Or skip 8 and take whatever maximum we already calculated from 7 onward.
        # And the nice thing is... we would have already computed those smaller answers!

        # So we can just keep repeating this process, moving backwards and building bigger and bigger solutions
        # Until we eventually reach the first house... at which point we would have solved the entire problem.

        NUMS = len(nums)
        dp = [0] * NUMS

        # dp[i] represents the maximum money we can rob considering all the houses from index i to the end.
        # And since we're starting from the end, the smaller problems we need will already be calculated by the time we reach them.
        for i in range(NUMS - 1, -1, -1):

            # For the last house, the max would obviously be gotten by robbing it : )
            if i == NUMS - 1:
                dp[i] = nums[-1]

            # For the second last house, because we can't rob two adjacent houses, we would have to choose between it and the last house
            elif i == NUMS - 2:
                dp[i] = max(nums[-1], nums[-2])

            # For every other house, we have to choose whether we want to rob it or not...
            # If we choose to rob it, then the max we can get from there will be itself + whatever we get from the one at i+2.
            # If we choose to not rob it, then we got nothing so the max we can get from there will be just whatever we had at i+1.
            # And since we've already calculated both of those smaller problems, we can simply take whichever gives us the bigger stash.
            else:
                dp[i] = max(
                    nums[i] + dp[i+2],
                    dp[i+1]
                )

        # By the time we reach index 0, dp[0] already considers BOTH robbing and skipping the first house.
        # So it represents the maximum money we can rob from the entire array.
        return dp[0]
