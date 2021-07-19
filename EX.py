# class Solution:
#     def majorityElement(self, nums):
        # sum, cursum = nums[0],0
        # for num in nums:
        #     if cursum>=0:
        #         cursum+=num
        #     else:
        #         cursum=num
        #     sum = max(sum, cursum)
        # return sum
        # n=len(nums)//2
        # dic={}
        # for num in nums:
        #     if num in dic:
        #         dic[num]+=1
        #     else:
        #         dic[num]=1
        # for k,v in dic.items():
        #     if v>n:
        #         return k

# class Solution:
#     def minNumber(self, nums):
#         def quick_sort(arr,start,end):
#             if start>end:return
#             vals=arr[start]
#             low=start
#             high=end
#             while low<high:
#                 while low<high and arr[high]+vals>=vals+arr[high]:
#                     high-=1
#                 arr[low]=arr[high]
#                 while low<high and arr[low]+vals<vals+arr[low]:
#                     low+=1
#                 arr[high]=arr[low]
#             arr[high]=vals
#             quick_sort(arr,start,low-1)
#             quick_sort(arr,low+1,end)
#         s=[str(num) for num in nums]
#         quick_sort(s,0,len(s)-1)
#         return ''.join(s)

# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         dp=[0]*(n+1)
#         dp[1]=1
#         p,q,k=1,1,1
#         for i in range(2,n+1):
#             dp[i]=min(2*dp[p],3*dp[q],5*dp[k])
#             if dp[i]==2*dp[p]:
#                 p+=1
#             if dp[i]==3*dp[q]:
#                 q+=1
#             if dp[i]==5*dp[k]:
#                 k+=1
#         return dp[n]

# class Solution:
#     def missingNumber(self, nums):
#         n = len(nums)+1
#         left=0
#         right=len(nums)-1
#         while left<=right:
#             if nums[left]+nums[right]==n-1:
#                 left+=1
#                 right-=1
#             else:
#                 break
#         if nums[left]+nums[right]<n-1:
#             return nums[right]+1
#         if nums[left]+nums[right]>n-1:
#             return nums[left]-1
#         if nums[left] + nums[right] == 2:
#             return 1

# class Solution:
#     def twoSum(self, nums, target):
#         start=0
#         end=len(nums)-1
#         while start<=end:
#             if nums[start]+nums[end]<target:
#                 start+=1
#             elif nums[start]+nums[end]>target:
#                 end-=1
#             else:
#                 return [nums[start],nums[end]]

# class Solution:
#     def findContinuousSequence(self, target):
#         left=1
#         right=1
#         sum=0
#         n=target//2
#         res=[]
#         while left<=n:
#             if sum<target:
#                 sum+=right
#                 right+=1
#             elif sum>target:
#                 sum-=left
#                 left+=1
#             else:
#                 res.append(list(range(left,right)))
#                 sum-=left
#                 left+=1
#         return res


# class Solution:
#     def maxSlidingWindow(self, nums, k: int) :
#         deque = []
#         res, n = [], len(nums)
#         for i, j in zip(range(1 - k, n + 1 - k), range(n)):
#             # 删除 deque 中对应的 nums[i-1]
#             if i > 0 and deque[0] == nums[i - 1]:
#                 deque.pop(0)
#             # 保持 deque 递减
#             while deque and deque[-1] < nums[j]:
#                 deque.pop()
#             deque.append(nums[j])
#             # 记录窗口最大值
#             if i >= 0:
#                 res.append(deque[0])
#         return res

# class Solution:
#     def isStraight(self, nums) -> bool:
#         dic=set()
#         ma,mi=0,14
#         for num in nums:
#             if num==0:continue
#             if num in dic:return False
#             dic.add(num)
#             if ma<num:
#                 ma=num
#             if mi>num:
#                 mi=num
#         return ma-mi<5

# class Solution:
#     def maxProfit(self, prices):
#         if prices == [] or len(prices) == 1:
#             return 0
#         res = 0
#         n = len(prices)
#         for i in range(1, n):
#             res = max(res, prices[i] - min(prices[:i]))
#         return res

class Solution:
    def constructArr(self, a):
        if a==[]:
            return []
        tmp=1
        res=[]
        for i in range(len(a)):
            if i==0:
                tmp=1
            else:
                tmp*=a[i-1]
            res.append(tmp)
        for i in range(len(a)-1,-1,-1):
            if i ==len(a)-1:
                tmp=1
            else:
                tmp*=a[i+1]
            res[i]=res[i]*tmp
        return res

if __name__ == "__main__":
    S=Solution()
    n= [1,2,3,4,5]
    print(S.constructArr(n))






