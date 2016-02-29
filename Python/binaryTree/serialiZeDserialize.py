# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

############### Method 1: Iterative BFS

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret = []
        queue = [root]

        while queue:
            if queue.count(None) == len(queue): # when only None is left
                break
            node = queue.pop(0)
            if node == None:
                ret.append('#')
            else:
                nxtLeft = node.left if node.left else None
                nxtRight = node.right if node.right else None
                queue += [nxtLeft, nxtRight]
                ret.append('%d' % node.val)

        return ','.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')

        queue = [TreeNode( int(data.pop(0)) )]
        root = queue[-1]
        left = True
        while data:
            nxt = data.pop(0)
            node = None if nxt == '#' else TreeNode( int(nxt) )
            if node:
                queue.append(node)
            if left:
                queue[0].left = node
            else:
                queue[0].right = node
                queue.pop(0)
            left = not left

        return root


############## Method 2: Using Recursion. Preorder




############# Method 3:  Tuple + Json .... Different Approach from BFS
    import json

    def serialize(self, root):
        def tuplify(root):
            return root and (root.val, tuplify(root.left), tuplify(root.right))
        return json.dumps(tuplify(root))

    def deserialize(self, data):
        def detuplify(t):
            if t:
                root = TreeNode(t[0])
                root.left = detuplify(t[1])
                root.right = detuplify(t[2])
                return root
        return detuplify(json.loads(data))
