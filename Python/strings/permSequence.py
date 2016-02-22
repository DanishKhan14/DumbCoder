"""
The set [1,2,3,…,n] contains a total of n! unique permutations.
Given n and k, return the kth permutation sequence.
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        """
        For permutations of n, the first (n-1)! permutations start with 1,
        next (n-1)! ones start with 2, ... and so on. And in each group of (n-1)! permutations,
        the first (n-2)! permutations start with the smallest remaining number, ...
        """

        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation