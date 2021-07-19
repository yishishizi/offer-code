class Solution:
    def maxValue(self, grid):
        m,n=len(grid),len(grid[0])
        dp=[0]*(n+1)
        for i in range(m):
            for j in range(1,n+1):
                dp[j]=max(dp[j-1],dp[j])+grid[i][j-1]
        return dp[-1]

if __name__ == "__main__":
    S=Solution()
    grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(S.maxValue(grid))