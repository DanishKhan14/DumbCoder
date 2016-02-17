    # Reconstruct BT from Inorder and Postorder

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # Method 1: Recursive
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root

        # Method 2: Recursive
        """
        use inddict, a dictionary of val:index in inorder, to reduce the runtime.
        Geting an item in a dictionary is O(1), but list.index() is O(n)
        use index pointers Lin, Rin for inorder instead of slicing
        """
        def helper(Lin, Rin):
            if Lin < Rin:
                root = TreeNode(postorder.pop(-1))
                rootind = inddict[root.val]
                root.right = helper(rootind+1, Rin)
                root.left  = helper(Lin, rootind)
                return root
        inddict = {val:i for i, val in enumerate(inorder)}
        return helper(0, len(inorder))


    # Iterative

