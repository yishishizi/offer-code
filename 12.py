# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         str_n=str(n)
#         count=0
#         for i in str_n:
#             if int(i)==1:
#                count+=1
#         return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res

if __name__=="__main__":
    S=Solution()
    n=bin(11).replace('0b','')
    print(S.hammingWeight(n))

