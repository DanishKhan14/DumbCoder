#!/usr/bin/python

    #Recursive

    def lowestCommonAncestor(self, root, p, q):
        """
        If the current (sub)tree contains both p and q,
        then the function result is their LCA. If only one of
        them is in that subtree, then the result is that one of them.
        If neither are in that subtree, the result is None

        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # escape condition
        if (not root) or (root == p) or (root == q):
            return root
        # search left and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            # both found, root is the LCA
            return root
        return left or right

    #Iterative

    def lowestCommonAncestor(self, root, p, q):
        """

        :param self:
        :param root:
        :param p:
        :param q:
        :return:
        """
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

