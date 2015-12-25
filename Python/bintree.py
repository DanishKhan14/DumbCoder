"""
Python library for binary trees
"""

class BinaryTree(object):
    def __init__(self, rootNode):
        self.key = rootNode
        self.leftChild = None
        self.rightChild = None

    def setRootValue(self, value):
        self.key = value

    def getRootValue(self):
        return self.key

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.rightChild

    def getRightChild(self):
        return self.leftChild
