    def majorityElement0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # two pass + dictionary
    def majorityElement1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for num in nums:
            if dic[num] > len(nums)//2:
                return num

    # one pass + dictionary
    def majorityElement2(self, nums):
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            if dic[num] > len(nums)//2:
                return num
            else:
                dic[num] += 1

    # TLE
    def majorityElement3(self, nums):
        for i in xrange(len(nums)):
            count = 0
            for j in xrange(len(nums)):
                if nums[j] == nums[i]:
                    count += 1
            if count > len(nums)//2:
                return nums[i]

    # Sorting
    def majorityElement4(self, nums):
        nums.sort()
        return nums[len(nums)//2]

    # Bit manipulation
    def majorityElement5(self, nums):
        bit = [0]*32
        for num in nums:
            for j in xrange(32):
                bit[j] += num >> j & 1
        res = 0
        for i, val in enumerate(bit):
            if val > len(nums)//2:
                # if the 31th bit if 1,
                # it means it's a negative number
                if i == 31:
                    res = -((1<<31)-res)
                else:
                    res |= 1 << i
        return res

    # Divide and Conquer: Recursive
    def majorityElement6(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        a = self.majorityElement(nums[:len(nums)//2])
        b = self.majorityElement(nums[len(nums)//2:])
        if a == b:
            return a
        return [b, a][nums.count(a) > len(nums)//2]

"""
Method 7: Moore's Voting Algorithm

Basic idea of the algorithm is if we cancel out each occurrence
of an element e with all the other elements that are different
from e then e will exist till end if it is a majority element.
Below code loops through each element and maintains a count of
the element that has the potential of being the majority element.
If next element is same then increments the count, otherwise decrements
the count. If the count reaches 0 then update the potential index to
the current element and sets count to 1

"""

    def majorityElement(self, nums):
        count, cand = 0, 0
        for num in nums:
            if num == cand:
                count += 1
            elif count == 0:
                cand, count = num, 1
            else:
                count -= 1
        return cand