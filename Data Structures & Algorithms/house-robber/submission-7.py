
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Aside the Top Down approach we used in the earlier problem, we can take another DP approach called the Bottom Up approach!
        # So unlike in Top Down where we ask, from this big problem, how do we solve it by breaking it into smaller pieces, eating it one chunk at a time,
        # The Bottom Up approach asks "what is the smallest version of this problem?" if I solved that, will it lead me to the full solution?

        # Now, one important thing to note with Top Down vs Bottom Up is that... for Top Down, the one who passed the baton over to you needs you to have completed your own computation before he can complete his.
        # However in Bottom Up, by the time we get to a given problem, the smaller problems it depends on would have already been solved.
        # So we can simply take those previously computed results and use them to solve our current, bigger problem.
        # That's why it works by solving the smallest problem first, storing the results and using them to build the bigger ones...

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

        # Now here's another interesting optimization...
        # In our previous solution, we were storing the maximum profit from EVERY single house in a DP array.
        # But looking at our recurrence, do we actually need to remember all those results?

        # Think about it... when we're standing at house i, we only care about TWO previously computed answers.
        # The maximum profit starting from the house one step ahead of us (i+1),
        # And the maximum profit starting from the house two steps ahead of us (i+2).
        # Anything beyond those two has already been accounted for in their own maximum profits!
        # So instead of storing an entire DP array, we can simply keep these two values in variables.

        NUMS = len(nums)

        # Initially, imagine we're standing just beyond the last house.
        # There's nothing left to rob from there, so the maximum profit is obviously 0.
        # The same goes for two houses beyond the end... there's still nothing to rob.
        # So both of our starting values can simply be 0.
        oneHouseAhead, twoHousesAhead = 0, 0

        # Now we start from the very last house and work backwards.
        # At any given index i, oneHouseAhead represents the maximum money we can rob from i+1 onward,
        # While twoHousesAhead represents the maximum money we can rob from i+2 onward.
        # And since we're going backwards, both of those answers would have already been calculated.

        for i in range(NUMS - 1, -1, -1):
            # For every house, we have to choose whether we want to rob it or not...
            # If we choose to rob it, we collect nums[i] and add whatever maximum profit we can get from two houses ahead.
            # If we choose not to rob it, we collect nothing from this house and just take the maximum profit from one house ahead.
            # So we can simply take whichever choice gives us the bigger stash.

            # Temporarily store the maximum profit starting from our current house.
            temp = max(nums[i] + twoHousesAhead, oneHouseAhead)

            # Now here's the important part... we are about to move one house to the left.
            # So what used to be one house ahead of us will now be TWO houses ahead of us.
            # And the result we JUST calculated for our current house will now be ONE house ahead of us.
            # So we should shift our values to reflect that.
            twoHousesAhead = oneHouseAhead
            oneHouseAhead = temp

            # This way, when the next iteration begins, our two variables will already contain exactly the answers we need.
            # And we can keep doing this without having to remember the maximum profit from every single house.

        # By the time we reach index 0, oneHouseAhead will contain the maximum money we can rob from the ENTIRE array.
        # Remember that this result already considers BOTH robbing and skipping the first house.
        # So there is no need to compare it using something like max(oneHouseAhead, twoHousesAhead).
        return oneHouseAhead

        # And the nice thing about this approach is that we still visit every house only once, giving us O(n) time.
        # But instead of storing an entire DP array, we only kept the two previously computed results and a temporary variable.
        # So our extra space is now O(1)!
