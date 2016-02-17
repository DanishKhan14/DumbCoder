class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nextVal = None
        self.stack = []
        self.root = root

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        else:
            if not self.stack:
                return False
            temp = self.stack.pop()
            self.nextVal = temp.val
            self.root = temp.right
        return True

    def next(self):
        """
        :rtype: int
        """
        return self.nextVal