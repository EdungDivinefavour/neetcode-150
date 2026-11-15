
class Solution:
    def rob(self, nums: List[int]) -> int:
        NUMS = len(nums)
        memo = {}

        # So for this question, just like in robber 1, at each house we are still asking the same question of whether we should rob a house or not.
        # But there's one important difference... the houses are now arranged in a circle! Which means that the very last house is now adjacent to the very first house.
        # So if we robbed the first house, we can't rob the last house and vice versa.

        # We can still use our Top Down recursive approach from House Robber 1...
        # Where we decide whether to rob the current house or skip it, and let recursion handle the remaining houses.
        # But this time, we need to somehow remember whether we've already robbed a house that would prevent us from robbing the current one.


        def decideWhetherToRobHouseAtIndex(index, robbed):
            # Now here's something interesting about memoization in this problem...
            # Recall that in House Robber 1, we could simply use index as our memo key.
            # Because the maximum money we could rob from a given index would never change regardless of how we got there.

            # But is that still true here? Not exactly...
            # Imagine we reach the very last house through two different paths.
            # In one path, we robbed the very first house... so we're NOT allowed to rob the last house.
            # But in another path, we didn't rob the first house... so we ARE allowed to rob the last house.
            # Both paths have the same index, but the maximum money we can rob from that position could be different!

            # So using just index as our memo key would be wrong because we'd be treating those two different situations as the same subproblem.

            # Now you might think we need to store the entire robbed set in our memo key...
            # But think about it... do we actually care about every single house we've robbed?

            # Not really! Because our index+2 jump already takes care of preventing us from robbing adjacent houses.
            # The only additional thing we need to remember is whether we robbed the FIRST house.
            # Because that's the only earlier decision that can affect whether we're allowed to rob the LAST house.

            # So our memo key can simply be the current index and whether house 0 has been robbed.
            # This way, two calls to the same index with different first-house decisions won't accidentally share the same answer.
            key = (index, 0 in robbed)

            # If we have already calculated the maximum profit for this exact situation...
            # We can simply return it instead of exploring the same decisions again.
            if key in memo: return memo[key]

            # If we have gone past the last house, there's nothing left to rob.
            if index >= NUMS: return 0

            # If we choose to rob it, we can take it and whatever we can compute from i+2 onwards
            # If we don't rob it, we can just pass the baton over to the next thing we are allowed to rob
            robMe = 0

            # Before we decide to rob this house though... we need to make sure we're actually allowed to rob it.
            # Normally our index+2 jump already handles this, but because the houses form a circle,
            # We also need to check whether the house AFTER us (wrapping around the circle) has already been robbed.
            # The modulo operation is important because when we are standing at the last house,
            # (index+1) % NUMS will bring us back to index 0, ie the very first house.
            # So if we robbed the first house, this check will prevent us from robbing the last one.
            canRobMe = ((index+1) % NUMS) not in robbed

            if canRobMe:
                # Okay... assuming we're allowed to rob this house, let's explore what happens if we do.
                # We first add the current house to our robbed set so that the future recursive call will know that we robbed it.
                robbed.add(index)

                # We collect the money from this house and pass the baton two houses forward.
                # Because we obviously can't rob the house immediately after this one.
                robMe = nums[index] + decideWhetherToRobHouseAtIndex(index+2, robbed)

                # Now that we have explored this decision, we need to undo it!
                # Remember that we're about to explore a completely different possibility where we DON'T rob this house.
                # So we cannot let the decisions from our previous branch affect that one.
                # This is our backtracking step.
                robbed.remove(index)

            # Now let's explore the other possibility... what if we DON'T rob this house?
            # We collect nothing from it, so we can simply pass the baton to the next house.
            dontRobMe = decideWhetherToRobHouseAtIndex(index+1, robbed)

            # So now that we've explored both possibilities, we can just take whichever gives us the bigger stash.
            res = max(robMe, dontRobMe)

            # And since we have now computed the maximum profit for this exact state, we can store it in our memo so we never have to calculate it again.
            memo[key] = res
            return memo[key]

        # Start from the first house with an empty robbed set because we haven't robbed anything yet.
        # And let recursion figure out the maximum money we can rob while respecting the circular constraint.
        # Since each index can only have two memoization states (first house robbed or not robbed),
        # We only have O(n) possible states, giving us O(n) time and O(n) space.
        return decideWhetherToRobHouseAtIndex(0, set())
