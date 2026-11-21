class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # There is a problem with our last solution in the sense that our memoization key was waay to specific
        # So it works but it is not a very efficient approach to take

        # We were trying to solve top down but we had a rather sneaky bad decision that led to our consfusion...
        # You see when we are trying to break the big problem into smaller problems with recursion, we always have to ask... 
        # Do we want the smaller problem to know about the decision of the bigger problem? Or should the smaller problem only care about what is specific to itself and then just pass its result over to the biiger problem
        # That right there was our mistake... We were trying to pass the total so far to the smaller problem.. But think about it.. Should the smaller problem really care about the bigger problem computed so far?
        # The answer is no!. It should only care about the minimum ways from right where its standing.. compute that, and pass the result over to the bigger problem

        # This does not mean that we won't pass any info down to the smaller problem. It just means that we are changing what we are passing to the smaller problem
        # ie instead of passing what we computed so far(which is kinda irrelevant to the small problem).. we can just say "Small problem, here is the problem you have to solve ie what is left for it to figure out"

        COINS = len(coins)
        memo = {}

        def minCoinsNeededFromIndex(i, target):
            # If we have ever computed the minimum needed to form this total from this given index, we don't need to do it again.. we can just return
            if (i, target) in memo: return memo[(i, target)]

            # If our target is 0, we have successfully formed the required amount, so we don't need any additional coins
            if target == 0: return 0

            # If we ever hit an unreachable target or we have gone through all our available coin options, there is no value in this path
            if target < 0 or i == COINS: return float('inf')
            
            # At every index, we can either use it again.. and pass the baton back to it
            # What does it mean to use me?.. well, we just count that we have used this coin.. and then pass the new target which will be total needed so far - me.. since the next problem will need to solve a smaller thing
            useMeAgain = 1 + minCoinsNeededFromIndex(i, target - coins[i])

            # Or not use it and pass the baton over to the next guy to make his own decisions
            # What does it mean to not use me?.. in this case we just pass the baton over and we still have the same target to hit
            dontUseMeAgain = minCoinsNeededFromIndex(i+1, target)

            # At this point we want to return whichever is smaller betweeen the decision to use me again or not use me again
            result = min(useMeAgain, dontUseMeAgain)
            memo[(i, target)] = result

            return memo[(i, target)]

        # If we cannot form the target amount from the array of coins we have available, the base case will hit +inf, so we can just return -1
        result = minCoinsNeededFromIndex(0, amount)
        return -1 if result == float('inf') else result