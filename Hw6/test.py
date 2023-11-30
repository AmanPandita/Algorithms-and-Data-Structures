from hw6 import editDistance
import random
import string
import time
import matplotlib.pyplot as plt



# # Test cases
# test_cases = [

#     # Test case 1
#     ("ATCAT", "ATTATC"),


#     # Test case 2
#     ("taacttctagtacatacccgggttgagcccccatttcttggttggatgcgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat", 
#      "taacttctagtacatacccgggttgagcccccatttccgaggaacattacgctagaggaacaacaaggtcagaggcctgttactcctat"),


#     # Test case 3
#     ("CGCAATTCTGAAGCGCTGGGGAAGACGGGT", "TATCCCATCGAACGCCTATTCTAGGAT"),


#     # Test case 4
#     ("tatttacccaccacttctcccgttctcgaatcaggaatagactactgcaatcgacgtagggataggaaactccccgagtttccacagaccgcgcgcgatattgctcgccggcatacagcccttgcgggaaatcggcaaccagttgagtagttcattggcttaagacgctttaagtacttaggatggtcgcgtcgtgccaa",

#      "atggtctccccgcaagataccctaattccttcactctctcacctagagcaccttaacgtgaaagatggctttaggatggcatagctatgccgtggtgctatgagatcaaacaccgctttctttttagaacgggtcctaatacgacgtgccgtgcacagcattgtaataacactggacgacgcgggctcggttagtaagtt")
# ]

# # results = print([editDistance(*test_case) for test_case in test_cases])

# # Initialize an empty list to store the results
# results = []
# # test = []

# # Loop through each test case in the list of test cases
# for test_case in test_cases:
#     # Unpack the test case into two separate strings
#     string1, string2 = test_case

#     # Calculate the edit distance for this pair of strings
#     distance = editDistance(string1, string2)

#     # Append the calculated distance to the results list
#     print("\n\n For test case: ", string1, ",", string2)
#     print("\n\n = ", distance)


#     # print("\n\n", string1,string2, " = ", distance)
#     results.append(distance)

#     # test.append(test_case)


# # print("\n\n", results)








# def generate_random_string(length):
#     """Generate a random string of given length."""
#     return ''.join(random.choice(string.ascii_letters) for _ in range(length))




# def compute_average_time(length, num_pairs=10):
#     """Compute the average time taken to calculate the edit distance for random string pairs of a given length."""
#     total_time = 0

#     for _ in range(num_pairs):
#         str1 = generate_random_string(length)
#         str2 = generate_random_string(length)

#         start_time = time.time()
#         editDistance(str1, str2)
#         end_time = time.time()

#         total_time += (end_time - start_time)

#     return total_time / num_pairs



# # Lengths of strings
# lengths = []
# for i in range(1, 11):
#     lengths.append(i * 100)



# # Compute average times
# average_times = []
# for length in lengths:
#     avg_time = compute_average_time(length)
#     # print(avg_time)
#     average_times.append(avg_time)




# print("\n\n+---------------+-------------------------+")
# print("| {:<13} | {:<23} |".format("Lengths", "Average Times"))
# print("+---------------+-------------------------+")
# for i in range(len(lengths)):
#     print("| {:<13} | {:<23} |".format(lengths[i], average_times[i]))
#     print("+---------------+-------------------------+")





# # Plotting
# plt.plot(lengths, average_times, marker='o', color = 'g')
# plt.xlabel('Length of Strings')
# plt.ylabel('Average Time (seconds)')
# plt.title('Average Time to Compute Edit Distances vs Length of Strings')
# plt.grid(True)
# plt.show()

# average_times, lengths



# def longest_common_substring(str1, str2):
#     m, n = len(str1), len(str2)
    
#     # Create a 2D array to store lengths of longest common suffixes
#     dp = [[0] * (n+1) for _ in range(m+1)]

#     # To store length of the longest common substring
#     length_max = 0

#     # To store the ending index of the longest common substring in str1
#     end_index = 0

#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if str1[i-1] == str2[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1

#                 if dp[i][j] > length_max:
#                     length_max = dp[i][j]
#                     end_index = i
#             else:
#                 dp[i][j] = 0

#     # Return the longest common substring
#     return str1[end_index - length_max:end_index]

# # Example usage
# print(longest_common_substring("Philanthropic", "Misanthropist"))





# Question 3--------------


def maximize_profit(locations, profits, k):
    n = len(locations)
    sorted_locations = sorted(zip(locations, profits), key=lambda x: x[0])
    max_profit = [0] * n

    # Base case
    max_profit[0] = sorted_locations[0][1]

    # Fill DP array
    for i in range(1, n):
        max_profit[i] = sorted_locations[i][1]
        j = i - 1
        # Find the farthest location that satisfies the distance constraint
        while j >= 0 and sorted_locations[i][0] - sorted_locations[j][0] < k:
            j -= 1
        if j >= 0:
            max_profit[i] = max(max_profit[i], max_profit[j] + sorted_locations[i][1])

    # Find maximum profit
    return max(max_profit)


# # Question 4---------------------------
# def minimizeCost(n, m, X):
#     X = [0] + sorted(X) + [n]  # Add the ends of the rope and ensure X is sorted
#     Cost = [[0 for _ in range(m+2)] for _ in range(m+2)]
#     BestCut = [[0 for _ in range(m+2)] for _ in range(m+2)]

#     # Dynamic programming to calculate cost and best cut positions
#     for length in range(2, m+2):
#         for i in range(m+2-length):
#             j = i + length
#             Cost[i][j] = float('inf')
#             for k in range(i+1, j):
#                 cost = X[j] - X[i] + Cost[i][k] + Cost[k][j]
#                 if cost < Cost[i][j]:
#                     Cost[i][j] = cost
#                     BestCut[i][j] = k

#     # Function to reconstruct the sequence of cuts
#     def constructCutSequence(i, j):
#         if i + 1 >= j:
#             return []
#         k = BestCut[i][j]
#         return constructCutSequence(i, k) + [X[k]] + constructCutSequence(k, j)

#     # Get the sequence of cuts
#     cut_sequence = constructCutSequence(0, m+1)

#     return Cost[0][m+1], cut_sequence  # Return both cost and the sequence of cuts

# # Test the modified function
# n = 10  # Length of the rope
# m = 3   # Number of desired cuts
# X = [2, 4, 7]  # Desired locations of the cuts

# min_cost, cut_sequence = minimizeCost(n, m, X)
# print(min_cost, cut_sequence)




