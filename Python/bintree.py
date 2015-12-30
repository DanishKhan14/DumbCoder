#!/usr/bin/python

"""
Python library for binary trees
"""

import stackModule as s

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


def inOrderNorec(rootNode):
    """
    :param rootNode:
    :return:
    """
    currenNode = rootNode
    while currenNode is not None or not s.isEmpty():
        if currenNode is not None:
            s.push(currenNode)
            currenNode = currenNode.getLeftChild()
        else:
            currenNode = s.pop()
            print currenNode.getRootValue()
            currenNode = currenNode.getRightChild()


def preOrderNorec(rootNode):
    """

    :param rootNode:
    :return:
    """
    currentNode = rootNode
    while currentNode is not None or not s.isEmpty():
        if currentNode is not None:
            s.push(currentNode)
            print currentNode.getRootValue()
            currentNode = currentNode.getLeftChild()
        else:
            s.push(currentNode)
            currentNode = currentNode.getRightChild()


def postOrderNorec(rootNode):
    """

    :param rootNode:
    :return:
    """
    visited = BinaryTree(None)
    currentNode = rootNode
    while currentNode is not None or not s.isEmpty:
        if currentNode is not None:
            s.push(currentNode)
            currentNode = currentNode.getLeftChild()
        else:
            currentNode = s.pop()
            if currentNode.getRightChild is None or currentNode.getRightChild == visited:
                print currentNode.getRootValue
                visited = currentNode
            if not currentNode == visited:
                s.push(currentNode)
            currentNode = currentNode.getRightChild()


def postOrder(rootNode):
    """

    :param rootNode:
    :return:
    """

def inOrder(rootNode):
    """

    :param rootNode:
    :return:
    """

def preOrder(rootNode):
    """

    :param rootNode:
    :return:
    """

def maxHeight(rootNode):
    """

    :param rootNode:
    :return:
    """

def hasSum(rootNode, sum):
    """

    :param rootNode:
    :param sum:
    :return:
    """
