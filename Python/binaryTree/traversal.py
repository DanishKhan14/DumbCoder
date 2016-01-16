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

    def maxDepth(self, root): #Recursion
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.mexDepth(root.right)) +1

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

    def minDepth(self, root):  # Recursive
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return 1 + self.minDepth(root.right)
        if root.right is None:
            return 1 + self.minDepth(root.left)
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def minDepth(self, root):



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

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ## Recursive Solution ##
        """
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        """
        ### Iterative Solution : DFS ###
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

    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res

    ##### Path Sum ######

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

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        if root is None:
            return 0
        res, total = [], 0
        self.dfs(root, "", res)
        for item in res:
            total += int(item)
        return total

    def dfs(self, root, path, res):
        if not root.left and not root.right:
            res.append(path+str(root.val))
        if root.left:
            self.dfs(root.left, path+str(root.val), res)
        if root.right:
            self.dfs(root.right, path+str(root.val), res)
        """
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