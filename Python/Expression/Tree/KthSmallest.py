    # Recursively
    def kthSmallest1(self, root, k):
        res = []
        self.inorder(root, res)
        return res[k-1]

    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)

    # Iteratively
    def kthSmallest(self, root, k):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res[k-1]
            node = stack.pop()
            res.append(node.val)
            root = node.right

"""
If we can modify tree structure: Check this example

https://leetcode.com/discuss/43464/what-if-you-could-modify-the-bst-nodes-structure
"""