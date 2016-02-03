"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.
"""

    def search(self, nums, target):
        """

        1) Find middle point mid = (l + h)/2
        2) If key is present at middle point, return mid.
        3) Else If arr[l..mid] is sorted
            a) If key to be searched lies in range from arr[l]
               to arr[mid], recur for arr[l..mid].
            b) Else recur for arr[mid+1..r]
        4) Else (arr[mid+1..r] must be sorted)
            a) If key to be searched lies in range from arr[mid+1]
               to arr[r], recur for arr[mid+1..r].
            b) Else recur for arr[l..mid]

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

# Recursive Method:

    def search(self, nums, target):
        if not nums:
            return -1
        return self.binarySearch(nums, target, 0, len(nums)-1)

    def binarySearch(self, nums, target, start, end):
        if end < start:
            return -1
        mid = (start+end)/2
        if nums[mid] == target:
            return mid
        if nums[start] <= target < nums[mid]: # left side is sorted and has target
            return self.binarySearch(nums, target, start, mid-1)
        elif nums[mid] < target <= nums[end]: # right side is sorted and has target
            return self.binarySearch(nums, target, mid+1, end)
        elif nums[mid] > nums[end]: # right side is pivoted
            return self.binarySearch(nums, target, mid+1, end)
        else: # left side is pivoted
            return self.binarySearch(nums, target, start, mid-1)


    # If Duplicates are there

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False