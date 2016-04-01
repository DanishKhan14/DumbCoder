#!/usr/bin/python


# Method 1: Recursion

def maxDepth(self, root):
    if root is None:
        return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Method 2: No Recursion

def maxDepth(self, root):

    if root is None:
        return 0
    max = 0
    depth = 0
    stack = [(root, depth)]
    while stack:
        node, depth = stack.pop()
        max = max if max > depth else depth
        if node.left:
            stack.append((node.left, depth+1))
        if node.right:
            stack.append((node.right, depth +1))
    retrun max


