from hw7 import Max_Flow_Fat, Max_Flow_Short
import random


# def generate_seq(k, length, seed):
#     """Generate a random graph."""
#     random.seed(seed)
#     temp = [tuple(sorted(random.sample(range(k), 2)) + [random.randint(5, 10)]) for _ in range(length)]
#     graph = []
#     edge_sets = set()
#     for (u, v, l) in temp:
#         if (u, v) not in edge_sets and (v, u) not in edge_sets:
#             graph.append((u, v, l))
#             edge_sets.add((u, v))
#     return graph



def run_tests():
    test_cases = [
        (0, 5, [(0, 1, 16), (0, 2, 13), (1, 3, 12), (2, 1, 4), (2, 4, 14), (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)]),
        (1, 4, [(1, 2, 3), (1, 3, 2), (2, 3, 1), (2, 4, 2), (3, 4, 3)]),
        (1, 5, [(1, 2, 2), (1, 3, 3), (2, 3, 1), (2, 4, 2), (3, 4, 2), (3, 5, 3), (4, 5, 2)]),
        (1, 3, [(1, 2, 2), (1, 3, 1), (2, 3, 1)]),
        (1, 5, [(1, 2, 2), (1, 3, 2), (2, 3, 3), (2, 4, 2), (3, 4, 1), (3, 5, 2), (4, 5, 3)]),
        (1, 5, [(1, 2, 2), (1, 3, 3), (2, 3, 3), (2, 4, 2), (3, 4, 1), (3, 5, 2), (4, 5, 3)])
    ]

# #     for source, sink, graph in test_cases:
# #         result_fat = Max_Flow_Fat(source, sink, graph)
# #         result_short = Max_Flow_Short(source, sink, graph)

# #         # Print the test case details
# #         print(f"test case: ({source}, {sink}, {graph})")
# #         print(f"Source: {source} -> Sink: {sink}")
        
# #         # Print the results
# #         print("Max_Flow_Fat Result   :", result_fat)
# #         print("Max_Flow_Short Result :", result_short)
# #         print()
        

     

# # if __name__ == "__main__":
# #     run_tests()


    print("\nRunning Max Flow Tests\n")
    print("=" * 60)
    
    for source, sink, graph in test_cases:
        result_fat = Max_Flow_Fat(source, sink, graph)
        result_short = Max_Flow_Short(source, sink, graph)

        # Header for each test case
        print(f"\nTest Case: [ {source} , {sink}, {graph}]")

        print(f"\nSource -> {source} Sink -> {sink}")

        print(f"Graph: {graph}")
        print("-" * 60)

        # Results
        print(f"Max_Flow_Fat Result   : {result_fat}")
        print(f"Max_Flow_Short Result : {result_short}")
        print("-" * 60)

if __name__ == "__main__":
    run_tests()






# -----------------------------------------------------------------------------------------------------
# import random
# from hw7 import Max_Flow_Fat, Max_Flow_Short
# import time

# def generate_seq(k, length):
#     """Generate a random graph."""
#     random.seed(time.time())  # Use current time as seed
#     temp = [tuple(sorted(random.sample(range(k), 2)) + [random.randint(5, 10)]) for _ in range(length)]
#     graph = []
#     edge_sets = set()
#     for (u, v, l) in temp:
#         if (u, v) not in edge_sets and (v, u) not in edge_sets:
#             graph.append((u, v, l))
#             edge_sets.add((u, v))
#     return graph


# def run_tests():
#     # Generate a set of test cases
    
    
#     test_cases = [
#         (0, 5, generate_seq(6, 10)),  # Example test case
#         # You can add more test cases with different parameters
#     ]

#     print("Running Max Flow Tests")
#     print("=" * 60)
    
#     for source, sink, graph in test_cases:
#         result_fat = Max_Flow_Fat(source, sink, graph)
#         result_short = Max_Flow_Short(source, sink, graph)

#         # Header for each test case

#         print(f"\nTest Case: [ {source} , {sink}, {graph}]")

#         print(f"\nTest Case: Source: {source} -> Sink: {sink}")
#         print(f"Graph: {graph}")
#         print("-" * 60)

#         # Results
#         print(f"Max_Flow_Fat Result   : {result_fat}")
#         print(f"Max_Flow_Short Result : {result_short}")
#         print("-" * 60)

# if __name__ == "__main__":
#     run_tests()
