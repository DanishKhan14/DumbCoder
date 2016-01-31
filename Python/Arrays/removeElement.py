    # Method 1: Very Pythonic

    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        try:
            while True:
                nums.remove(val)
        except:
            return len(nums)

    # Method 2: More efficient

    def removeElement(self, nums, val):
        """
        It scans numbers from the left to the right, one by one.
        Once it finds a number that equals to elem, it swaps current
        element with the last element in the array and then dispose the last.
        """
        i = 0
        n = len(nums)
        while (i < n):
            if nums[i] == val:
                nums[i] = nums[n -1]
                n-=1
            else:
                i+=1
        return n

    # Method 3: Best

    def removeElement3(self, nums, val):
        if not nums: return 0
        A = 0
        for n in nums:
            if n != val:
                nums[A] = n
                A += 1
        return A