import os

def MST_Kruskal(graph):
    # Helper function to find the root of a set
    def find(parent, node):
        if parent[node] == node:
            return node
        return find(parent, parent[node])

    # Helper function to perform union of two sets
    def union(parent, rank, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    graph = sorted(graph, key=lambda x: x[2])  # Sort edges by weight
    num_nodes = max(max(edge[:2]) for edge in graph) + 1
    parent = list(range(num_nodes))
    rank = [0] * num_nodes
    mst = []
    total_weight = 0

    for edge in graph:
        u, v, weight = edge
        if find(parent, u) != find(parent, v):
            mst.append((u, v))
            total_weight += weight
            union(parent, rank, u, v)

    return total_weight, mst

import heapq

def MST_Prim(graph):
    visited = set()
    start_node = graph[0][0]
    visited.add(start_node)
    min_heap = [(weight, start_node, node) for (start_node, node, weight) in graph]
    heapq.heapify(min_heap)
    mst = []
    total_weight = 0

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if v not in visited:
            visited.add(v)
            mst.append((u, v))
            total_weight += weight

    return total_weight, mst



# graph1 = ([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
# graph2 = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]


# Krushal_Algo = MST_Kruskal(graph1)
# prim_algo = MST_Prim(graph2)

# print(Krushal_Algo)
# print(prim_algo)