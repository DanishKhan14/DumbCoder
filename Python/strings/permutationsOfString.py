# Method 1: Using itertools

import itertools
itertools.permutations([1,2,3,4,5], 2)

# Same thing for combinations
print list(itertools.combinations('123', 2))

# Method 2: Backtracking
"""
As I'm swapping the content of the list it's required a mutable sequence type as input.
E.g. perm(list("ball")) will work and perm("ball") won't because you can't change a string.
"""

def perm(a,k=0):
   if(k==len(a)):
      print a
   else:
      for i in xrange(k,len(a)):
         a[k],a[i] = a[i],a[k]
         perm(a, k+1)
         a[k],a[i] = a[i],a[k]

perm([1,2,3])

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

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)