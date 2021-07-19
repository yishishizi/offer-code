class Solution:
    def twoSum(self, nums, target):
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left]+nums[right]==target:
                return [nums[left],nums[right]]
            elif nums[left]+nums[right]>target:
                right-=1
            else:
                left+=1
        return None

if __name__ == "__main__":
    S=Solution()
    nums = [15,15,16,22,53,60]
    target = 15
    print(S.twoSum(nums,target))