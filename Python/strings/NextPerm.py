    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        This algo I found from Wikipedia:

        1) Find the largest index k such that nums[k] < nums[k + 1].
        If no such index exists, the permutation is sorted in descending order, just reverse it to ascending order
        and we are done. For example, the next permutation of [3, 2, 1] is [1, 2, 3].

        2) Find the largest index l greater than k such that nums[k] < nums[l].
        3) Swap the value of nums[k] with that of nums[l].
        4) Reverse the sequence from nums[k + 1] up to and including the final element nums[nums.size() - 1].
        """

        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1