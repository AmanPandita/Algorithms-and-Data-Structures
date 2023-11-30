# Adapted from:
# Geeks for geeks
# stackoverflow
# https://docs.python.org/3.5/


def editDistance(x, y):
    """
    Compute the edit distance between two strings.

    Args:
    x (str): First string.
    y (str): Second string.

    Returns:
    int: The edit distance between the two strings.
    """

    m, n = len(x), len(y)

    # Create a matrix to store the distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column of the matrix
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Compute the distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # Delete
                                   dp[i][j - 1],    # Insert
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]
