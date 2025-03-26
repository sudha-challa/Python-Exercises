def maximize_earnings(N, M, quantity_available, quantity_needed, cost_of_one_unit, selling_price):
    # Create a 2D array to store the maximum earnings for each quantity and type of material
    dp = [[0] * (N + 1) for _ in range(M + 1)]

    # Fill the dp array using bottom-up dynamic programming
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            # If there is enough quantity of material i, consider the possibility of using it
            if quantity_available[i - 1] >= quantity_needed[i - 1]:
                # Calculate the maximum earnings for the current quantity and material type
                dp[i][j] = max(dp[i - 1][j], dp[i][j - quantity_needed[i - 1]] + selling_price[i - 1] - cost_of_one_unit[i - 1])

    # The maximum earnings will be stored in the bottom-right cell of the dp array
    max_earnings = dp[M][N]

    return max_earnings

# Read input
N, M = map(int, input().split())
quantity_available = list(map(int, input().split()))
quantity_needed = list(map(int, input().split()))
cost_of_one_unit = list(map(int, input().split()))
selling_price = list(map(int, input().split()))

# Call the function and print the result
result = maximize_earnings(N, M, quantity_available, quantity_needed, cost_of_one_unit, selling_price)

# Print the total amount earned by Vinni by selling toys
print(result)
