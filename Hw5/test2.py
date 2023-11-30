from swar import MST_Kruskal, MST_Prim

class Graph:
    def _init_(self):
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))

def read_graph_from_file(file_path):
    graph = Graph()
    with open(file_path, 'r') as file:
        graph_data = file.read().strip('[]\n').replace('), (', ')\n(').split('\n')
        for line in graph_data:
            u, v, weight = map(int, line.strip('()').split(', '))
            graph.add_edge(u, v, weight)
    return graph

# Example usage
file_path = 'test_data/9.txt'  # Update this with the path to your text file
graph = read_graph_from_file(file_path)


# a =  MST_Kruskal([(u, v, weight) for u in graph.adjacency_list for v, weight in graph.adjacency_list[u]])
# b =  MST_Prim([(u, v, weight) for u in graph.adjacency_list for v, weight in graph.adjacency_list[u]])

# Now you can use the graph object to perform MST algorithms (Kruskal's and Prim's)
kruskal_weight, kruskal_edges = MST_Kruskal([(u, v, weight) for u in graph.adjacency_list for v, weight in graph.adjacency_list[u]])
prim_weight, prim_edges = MST_Prim([(u, v, weight) for u in graph.adjacency_list for v, weight in graph.adjacency_list[u]])

print("Kruskal's MST Weight:", kruskal_weight)
print("Kruskal's MST Edges:", kruskal_edges)
print("Prim's MST Weight:", prim_weight)
print("Prim's MST Edges:", prim_edges)

# print("kkkk:", a)
# print("ppp:", b )
print(kruskal_weight == prim_weight)