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