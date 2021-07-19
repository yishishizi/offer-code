class Solution:
    def twoSum(self, nums, target):
        def bsearch(nums,target,vid):
            start=0
            end=len(nums)-1
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return False
        for i in range(len(nums)):
            m=bsearch(nums,target-nums[i],i)
            if m:break
        if m is False:return None
        return [nums[i],nums[m]]

if __name__ == "__main__":
    S=Solution()
    nums = [15,15,16,22,53,60]
    target = 15
    print(S.twoSum(nums,target))


