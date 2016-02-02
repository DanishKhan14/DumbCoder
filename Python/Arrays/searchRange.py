"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Method 1: Naive O(n) time and space
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return [-1,-1] if len(res)==0 else [res[0],res[-1]]

        # Method 2: O(log n) time
        left = bisect.bisect_left(nums, target)
        if left >= len(nums) or nums[left] != target:
            left = -1

        right = bisect.bisect_right(nums, target) - 1
        if right < 0 or nums[right] != target:
            right = -1

        return [left, right]