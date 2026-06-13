class Solution:
    # Bottom-up
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

    # Memoization
    # def climbStairs(self, n: int) -> int:
    #     memo = {}

    #     def helper(x):
    #         if x == 1:
    #             return 1
    #         elif x == 2:
    #             return 2

    #         if x in memo:
    #             return memo[x]

    #         memo[x] = helper(x-1) + helper(x-2)
    #         return memo[x]

    #     return helper(n)