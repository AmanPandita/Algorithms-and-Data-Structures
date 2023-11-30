from swar import MST_Kruskal, MST_Prim
import sys
import os
import ast
import time
import matplotlib.pyplot as plt

import pandas as pd


# Define a function to process each file and run the MST algorithms
def process_file(file_path):
    with open(file_path, 'r') as file:
        
        # Read the file content and convert it to a list of tuples
        content = file.read()
        graph_edges = ast.literal_eval(content)
        


        # Calculate the number of edges
        number_of_edges = len(graph_edges)
        Edge_count.append(number_of_edges)

        # Calculate the number of nodes
        nodes = set()
        for edge in graph_edges:
            nodes.update(edge)  # Add all nodes from each edge to the set
        number_of_nodes = len(nodes)

        Node_count.append(number_of_nodes)


        # Run the MST algorithms
        
        start = time.time()
        kruskal_result = MST_Kruskal(graph_edges)
        end = time.time()
        time_taken = round((end - start), 6) * 1000
        Krushal_time.append(time_taken)

        

        
        start = time.time()
        prim_result = MST_Prim(graph_edges)
        end = time.time()
        time_taken = round((end - start), 6) * 1000
        Prim_time.append(time_taken)

        
        
        # print(f"Results for {os.path.basename(file_path)}:")
        # print(f"Kruskal's algorithm: {kruskal_result}")
        # print(f"Prim's algorithm: {prim_result}")
        # print()
        


FileName = []
Krushal_time = []
Prim_time = []
Overall_time = []
Node_count = []
Edge_count = []

# Set the path to the folder containing the .txt files
folder_path = 'test_data'

# Get all the txt files and sort them
txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
sorted_files = sorted(txt_files, key=lambda x: int(x.split('.')[0]))

# Iterate over each file in the directory and process it in sorted order
for filename in sorted_files:
    # print(filename)
    
    FileName.append(filename)
    file_path = os.path.join(folder_path, filename)

    start = time.time()
    process_file(file_path)
    end = time.time()

    time_taken = round((end - start), 6) * 1000
    Overall_time.append(time_taken)




print("\n\n{:<15} {:<25} {:<25} {:<25} {:<25} {:<25}".format("Test_File", "Node_count", "Edge_count", "Krusal's Algorithm (ms)", "Prim's Algorithm (ms)", "Total Time taken (ms)"))
for i in range(len(FileName)):
    print("{:<15} {:<25} {:<25} {:<25} {:<25} {:<25}".format(FileName[i], Node_count[i], Edge_count[i], Krushal_time[i], Prim_time[i], Overall_time[i]))





# Converting the simulated data into a DataFrame for plotting
data = {
    'Test_File': FileName,
    'Node_count': Node_count,
    'Edge_count': Edge_count,
    'Kruskal_Algorithm_ms': Krushal_time,
    'Prim_Algorithm_ms': Prim_time,
    'Total_Time_ms': Overall_time
}

results_df = pd.DataFrame(data)

# Plotting the results
plt.figure(figsize=(14, 7))

# Plot for Kruskal's Algorithm
plt.plot(results_df['Edge_count'], results_df['Kruskal_Algorithm_ms'], marker='o', linestyle='-', color='blue', label="Kruskal's Algorithm")

# Plot for Prim's Algorithm
plt.plot(results_df['Edge_count'], results_df['Prim_Algorithm_ms'], marker='s', linestyle='--', color='red', label="Prim's Algorithm")

# Adding labels and title
plt.xlabel('Number of Edges')
plt.ylabel('Running Time (ms)')
plt.title('Running Times of Kruskal vs Prim Algorithms')

# Adding legend
plt.legend()

# Setting log scale for x and y due to large range of values
# plt.xscale('log')
# plt.yscale('log')

# Adding grid for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Showing the plot
plt.tight_layout()
plt.show()
