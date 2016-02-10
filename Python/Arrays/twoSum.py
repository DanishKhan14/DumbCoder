    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Method 1: Using HashMaps

        Do following for each element A[i] in A[]
       (a)	If M[x - A[i]] is set then print the pair (A[i], x - A[i])
       (b)	Set M[A[i]]

        """

        index = {}
        for i, x in enumerate(nums):
            if target - x in index:
                return [index[target - x] + 1, i + 1]
            index[x] = i

        """
        Method 2: Sorting
        1) Sort the array in non-decreasing order.
        2) Initialize two index variables to find the candidate
           elements in the sorted array.
               (a) Initialize first to the leftmost index: l = 0
               (b) Initialize second  the rightmost index:  r = ar_size-1
        3) Loop while l < r.
               (a) If (A[l] + A[r] == sum)  then return 1
               (b) Else if( A[l] + A[r] <  sum )  then l++
               (c) Else r--
        4) No candidates in whole array - return 0
        """

########################
# If given array is sorted"
########################

    # two-pointer
    def twoSum1(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

    # dictionary
    def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

    # binary search
    def twoSum(self, numbers, target):
        for i in xrange(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1