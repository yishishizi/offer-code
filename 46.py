class Solution:
    def missingNumber(self, nums):
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==mid:
                start=mid+1
            else:
                end=mid-1
        return start
        # if nums==[]:return None
        # for i in range(len(nums)+1):
        #     if nums==[]:return i
        #     if i!=nums.pop(0):
        #         return i

if __name__ == "__main__":
    S=Solution()
    nums=[0]
    print(S.missingNumber(nums))
