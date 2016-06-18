#!/usr/bin/python

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """

        l = []
        visited = None
        if root is None:
            return l
        if root.left is None and root.right is None:
            l.append(root.val)
            return l
        q = []
        while (root or len(q)>0):
            if root:
                q.append(root)
                root = root.left
            else:
                root = q.pop()
                if root.right is None or root.right == visited:
                    l.append(root.val)
                    visited = root
                if not root == visited:
                    q.append(root)
                root = root.right
        return l
    """
        p = root
        l, stack = [], []
        while p or len(stack)>0:
            if p:
                stack.append(p)
                l.insert(0,p.val)
                p = p.right
            else:
                node = stack.pop()
                p = node.left
        return l


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(5)

n3.left = None
n3.right = n1
n1.left = n2
n1.right = None


s = Solution()
res = s.postorderTraversal(n3)
print res
