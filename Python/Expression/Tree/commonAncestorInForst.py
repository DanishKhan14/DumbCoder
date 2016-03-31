class Node(object):

    def __init__(self, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right


class NodeCursor:

    def __init__(self, node):
        self.node = node
        self.depth = 0
        self.root = self.node
        while self.root.parent is not None:
            self.depth += 1
            self.root = self.root.parent

    def move_up(self):
        self.depth -= 1
        self.node = self.node.parent


class AncestorFinder(object):

    def __init__(self, node1, node2):
        self.cursor1 = NodeCursor(node1)
        self.cursor2 = NodeCursor(node2)
        self.ancestor = self.__find()

    def __find(self):
        if self.cursor1.root != self.cursor2.root:
            return None

        # make both cursors the same depth
        while self.cursor1.depth != self.cursor2.depth:
            if self.cursor1.depth > self.cursor2.depth:
                self.cursor1.move_up()
            else:
                self.cursor2.move_up()

        while self.cursor1.node != self.cursor2.node:
            self.cursor1.move_up()
            self.cursor2.move_up()
        return self.cursor1.node