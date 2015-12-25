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
        print item
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
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootValue()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootValue()


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print evaluate(pt)
