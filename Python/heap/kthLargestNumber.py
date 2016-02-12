class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        # Method 1: O(k+(n-k)lgk) time, min-heap
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in xrange(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
        """

        # Method 2   O(nlogk)
        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            else:
                heapq.heappushpop(h, n)
        return h[0]