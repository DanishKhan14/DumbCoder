#!/usr/bin/python


def dfs(graph, start):
    """
    No recursion

    :param graph: adjacency list
    :param start: starting node
    :return: visited nodes
    """

    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
    return visited


def bfs(graph, start):
    """
    No recursion

    :param graph:
    :param start:
    :return:
    """
    visited, stack = set(), [start]
    while stack:
        node = stack.pop(0)
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node] - visited)
    return visited

