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


def dfs_rec(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_rec(graph, next, visited)
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


def bfs_rec(graph, start, visited = None):
    """
    Not tested. Basically, at each level, visit all
    nodes and then recursively call bfs

    :param graph:
    :param start:
    :param visited:
    :return:
    """
    if visited is None:
        visited = set()
    visited.add(start)
    nodes = graph[start] - visited
    for next in nodes:
        visited.add(next)
    for node in nodes:
        bfs_rec(graph, node, visited)


def dfs_paths(graph, start, goal):
    """

    :param graph:
    :param start:
    :param goal:
    :return:
    """
    stack = [(start, [start])]
    while stack:
        node, path = stack.pop()
        for next in graph[node] - set(path)
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def dfs_paths_rec(graph, start, goal, path=None):
    """

    :param graph:
    :param start:
    :param end:
    :param path:
    :return:
    """
    if start is None:
        path =  [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_rec(graph, next, goal, path + [next])


def bfs_paths(graph, start, goal):
    """

    :param graph:
    :param start:
    :param goal:
    :return:
    """
    queue = [(start, [start])]
    while queue:
        node, path = queue.pop(0)
        for next in graph[node] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append(next, path+[next])


def shortestPath(graph, start, goal):
    """

    :param graph:
    :param start:
    :param goal:
    :return: shorted path
    """
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


