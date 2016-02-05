# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l= 0
        for r in range(1,len(nums)):
            if nums[l] != nums[r]:
                l +=1
                nums[l] = nums[r]
        return l+1 if nums else 0

"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the
first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length

"""

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(1) space. But array needs to be sorted

        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

        # O(n) Space. But array need not be sorted

        l = 0
        map = {}
        for i,v in enumerate(nums):
            map[v] = 0
        for r,val in enumerate(nums):
            if map[val] < 2:
                map[val]+=1
                nums[l] = nums[r]
                l+=1
        return l if nums else 0