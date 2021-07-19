class Solution:
    def findNthDigit(self, n):
        start=1
        dight=1
        while n>9*start*dight:
            n-=9*start*dight
            start*=10
            dight+=1
        num=start+(n-1)//dight
        index=(n-1)%dight
        return int(str(num)[index])

if __name__ == "__main__":
    S=Solution()
    print(S.findNthDigit(15))