class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])

def main():
    sol = Solution()
    cost = [ 1 ,100, 1 ,1, 1 ,100, 1 , 1 ,100, 1 ]
    result = sol.minCostClimbingStairs(cost)
    print(result)

if __name__ == "__main__":
    main()
