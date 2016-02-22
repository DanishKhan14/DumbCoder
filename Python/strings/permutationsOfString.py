# Method 1: Using itertools

import itertools
itertools.permutations([1,2,3,4,5], 2)

# Same thing for combinations
print list(itertools.combinations('123', 2))
"""
# Method 2: Backtracking
"""
As I'm swapping the content of the list it's required a mutable sequence type as input.
E.g. perm(list("ball")) will work and perm("ball") won't because you can't change a string.


def perm(a,k=0):
   if(k==len(a)):
      print a
   else:
      for i in xrange(k,len(a)):
         a[k],a[i] = a[i],a[k]
         perm(a, k+1)
         a[k],a[i] = a[i],a[k]

perm([1,2,3,4])


# Method 3: Iterative. Implemented as a generator

def permute_in_place(a):
    a.sort()
    yield list(a)

    if len(a) <= 1:
        return

    first = 0
    last = len(a)
    while 1:
        i = last - 1

        while 1:
            i = i - 1
            if a[i] < a[i+1]:
                j = last - 1
                while not (a[i] < a[j]):
                    j = j - 1
                a[i], a[j] = a[j], a[i] # swap the values
                r = a[i+1:last]
                r.reverse()
                a[i+1:last] = r
                yield list(a)
                break
            if i == first:
                a.reverse()
                return

if __name__ == '__main__':
    for n in range(5):
        for a in permute_in_place(range(1, n+1)):
            print a
        print

    for a in permute_in_place([0, 0, 1, 1, 1]):
        print a
    print

# Method 3: DFS Recursive

def permute(nums):

    res = []
    dfs(nums, [], res)
    return res

def dfs(nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    #print nums
    for i in xrange(len(nums)):
        print path
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

p = permute([1,2,3,4])
print p

# Method 4: Next Permutation

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


# Method 5: Another solution for perms with duplicates

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for n in nums:
            temp = []
            for item in ret:
                for i in xrange(len(item) + 1):
                    temp += item[:i] + [n] + item[i:],
                    if i < len(item) and item[i] == n:
                        break
            ret = temp
        return ret if any(ret) else []