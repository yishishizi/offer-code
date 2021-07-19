class Solution:
    def isStraight(self, nums):
        dic = set()
        max_num, min_num = 0, 14
        for num in nums:
            if num in dic: return False
            if num == 0: continue
            max_num = max(num, max_num)
            min_num = min(num, min_num)
            dic.add(num)
        return max_num - min_num < 5

if __name__ == "__main__":
    S=Solution()
    n=[1,2,3,4,5]
    print(S.isStraight(n))
