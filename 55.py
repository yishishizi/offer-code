class Solution:
    def dicesProbability(self, n):
        dp=[1/6]*6
        for i in range(2,n+1):
            tmp=[0]*(5*i+1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j+k]+=dp[j]/6
            dp=tmp
        return dp

if __name__ == "__main__":
    S=Solution()
    n=4
    print(S.dicesProbability(n))

