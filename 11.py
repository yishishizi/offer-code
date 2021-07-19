class Solution:
    def cuttingRope(self, n: int) -> int:
        if n<=3:
            return n-1
        a,b=n//3,n%3
        if b==0:
            res=3**a
        if b==1:
            res=3**(a-1)*4
        if b==2:
            res=3**a*2
        return res

if __name__=="__main__":
    S=Solution()
    print(S.cuttingRope(2))
    print(S.cuttingRope(10))