class Solution:
    def maxValue(self, grid):
        m,n=len(grid),len(grid[0])
        dp=[[0]*(n+1) for i in range(m+1)]#[[0]*(n+1)]*(m+1)
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
        return dp[m][n]

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if i==0 and j==0: continue
        #         if i==0 :
        #             grid[i][j]+=grid[i][j-1]
        #         if j==0 :
        #             grid[i][j]+=grid[i-1][j]
        #         else:
        #             grid[i][j]+=max(grid[i-1][j],grid[i][j-1])
        # return grid[-1][-1]

if __name__ == "__main__":
    S=Solution()
    n=[[1,3,1],[1,5,1],[4,2,1]]
    print(S.maxValue(n))