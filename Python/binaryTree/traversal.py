#!/usr/bin/python

"""
InOrder Traversal no recursion
"""

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        if root is None:
            return l
        if root.left is None and root.right is None:
            l.append(root.val)
            return l

        import Queue
        q = Queue.LifoQueue()
        cur = root
        while(cur is not None or not q.empty()):
            if cur:
                q.put(cur)
                cur = cur.left
            else:
                cur = q.get()
                l.append(cur.val)
                cur=cur.right
        return l

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        if root is None:
            return l
        if root.left is None and root.right is None:
            l.append(root.val)
            return l
        import Queue
        q = Queue.LifoQueue()
        cur = root
        while(cur or not q.empty()):
            if cur:
                q.put(cur)
                l.append(cur.val)
                cur = cur.left
            else:
                cur = q.get()
                cur = cur.right
        return l

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        # Chindi Method

        l = []
        visited = None
        if root is None:
            return l
        if root.left is None and root.right is None:
            l.append(root.val)
            return l
        import Queue
        q = Queue.LifoQueue()
        cur = root
        while (cur or not q.empty()):
            if cur:
                q.put(cur)
                cur = cur.left
            else:
                cur = q.get()
                if cur.right is None or cur.right == visited:
                    l.append(cur.val)
                    visited = cur
                if not cur == visited:
                    q.put(cur)
                cur = cur.right
        return l
        """

        """
        Pelar Method _/\_
        """
        ans, stack = [], [root]
        while stack:
            tmp = stack.pop()
            if tmp:
                ans.append(tmp.val)
                stack.append(tmp.left)
                stack.append(tmp.right)
        return ans[::-1]

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

    def isBalanced(self, root):
        if self.checkHeight(root) == -1:
            return False
        else:
            return True

    def checkHeight(self, root):
        if root == None:
            return 0
        leftHeight = self.checkHeight(root.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.checkHeight(root.right)
        if rightHeight == -1:
            return -1
        diffHeight = abs(leftHeight - rightHeight)
        if diffHeight > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1