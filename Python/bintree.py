#!/usr/bin/python

"""
Python library for binary trees
"""

class BinaryTree():

    def __init__(self, rootNode):
        self.key = rootNode
        self.leftChild = None
        self.rightChild = None

    def setRootValue(self, value):
        self.key = value

    def getRootValue(self):
        return self.key

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild
