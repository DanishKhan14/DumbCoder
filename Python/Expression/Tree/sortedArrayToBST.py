#!/usr/bin/python

    # Recursive

    def sortedArrayToBST(self, nums):
        if nums:
            mid = len(nums)/2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root


    # Iterative

