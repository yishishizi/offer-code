class Solution:
    def exchange(self, nums):
        a=[]
        b=[]
        for i in nums:
            if i % 2 == 1:
                a.append(i)
            else:
                b.append(i)
        return a+b


if __name__=="__main__":
    S=Solution()
    num=[1,2,3,4]
    print(S.exchange(num))