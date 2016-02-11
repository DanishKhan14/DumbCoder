"""
The inorder traversal of a BST is the nodes in ascending order. To find a successor,
you just need to find the smallest one that is larger than the given value since there
are no duplicate values in a BST. It just like the binary search in a sorted list.
The time complexity should be O(h) where h is the depth of the result node. succ is a
pointer that keeps the possible successor. Whenever you go left the current root is the new
possible successor, otherwise the it remains the same.

Only in a balanced BST O(h) = O(log n). In the worst case h can be as large as n.
"""



def inorderSuccessor(self, root, p):
    succ = None
    while root:
        if p.val < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ


# Recursive

def inorderSuccessor(self, root, p):
    if not root: return None
    if root.val>p.val: return self.inorderSuccessor(root.left,p) or root
    return self.inorderSuccessor(root.right,p)


# recursively, O(n) time
def inorderSuccessor1(self, root, p):
    res = []
    self.inOrder(root, res)
    for i, node in enumerate(res):
        if node == p:
            if i == len(res)-1:
                return None
            else:
                return res[i+1]

def inOrder(self, root, res):
    if root:
        self.inOrder(root.left, res)
        res.append(root)
        self.inOrder(root.right, res)

# recursively, O(k), k is the position of p
# in the inorder traversal order
def inorderSuccessor(self, root, p):
    res = []
    self.ret = None
    self.inOrder(root, res, p)
    return self.ret

def inOrder(self, root, res, p):
    if root:
        self.inOrder(root.left, res, p)
        res.append(root)
        if len(res) > 1 and res[-2] == p:
            self.ret = res[-1]
            return
        self.inOrder(root.right, res, p)

# iteratively, O(k)
def inorderSuccessor3(self, root, p):
    stack, res = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return
        node = stack.pop()
        res.append(node)
        if len(res) > 1 and res[-2] == p:
            return res[-1]
        root = node.right