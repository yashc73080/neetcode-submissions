class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] would contain min total cost at that point
        # at each dp[i], find the min of the last 2 steps and go on
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])