def min_budget_for_all_orders(projects):
    n = len(projects)

    # Sort projects based on the penalty/reward (descending order)
    projects.sort(key=lambda x: x[2], reverse=True)

    # Initialize DP array
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Update DP array for each project
    for i in range(1, n + 1):
        expenditure, completion_bonus, reward_penalty = projects[i - 1]

        # Iterate through all previous projects
        for j in range(i, 0, -1):
            # Calculate the new budget for the current order
            new_budget = dp[j - 1] + expenditure - completion_bonus

            # Update DP array if the new budget is smaller
            dp[j] = min(dp[j], new_budget)

    # Find the minimum budget needed
    min_budget = float('inf')
    for i in range(n + 1):
        min_budget = min(min_budget, max(dp[i], 0))

    return min_budget

# Input
n = int(input())
projects = [input().strip().split() for _ in range(n)]
projects = [(int(proj[0]), int(proj[1]), int(proj[2])) for proj in projects]

# Output
result = min_budget_for_all_orders(projects)
print(result)
