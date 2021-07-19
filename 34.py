class Solution:
    def majorityElement(self, nums):
        n=len(nums)//2
        dic={}
        for i in nums:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
        res=[]
        for k,v in dic.items():
            if v>n:
                res.append(k)
        return res

if __name__ == "__main__":
    S=Solution()
    li=[1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(S.majorityElement(li))
