def satisfy_dogs(hunger_levels, biscuit_sizes):
    # Sort the hunger levels and biscuit sizes in ascending order
    hunger_levels.sort()
    biscuit_sizes.sort()

    satisfied_dogs = 0
    current_biscuit = 0

    # Iterate through each dog's hunger level
    for hunger in hunger_levels:
        # Iterate through the biscuit sizes to find a suitable biscuit
        while current_biscuit < len(biscuit_sizes) and biscuit_sizes[current_biscuit] < hunger:
            current_biscuit += 1  # Move to the next larger biscuit

        # Check if a suitable biscuit was found
        if current_biscuit < len(biscuit_sizes):
            satisfied_dogs += 1  # Satisfy the current dog
            current_biscuit += 1  # Use this biscuit and move to the next

    return satisfied_dogs

# Example use of the function
hunger_level_example = [1, 5, 8]
biscuit_size_example = [1, 2, 3, 8]



print(satisfy_dogs(hunger_level_example, biscuit_size_example))





def count_ways_to_arrange_blocks(N):
    # Base cases: If N is 0 or 1, there is only one way to arrange the blocks
    if N == 0 or N == 1:
        return 1

    # Initialize an array to store the number of ways for each length up to N
    dp = [0] * (N + 1)

    # Base cases
    dp[0], dp[1] = 1, 1

    # Use a bottom-up approach to fill the dp array
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]

# Example use of the function
example_N = 4
count_ways_to_arrange_blocks(example_N)




def count_ways_brute_force(N):

    # Base case: if N is 0, it means the blocks have perfectly fitted the required length
    if N == 0:
        return 1

    # If N is negative, it means the blocks exceeded the required length
    if N < 0:
        return 0

    # Count the ways by adding a 1-unit block and a 2-unit block
    return count_ways_brute_force(N - 1) + count_ways_brute_force(N - 2)

# Example use of the function
example_N = 2
count_ways_brute_force(example_N)








def max_dogs(hunger_levels, biscuit_sizes):
    # Sort the hunger levels and biscuit sizes in ascending order
    hunger_levels.sort()
    biscuit_sizes.sort()
    
    
    # Initialize number of satisfied dogs count to 0
    no_of_dogs = 0

    # Initialize the index of the current biscuit
    current_biscuit = 0


    # Iterate through the hunger levels
    for hunger in hunger_levels:

        # Find a suitable biscuit for the current dog

        while current_biscuit < len(biscuit_sizes) and biscuit_sizes[current_biscuit] < hunger:
            current_biscuit += 1  # Move to the next larger biscuit

        # Check if a suitable biscuit was found
        if current_biscuit < len(biscuit_sizes):
            no_of_dogs += 1  # Satisfy the current dog
            current_biscuit += 1  # Use this biscuit and move to the next

    return no_of_dogs
