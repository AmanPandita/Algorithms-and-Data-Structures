
import random
from collections import defaultdict, deque

def generate_seq(k, length, seed):
    """Generate a random graph."""
    random.seed(seed)
    temp = [tuple(sorted(random.sample(range(k), 2)) + [random.randint(5, 10)]) for _ in range(length)]
    graph = []
    edge_sets = set()
    for (u, v, l) in temp:
        if (u, v) not in edge_sets and (v, u) not in edge_sets:
            graph.append((u, v, l))
            edge_sets.add((u, v))
    return graph

def bfs_shortest_path(residual_graph, source, sink):
    """Find shortest path using BFS."""
    visited = set()
    queue = deque([(source, [])])
    while queue:
        node, path = queue.popleft()
        if node == sink:
            return path
        visited.add(node)
        for neighbor, capacity in residual_graph[node].items():
            if capacity > 0 and neighbor not in visited:
                new_path = path + [(node, neighbor)]
                queue.append((neighbor, new_path))
    return None

def dijkstra_max_path(residual_graph, source, sink):
    """Find maximum capacity path using a Dijkstra-like approach."""
    max_capacity = {node: 0 for node in residual_graph}
    max_capacity[source] = float('inf')
    visited = set()
    path = {}
    while True:
        max_node = None
        max_cap = 0
        for node in residual_graph:
            if max_capacity[node] > max_cap and node not in visited:
                max_cap = max_capacity[node]
                max_node = node
        if max_node is None or max_node == sink:
            break
        visited.add(max_node)
        for neighbor, capacity in residual_graph[max_node].items():
            if capacity > 0 and max_capacity[neighbor] < min(max_cap, capacity):
                max_capacity[neighbor] = min(max_cap, capacity)
                path[neighbor] = max_node
    
    
    if sink not in path:
        return None
    # Reconstruct the path
    
    
    max_path = []
    current = sink
    while current != source:
        prev = path[current]
        max_path.append((prev, current))
        current = prev
    return max_path[::-1]

def Max_Flow_Short(source, sink, graph):
    """Ford-Fulkerson algorithm using the Short Pipes strategy."""
    residual_graph = defaultdict(dict)
    for u, v, capacity in graph:
        residual_graph[u][v] = capacity
        residual_graph[v][u] = 0

    max_flow = 0
    flows = []
    while True:
        path = bfs_shortest_path(residual_graph, source, sink)
        if not path:
            break

        min_capacity = min(residual_graph[u][v] for u, v in path)
        max_flow += min_capacity

        for u, v in path:
            residual_graph[u][v] -= min_capacity
            residual_graph[v][u] += min_capacity
            flows.append((u, v, min_capacity))

    return max_flow, flows

def Max_Flow_Fat(source, sink, graph):
    """Ford-Fulkerson algorithm using the Fat Pipes strategy."""
    residual_graph = defaultdict(dict)
    for u, v, capacity in graph:
        residual_graph[u][v] = capacity
        residual_graph[v][u] = 0

    max_flow = 0
    flows = []
    while True:
        path = dijkstra_max_path(residual_graph, source, sink)
        if not path:
            break

        min_capacity = min(residual_graph[u][v] for u, v in path)
        max_flow += min_capacity

        for u, v in path:
            residual_graph[u][v] -= min_capacity
            residual_graph[v][u] += min_capacity
            flows.append((u, v, min_capacity))

    return max_flow, flows



    