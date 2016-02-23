# coding=utf-8

# Directed Graph

# Method 1: Using DFS
"""
Detecting cycles in a directed graph with DFS. Suppose we wanted to determine whether a directed graph has a cycle.
Then we can do this with a depth first search (DFS):

– Initialize a dictionary ‘marked’ that tells us whether a node has been visited.
– Initialize a dictionary ‘color’ that tells us whether a node is “white”, “gray” or “black”.
– We visit all nodes.
– Everytime we visit a node u we color it “gray” indicating that the node is part of our current path.
– We visit the neighbors of u that are “white”, i.e. those nodes that have not been visited yet.
– If we visit a neighbor node v that is colored “gray”, then a cycle exists. Otherwise, if we don’t find such a node v,
 then there is no cycle.
– After having visited all neighbor nodes v we color node u “black”, indicating that we are finished with u and that we
 will leave it again.
"""


def cycle_exists(G):  # - G is a directed graph
    # color = { u : "white" for u in G  }  # - All nodes are initially white
    color = dict([(u, "white") for u in G])
    found_cycle = [False]  # - Define found_cycle as a list so we can change
    # its value per reference, see:
    # http://stackoverflow.com/questions/11222440/python-variable-reference-assignment
    for u in G:  # - Visit all nodes.
        if color[u] == "white":
            dfs_visit(G, u, color, found_cycle)
        if found_cycle[0]:
            break
    return found_cycle[0]


# -------

def dfs_visit(G, u, color, found_cycle):
    if found_cycle[0]:  # - Stop dfs if cycle is found.
        return
    color[u] = "gray"  # - Gray nodes are in the current path
    for v in G[u]:  # - Check neighbors, where G[u] is the adjacency list of u.
        if color[v] == "gray":  # - Case where a loop in the current path is present.
            found_cycle[0] = True
            return
        if color[v] == "white":  # - Call dfs_visit recursively.
            dfs_visit(G, v, color, found_cycle)
    color[u] = "black"  # - Mark node as done.


# Undirected Graph

"""
Detecting cycles in an undirected graph with DFS
Suppose we wanted to determine whether an undirected graph has a cycle. Then we can do this
with a depth first search (DFS):

– Initialize a dictionary ‘marked’ that tells us whether a node has been visited.
– We visit all nodes.
– Everytime we visit a node u we mark it.
– We visit the neighbors of u.
– If we visit a neighbor node v that has already been marked, then a cycle exists. Otherwise,
if we don’t find such a node v, then there is no cycle.
– We visit the neighbors of v by a recursive call of dfs_visit.
– If we visit the neighbors of v, then we have to ignore its predecessor u which has already been marked.
Otherwise we would erroneously conclude that the graph G = (V, E) with V = {1, 2} and E = {{1, 2}} has a cycle.

To be more elaborate, after visiting node u = 1 and marking it, we visit its neighbor v = 2.
 Now, if we visit v = 2 and discover its already marked neighbor node 1, we must not conclude that the graph
 has a cycle.
"""


def cycle_exists(G):  # - G is an undirected graph.
    # marked = { u : False for u in G }     # - All nodes are initially unmarked.
    marked = dict([(u, False) for u in G])
    found_cycle = [False]  # - Define found_cycle as a list so we can change

    for u in G:  # - Visit all nodes.
        if not marked[u]:
            dfs_visit(G, u, found_cycle, u, marked)  # - u is its own predecessor initially
        if found_cycle[0]:
            break
    return found_cycle[0]


# --------

def dfs_visit(G, u, found_cycle, pred_node, marked):
    if found_cycle[0]:  # - Stop dfs if cycle is found.
        return
    marked[u] = True  # - Mark node.
    for v in G[u]:  # - Check neighbors, where G[u] is the adjacency list of u.
        if marked[v] and v != pred_node:  # - If neighbor is marked and not predecessor,
            found_cycle[0] = True  # then a cycle exists.
            return
        if not marked[v]:  # - Call dfs_visit recursively.
            dfs_visit(G, v, found_cycle, u, marked)
