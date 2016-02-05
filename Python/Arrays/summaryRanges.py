"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res, i, start = [], 0, 0
        while i < len(nums)-1:
            if nums[i]+1 != nums[i+1]:
                res.append(self.printRange(nums[start], nums[i]))
                start = i+1
            i += 1
        res.append(self.printRange(nums[start], nums[i]))
        return res

    def printRange(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)