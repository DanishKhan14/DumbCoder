#!/usr/bin/python

    # Iterative
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or (root.left is None and root.right is None):
            return True
        isBST = True
        cur = root
        self.val = None
        import Queue
        q = Queue.LifoQueue()
        while(cur or not q.empty()):
            if cur:
                q.put(cur)
                cur = cur.left
            else:
                cur = q.get()
                if self.val >= cur.val:
                    isBST = False
                self.val = cur.val
                cur = cur.right
        return isBST

    # Recursive

    # same thing as above. Recursive in order traversal
