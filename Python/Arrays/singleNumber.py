"""
Given an array of integers, every element appears twice except for one. Find that single one.

"""
    # Method 1: XOR  O(n) time, O(1) space
    def singleNumber(self, nums):
        """

        known that A XOR A = 0 and the XOR operator is commutative,
        the solution will be very straightforward.

        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res

    # Method 2: O(n) time and space
    def singleNumber3(self, nums):
        return 2*sum(set(nums))-sum(nums)

    # Method 3: Same as 1 but with python syntactic sugar :)

    def singleNumber4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)