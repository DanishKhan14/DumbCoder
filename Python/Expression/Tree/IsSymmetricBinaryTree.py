#!/usr/bin/python

    # Method 1: Recursive

    def (self, root):
        """

        :param self:
        :param root:
        :return:
        """
        if root is None:
            return True
        return self.isMirror()

    def isMirror(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)

    # Method 2: Iterative

    def (self, root):
        """

        :param self:
        :param root:
        :return:
        """
        if root is None:
            return True

        q = [(root.left, root.right)]
        while q:
            n1, n2 = q.pop(0)
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            q.append((n1.left, n2.right))
            q.append((n1.right, n2.left))
        return True