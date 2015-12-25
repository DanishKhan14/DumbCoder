#!/usr/bin/python

"""
Expression Parser Tree for fully parenthesized input expression
"""

from bintree import BinaryTree
from stackModule import Stack

def buildParseTree(expression):
    expList = expression.split()
    empTree = BinaryTree('')
    parentStack = Stack()
    parentStack.push(empTree)
    currentNode = empTree

    for item in expList:
        if item == '(':
            currentNode.insertLeft('')
            parentStack.push(currentNode)
            currentNode = currentNode.getLeftChild()
        elif item not in ['+', '-', '*', '/', ')']:
            currentNode.setRootValue(int(item))
            currentNode = parentStack.pop()
        elif item in ['+', '-', '*', '/']:
            currentNode.setRootValue(item)
            currentNode.insertRight('')
            parentStack.push(currentNode)
            currentNode = currentNode.getRightChild()
        elif item == ')':
            currentNode = parentStack.pop()
        else:
            raise ValueError
    return empTree

import operator

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootValue()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootValue()

def postOrderTraversal(parseTree):

    if parseTree != None:
        postOrderTraversal(parseTree.getLeftChild())
        postOrderTraversal(parseTree.getRightChild())
        print parseTree.getRootValue()

def preOrderTraversal(parseTree):

    if parseTree !=None:
        print parseTree.getRootValue()
        preOrderTraversal(parseTree.getLeftChild())
        preOrderTraversal(parseTree.getRightChild())

def inOrderTraversal(parseTree):

    if  parseTree !=None:
        inOrderTraversal(parseTree.getLeftChild())
        print parseTree.getRootValue()
        inOrderTraversal(parseTree.getRightChild())


def iterInOrder(currentTree):
    pStack = Stack()
    print "\nPrinting in order traversal\n"
    while currentTree != None or not pStack.isEmpty():
        if currentTree !=None:
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        else:
            currentTree = pStack.pop()
            print currentTree.getRootValue()
            currentTree = currentTree.getRightChild()


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print "\nGiven Expression evaluates to %d\n" % evaluate(pt)
preOrderTraversal(pt)
postOrderTraversal(pt)
inOrderTraversal(pt)
iterInOrder(pt)
