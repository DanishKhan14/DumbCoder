# coding=utf-8
"""
Kahns algorithm
The idea of Kahns algorithm is to repeatedly remove nodes that have zero in-degree. The steps are as follows:
– Determine the in-degree of each node.
– Collect nodes with zero in-degree in a queue.
– While the queue is not empty:
______Pop node u from queue,
______remove u from the graph,
______check if there is a new node with in-degree zero (among the neighbors of u)
______If yes, put that node into the queue.
– We maintain a list that records in which order the nodes are removed.
– If the queue is empty:
_____if we removed all nodes from the graph, return the list
_____else we return an empty list that indicates that an order is not possible due to a cycle
"""

from collections import deque


def kahn_topsort(graph):
    in_degree = dict([(u, 0) for u in graph])  # determine in-degree
    for u in graph:  # of each node
        for v in graph[u]:
            in_degree[v] += 1

    Q = deque()  # collect nodes with zero in-degree
    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)

    L = []  # list for order of nodes

    while Q:
        u = Q.pop()  # choose node of zero in-degree
        L.append(u)  # and 'remove' it from graph
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.appendleft(v)

    if len(L) == len(graph):
        return L
    else:  # if there is a cycle,
        return []  # then return an empty list


# Using DFS

"""
We can get the topological sort, i.e. the order for the nodes with a depth first search (DFS).
It works as follows: everytime we are finished with a node, we put the node into a list.
After DFS has finished we reverse that list and return it. The list then contains the topological sort.

Another way to look at it is that we first determine the finishing times of the nodes, and then we print
the nodes in the reverse order of their finishing times
"""


def dfs_topsort(graph):  # recursive dfs with
    L = []  # additional list for order of nodes
    color = dict([(u, "white") for u in graph])
    found_cycle = [False]
    for u in graph:
        if color[u] == "white":
            dfs_visit(graph, u, color, L, found_cycle)
        if found_cycle[0]:
            break

    if found_cycle[0]:  # if there is a cycle,
        L = []  # then return an empty list

    L.reverse()  # reverse the list
    return L  # L contains the topological sort


def dfs_visit(graph, u, color, L, found_cycle):
    if found_cycle[0]:
        return
    color[u] = "gray"
    for v in graph[u]:
        if color[v] == "gray":
            found_cycle[0] = True
            return
        if color[v] == "white":
            dfs_visit(graph, v, color, L, found_cycle)
    color[u] = "black"  # when we're done with u,
    L.append(u)  # add u to list (reverse it later!)
