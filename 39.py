class Solution:
    def translateNum(self, num):
        s=str(num)
        dp=[0]*(len(s)+1)
        dp[0],dp[1]=1,1
        for i in range(2,len(s)+1):
            tmp=s[i-2:i]#i取不到，实际为i-1和i-2
            if tmp>='10' and tmp<='25':
                dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]
        return dp[-1]
        # a=b=1
        # y=num%10
        # while num:
        #     num=num//10
        #     x=num%10
        #     a,b=(a+b if 10<=x*10+y<=25 else a),a
        #     y=x
        # return a
if __name__ == "__main__":
    S=Solution()
    n=12258
    print(S.translateNum(n))
