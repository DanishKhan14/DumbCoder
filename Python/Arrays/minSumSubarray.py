"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a subarray of which the sum ≥ s.
If there isn't one, return 0 instead.
For example, given the array [2,3,1,2,4,3] and s = 7, return 2 for  [4,3]
"""


    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time
        left = sum = 0
        res = len(nums) +1
        for right, val in enumerate(nums):
            sum += val
            while sum >= s:
                res = min(res, right -left +1)
                sum -= nums[left]
                left += 1
        return res if res <=len(nums) else 0