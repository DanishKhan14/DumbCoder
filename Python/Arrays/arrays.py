#!/usr/bin/python


### Rotate Array ###

def rotate(nums, k):
    nums[:] = nums[len(nums) - k:] + [:len(nums) -k]

### Method 2 ######

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        k%=len(nums)
        nums.reverse()
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)


    def reverse(self,nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
