class Solution:
    def nthUglyNumber(self, n):
        dp=[0]*(n+1)
        dp[1]=1
        p2,p3,p5=1,1,1
        for i in range(2,n+1):
            dp[i]=min(dp[p2]*2,dp[p3]*3,dp[p5]*5)
            if dp[i]==dp[p2]*2:
                p2+=1
            if dp[i]==dp[p3]*3:
                p3+=1
            if dp[i]==dp[p5]*5:
                p5+=1
        return dp[-1]


if __name__ == "__main__":
    S=Solution()
    print(S.nthUglyNumber(15))
