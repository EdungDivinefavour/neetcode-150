class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # So the array has n + 1 numbers in it, and every number is between 1 and n.. and there is exactly one number that appears more than once
        # The trick here is to stop seeing nums as an array, and start seeing it as a linked list
        # In the sense that every index points to the index nums[index].. so from index 0, we go to nums[0], then to nums[nums[0]] and so on
        # Now think about what a duplicate means in that picture.. if 2 different indices have the same value, then 2 different nodes are pointing to the same next node
        # And that can only happen if there is a cycle! The node that those 2 indices point to is the start of the cycle, and that is our duplicate
        # So the problem is now basically, find where the cycle starts in a linked list.. which is the classic Floyd's cycle detection
        # See https://github.com/EdungDivinefavour/neetcode-150/blob/master/Data%20Structures%20%26%20Algorithms/linked-list-cycle-detection/submission-0.py

        # We can start from 0 here because every value in nums is at least 1, so nothing really ever points back to index 0
        # Which means 0 can never be part of the cycle, so it is a safe place to start from
        slow, fast = 0, 0

        # Phase 1: Let's find out if there is a cycle and get inside of it
        # slow will move 1 step at a time and fast will move 2 steps at a time
        # Since there is always a cycle, fast will eventually meet slow and they will land on the same node somewhere inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        # Phase 2: Now that we are inside the cycle, we want to find where the cycle starts
        # Say it takes a steps to get from 0 to the start of the cycle, and slow and fast met b steps into the cycle, and the cycle is c nodes long
        # At the time they met, slow had travelled a + b steps and fast had travelled twice of that, 2(a + b)
        # The extra distance fast travelled is just full laps around the cycle, so a + b has to be a multiple of c
        # Which means if we are at the meeting point and move forward a more steps, we will have completed a full lap and landed exactly on the start of the cycle!
        # We don't know what a is, but we do know that walking from 0 also takes a steps to get to the start of the cycle
        # So we can put a second pointer at 0, and move both pointers 1 step at a time. Whenever they meet, that is the start of the cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: return slow