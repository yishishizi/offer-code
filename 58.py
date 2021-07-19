class Solution:
    def maxProfit(self, prices):
        if prices==[]:return 0
        vals,minprice=0,int(1e9)
        for i in range(len(prices)):
            vals=max(prices[i]-minprice,vals)
            minprice=min(prices[i],minprice)
        return vals


if __name__ == "__main__":
    S=Solution()
    n= [7,6,8,3,1]
    print(S.maxProfit(n))

