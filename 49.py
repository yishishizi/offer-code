class Solution:
    def singleNumbers(self, nums):
        res=0
        x,y,m=0,0,1
        for num in nums:
            res^=num
        while res&m==0:#参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
            m<<=1
        for num in nums:
            if num&m: x^=num
            else:y^=num
        return [x,y]

if __name__ == "__main__":
    S=Solution()
    nums=[4,1,4,6]
    print(S.singleNumbers(nums))
