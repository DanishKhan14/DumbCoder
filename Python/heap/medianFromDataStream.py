#!/usr/bin/python

from heapq import *

class MedianFinder:
    """
    - The length of smaller half is kept to be n / 2 at all time
    length of the larger half is either n / 2 or n / 2 depend on n

    - push the new number into small and pop the maximum item from
    small then push it into large.

    - add operation is O(logn), The findMedian operation is O(1)
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap


    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))


    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


# MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()