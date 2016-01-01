#!/usr/bin/python

"""
Graph Traversal Algorithms
"""

from Queue import Queue as Q


def bfs(g, start):
    start.setDistance = -1
    start.setPred(None)
    nodeQ = Q
    nodeQ.put(start)
    while not nodeQ.empty():
        currentNode = nodeQ.get()
        for nbr in currentNode.getConnections():
            if nbr.getColor == "white":
                nodeQ.setDistance = currentNode.getDistance() + 1
                nodeQ.setPred(currentNode)
                nodeQ.setColor = "gray"
                nodeQ.put(currentNode)
        currentNode.setColor = "black"

def bfsTraverse(y):
    x = y
    while(x.getPred()):
        print x.getId()
        x = x.getPred()
    print x.getPred()

def dfs(g, start):
    start.setDistance = -1
    start.setPred = None
    nodeStack = Queue.LifoQueue()
    start.setColor = "White"
    currentNode = start
    nodeStack.put(currentNode)
    while not nodeStack.empty():
        currentNode = nodeStack.get()
        print currentNode.getId()
        currentNode.setColor = "Black"
        for nbr in currentNode.getConnections():
            if nbr.getColor == "White":
                nbr.setPred = currentNode
                nbr.setDistance = currentNode.getDistance() + 1
                nodeStack.put(nbr)

def dfsRec(g, start)
    start.setColor == "gray"
    for nbr in start.getConnections():
        if nbr.getColor == "white":
            nbr.setColor == "gray"
            dfsRec(nbr)
    start.setColor = "Black"
    print start.getId()




