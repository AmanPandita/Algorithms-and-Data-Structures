



from hw4 import ShortestPath




# Example usage
start_state = [1, 2, 3, 4, 5, 6, 8, 7, 0]
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
initial_states = [start_state]  
solution_lengths = ShortestPath(goal_state, initial_states)
print(solution_lengths)

start_state = [1, 2, 3, 8,0,4,7,6,5]
goal_state = [1,3,4,8,6,2,7,0,5]
initial_states = [start_state]  
solution_lengths = ShortestPath(goal_state, initial_states)
print(solution_lengths)

start_state = [1, 2, 3, 8,0,4,7,6,5]
goal_state = [2,8,1,0,4,3,7,6,5]
initial_states = [start_state]  
solution_lengths = ShortestPath(goal_state, initial_states)
print(solution_lengths)

start_state = [1, 2, 3, 8,0,4,7,6,5]
goal_state = [2,8,1,4,6,3,0,7,5]
initial_states = [start_state]  
solution_lengths = ShortestPath(goal_state, initial_states)
print(solution_lengths)

start_state = [1,3,4,8,0,5,7,2,6]
goal_state = [1,2,3,8,0,4,7,6,5]
initial_states = [start_state]  
solution_lengths = ShortestPath(goal_state, initial_states)
print(solution_lengths)

start_state = [2,3,1,7,0,8,6,5,4]
goal_state = [1,2,3,8,0,4,7,6,5]
initial_states = [start_state]  
solution_lengths = ShortestPath(goal_state, initial_states)
print(solution_lengths)

start_state = [2,3,1,8,0,4,7,6,5]
goal_state = [1,2,3,8,0,4,7,6,5]
initial_states = [start_state]  
solution_lengths = ShortestPath(goal_state, initial_states)
print(solution_lengths)

start_state = [4,1,2,0,8,7,6,3,5]
goal_state = [1, 2, 3, 4,5,6,7,8,0]
initial_states = [start_state,[1,6,2,5,7,3,0,4,8]]  
solution_lengths = ShortestPath(goal_state, initial_states)
print(solution_lengths)

start_state = [1,6,2,5,7,3,0,4,8]
goal_state = [1, 2, 3, 4,5,6,7,8,0]
initial_states = [start_state]  
solution_lengths = ShortestPath(goal_state, initial_states)
print(solution_lengths)

start_state = [8,0,6,5,4,7,2,3,1]
goal_state = [0,1,2,3,4,5,6,7,8]
initial_states = [start_state]  
solution_lengths = ShortestPath(goal_state, initial_states)
print(solution_lengths)










#************************************ Question 3 ********************* O(n^3) Algorithm Floyd-Warshall Algorithm *********************************************************



# print("\n---------------------------------------------------------------------------Question 3 --------------------------------------------------------------------------")
def shortest_cycle(graph):
    n = len(graph)
    min_cycle_length = float('inf')
    
    # Run Floyd-Warshall to find shortest paths between all pairs of vertices
    dist = [[float('inf')] * n for _ in range(n)]
    for vertex in graph:
        for neighbor in graph[vertex]:
            dist[vertex][neighbor] = 1  # or the weight of the edge if the graph is weighted
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    # Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            return "Negative cycle detected"
                
    # Check for cycles after all shortest paths are found
    for i in range(n):
        if dist[i][i] < min_cycle_length:
            min_cycle_length = dist[i][i]
                    
    return -1 if min_cycle_length == float('inf') else min_cycle_length


# import time
# def shortest_cycle(graph):
#     n = len(graph)
#     min_cycle_length = float('inf')
    
#     # Run Floyd-Warshall to find shortest paths between all pairs of vertices
#     dist = [[float('inf')] * n for _ in range(n)]
#     for vertex in graph:
#         for neighbor in graph[vertex]:
#             dist[vertex][neighbor] = 1
    
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
#                 if i == j and dist[i][j] < min_cycle_length:
#                     min_cycle_length = dist[i][j]
                    
#     return -1 if min_cycle_length == float('inf') else min_cycle_length

# # Example usage:
# # Adjacency list representation
# graph = {
#     0: [1],
#     1: [2],
#     2: [3],
#     3: [1, 4],
#     4: []
# }


# start = time.time()
# print(shortest_cycle(graph))  # Output should be the length of the shortest cycle
# end = time.time()

# print(f"Time taken: {end - start} ms")



#************************************** Question 4 ******************* two runs of Dijkstra’s algorithm *********************************************************




# print("\n---------------------------------------------------------------------------Question 4 --------------------------------------------------------------------------")



# import heapq

# def dijkstra(graph, start):
#     distances = {v: float('inf') for v in graph}
#     distances[start] = 0
#     priority_queue = [(0, start)]

#     while priority_queue:
#         current_distance, current_node = heapq.heappop(priority_queue)

#         if current_distance > distances[current_node]:
#             continue

#         for neighbor, weight in graph[current_node].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(priority_queue, (distance, neighbor))

#     return distances

# def shortest_paths_through_A(graph, A):
#     # From every vertex to A
#     distToA = dijkstra(graph, A)

#     # Reverse the graph
#     reversed_graph = {v: {} for v in graph}
#     for v in graph:
#         for u, w in graph[v].items():
#             reversed_graph[u][v] = w

#     # From A to every vertex in the reversed graph
#     distFromA = dijkstra(reversed_graph, A)

#     # Calculate shortest paths through A
#     shortest_paths = {}
#     for i in graph:
#         for j in graph:
#             shortest_paths[(i, j)] = distToA[i] + distFromA[j]

#     return shortest_paths






# graph1 = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'C': 2, 'D': 5},
#     'C': {'D': 1},
#     'D': {}
# }

# start = time.time()

# print("\n")
# print(shortest_paths_through_A(graph1, 'A'))
# end = time.time()
# print(f"Time taken: {time_taken} ms")




# start = time.time()

# graph2 = {
#     'A': {'B': 2, 'C': 1},
#     'B': {'C': 2, 'D': 1},
#     'C': {'D': 3, 'E': 1},
#     'D': {'E': 1},
#     'E': {}
# }

# print("\n")
# print(shortest_paths_through_A(graph2, 'C'))

# end = time.time()
# print(f"Time taken: {time_taken} ms")



# graph3 = {
#     'A': {'B': 1},
#     'B': {'C': 2, 'D': 3},
#     'C': {'A': 4, 'D': 1},
#     'D': {'C': 1}
# }

# start = time.time()

# print("\n")
# print(shortest_paths_through_A(graph3, 'B'))
# end = time.time()
# print(f"Time taken: {time_taken} ms")
