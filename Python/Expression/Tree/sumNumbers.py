#!/usr/bin/python


    def sumNumbers(self, root):
        """

        Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

        An example is the root-to-leaf path 1->2->3 which represents the number 123.

        Find the total sum of all root-to-leaf numbers.

        :type root: TreeNode
        :rtype: int
        """
    # Recursive

        if root is None:
            return 0
        self.res= 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, sum):
        if not root.left and not root.right:
            self.res += sum*10 + root.val
        if root.left:
            self.dfs(root.left, sum*10+root.val)
        if root.right:
            self.dfs(root.right, sum*10+root.val)

    # Iterative