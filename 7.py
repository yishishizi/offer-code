# class Solution:
#     def fib(self, n):
#         if n==0:
#             return 0
#         elif n==1:
#             return 1
#         else:
#             return self.fib(n-1)+self.fib(n-2)
# class Solution:
#     def fib(self, n):
#         a=[0]*(n+1)
#         return self.recurse(a,n)
#
#     def recurse(self,a,n):
#         if n == 0:
#             return 0
#         if n==1:
#             return 1
#         if a[n]!=0:
#             return a[n]
#         a[n]=self.fib(n-1)+self.fib(n-2)
#         return a[n]
class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        low = 0
        high = 1
        for i in range(2, n + 1):
            sum = (low + high)%1000000007
            low = high
            high = sum
        return high




S=Solution()
a=S.fib(0)
print(a)
b=S.fib(1)
print(b)
c=S.fib(2)
print(c)
d=S.fib(37)
print(d)