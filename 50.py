class Solution:
    def singleNumbers(self, nums):
        dic = {}
        li = []
        for i in nums:
            dic[i] = not i in dic
        for k, v in dic.items():
            if v: li.append(k)
        return li

if __name__ == "__main__":
    S=Solution()
    nums = [3,4,3,3]
    print(S.singleNumbers(nums))