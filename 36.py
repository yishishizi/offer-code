class Solution:
    def maxSubArray(self, nums):
        cursum=0
        res=nums[0]
        for num in nums:
            if cursum>0:
                cursum+=num
            else:
                cursum=num
            res=max(res,cursum)
        return res

if __name__ == "__main__":
    S=Solution()
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    print(S.maxSubArray(nums))
