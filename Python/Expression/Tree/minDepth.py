    #!/usr/bin/python

    def minDepth(self, root):  # Recursive
        """

        :param self:
        :param root:
        :return:
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth(self, root): #Iterative
        """
        Use Level Order Traversal or BFS
        :param self:
        :param root:
        :return:
        """
        depth, level = 0, [root]
        while level and level[0]:
            depth += 1
            temp = []
            for n in level:
                if not n.left and not n.right:
                    return depth
                temp.extend([kid for kid in (n.left, n.right) if kid])
            level = temp
        return depth