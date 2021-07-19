class Solution:
    def exchange(self, nums):
        left=0
        right=len(nums)-1
        while left<right:
            while nums[left] % 2 == 1:
                left+=1
                if left>right:
                    return nums
            while nums[right] % 2 ==1:
                nums[left],nums[right]=nums[right],nums[left]
            right-=1
        return nums

if __name__=="__main__":
    S=Solution()
    num=[1,3,5]
    print(S.exchange(num))
