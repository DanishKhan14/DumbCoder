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

###########################################################

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

###########################################################

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

        # Another Method: Same as Pelar

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

###########################################################

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

###########################################################

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

###########################################################

    def maxDepth(self, root): #Recursion
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) +1

    def maxDepthIter(self, root): #Iteration
        if root == None:
            return 0
        nodeStack = [root];
        depthStack = [1];
        maxDepth = 0;
        while len(nodeStack)>0:
            node = nodeStack.pop();
            depth = depthStack.pop();
            maxDepth = maxDepth if maxDepth > depth else depth
            if node.left != None:
                nodeStack.append(node.left)
                depthStack.append(depth+1)
            if node.right != None:
                nodeStack.append(node.right)
                depthStack.append(depth+1)
        return maxDepth

###########################################################

    def minDepth(self, root):  # Recursive
        """
        [1] has minDepth as 1
        [1,#,2] has minDepth as 2 and not 1
        [1,2,#] again has minDepth as 2

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
        Use Level Order Traversal or BFS. When hit with leaf first,
        return depth

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

###########################################################


    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


    # Iterative is Same tree

    # DFS with stack
    def isSameTree2(self, p, q):
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.right, node2.right))
                stack.append((node1.left, node2.left))
        return True

    # BFS with queue
    def isSameTree3(self, p, q):
        queue = [(p, q)]
        while queue:
            node1, node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True

###########################################################

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)

    # Method 2: Iterative

    def isSymmetric_BFS(self, root):
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

    def mirrorify(self, root):
        if root is None:
            return None
        cur = root
        self.mirrorify(cur.left)
        self.mirrorify(cur.right)
        temp = cur.left
        cur.left = cur.right
        cur.right = temp
        return root
###########################################################

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ## Recursive Solution ##

        if root is None:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


        ### Iterative Solution : DFS ###
    def hasPathSum2(self, root, sum):
        if root is None:
            return False
        rsum, node = [0], [root]
        while len(node) > 0:
            n = node.pop()
            s = rsum.pop() + n.val
            if n.left is None and n.right is None and s == sum:
                return True
            if n.left is not None:
                node.append(n.left)
                rsum.append(s)
            if n.right is not None:
                node.append(n.right)
                rsum.append(s)
        return False

###########################################################

    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, ls+[root.val], res)

    def pathSum2(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val]+i for i in tmp]

    # BFS + queue
    def pathSum3(self, root, sum):
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res

    # DFS + stack I
    def pathSum4(self, root, sum):
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res

    # DFS + stack II
    def pathSum5(self, root, s):
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls+[curr.left.val]))
        return res

    ##### Path Sum Ends ####

###########################################################

    ##### Path Traversals ######

    # dfs + stack
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res

    # bfs + queue
    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                queue.append((node.left, ls+str(node.val)+"->"))
            if node.right:
                queue.append((node.right, ls+str(node.val)+"->"))
        return res

    # dfs recursively
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)

###########################################################

    def sumNumbers(self, root):
        """

        Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

        An example is the root-to-leaf path 1->2->3 which represents the number 123.

        Find the total sum of all root-to-leaf numbers.

        :type root: TreeNode
        :rtype: int
        """
        # Recursive

        if root is None:
            return 0
        self.res= 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, sum):
        if not root.left and not root.right:
            self.res += sum*10 + root.val
        if root.left:
            self.dfs(root.left, sum*10+root.val)
        if root.right:
            self.dfs(root.right, sum*10+root.val)

###########################################################


    def kthSmallest(self, root, sum):
        if not root.left and not root.right:

            self.res += sum*10 + root.val
        if root.left:
            self.dfs(root.left, sum*10+root.val)
        if root.right:
            self.dfs(root.right, sum*10+root.val)

        stack = [(root, False)]
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    # if visited is True, it means a "small" node is found
                    k -= 1
                    # if k == 0, it means k small nodes has been checked,
                    # the current node is the kth one
                    if k == 0:
                        return curr.val
                else:
                    # Add from right to left
                    stack.append((curr.right, False))
                    stack.append((curr, True))
                    stack.append((curr.left, False))


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


###########################################################

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
        To find the lowest common ancestor, we need to find where is p and q
        and a way to track their ancestors. A parent pointer for each node
        found is good for the job. After we found both p and q, we create
        a set of p's ancestors. Then we travel through q's ancestors, the first one
        appears in p's is our answer.

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

############################################################

    # Recursive

    def lowestCommonAncestor(self, root, p, q):
        """

        :param self:
        :param root:
        :param p:
        :param q:
        :return:
        """
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


    # Iterative

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right
            else:
                return root
        return None

################################################################

    # Recursive

    def sortedArrayToBST(self, nums):
        if nums:
            mid = len(nums)/2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root

    # Iterative

################################################################

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


