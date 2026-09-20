class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # When searching for an element in an array, you might think to go through every single element until you find your desired element
        # If our array is 'sorted' eg [1,2,3,4,5,6,7....1000000], and we are looking for say the number 999999
        # Does it make sense to search all the way from 1? Nope
        # We can just ignore the elements that are not relevant
        # Think about a physical dictionary.. How do you search for a word?.
        # You open some page... and if your desired word comes before the page you landed on, you simply discard everything after the page you landed on
        # And if your desired word comes after the page you landed on, you simply discard everything before the page you landed on
        # How many times do you repeat this process? Well you can simply keep doing it until you find your desired word
        # We can do the same with our array

        l, r = 0, len(nums)

        # We will repeat this till we find our result.. 
        while l < r:
            mid = l + (r - l)//2
            
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                # If its neither bigger nor smaller, we have just found our target
                return mid

        return -1