    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1: DP   O(n) space

        for i in xrange(1,len(nums)):
            nums[i]=max(nums[i], nums[i]+nums[i-1])
        return max(nums)

        # Method 2: DP O(1) space

        if not nums:
            return None
        loc = glo= nums[0]
        for i in xrange(1, len(nums)):
            loc = max(loc+nums[i], nums[i])
            glo = max(loc, glo)
        return glo


        # Method 2: Greedy

        current = 0
        result = nums[0]
        for i in nums:
            current += i
            result = max(current,result)
            current = max(0,current)
        return result