#解法一：
class Solution:
    def findRepeatNumber(self, nums) -> int:
        n = len(nums)
        for i in range(n):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]
            #   注意这里不要写成nums[i], nums[nums[i]] = nums[nums[i]], nums[i]

searchnumber=Solution()
nums=[2, 3, 1, 0, 2, 5, 3]
number=searchnumber.findRepeatNumber(nums)
print(number)
#解法二：
class Solution:
    def findRepeatNumber(self, nums):
        Dict={}
        for num in nums:
            if num not in Dict:
                Dict[num]=1
            else:
                return num

