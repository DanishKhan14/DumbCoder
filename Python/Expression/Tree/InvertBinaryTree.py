#!/usr/bin/python


    # Method 1: No recursion , BFS

    def invert_bfs(self, root):
        """

        :param self:
        :param root:
        :return:
        """
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

    # Method 2: No recursion, DFS

    def invert_dfs(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend[(node.left, node.right)]
        return root

    # Method 3: Recursion

    def invert(self, root):
        if root is None:
            return None
        self.invert(root.left)
        self.invert(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp

        return root