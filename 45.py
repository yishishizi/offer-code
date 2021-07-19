class Solution:
    def search(self, nums, target):
        n=len(nums)
        start=0
        end=n-1
        #查找右边界
        while start<=end:
            mid=(start+end)//2
            if nums[mid]<=target:
                start=mid+1
            if nums[mid]>target:
                end=mid-1
        right=start
        # 查找左边界
        start=0
        while start<=end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            if nums[mid] >= target:
                end = mid - 1
        left=end
        return right - left - 1
        # n = len(nums)-1
        # left = 0
        # right = n
        # while nums[left] != target and left < n:
        #     left += 1
        # while nums[right] != target and right >= 0:
        #     right -= 1
        # if right < left:
        #     return 0
        # else:
        #     return right - left + 1

if __name__ == "__main__":
    S=Solution()
    nums = [5,7,7,8,8,10]
    target = 8
    print(S.search(nums,target))
