class Solution:
    def printNumbers(self, n: int):
        # a=[]
        # b=10**n
        # for i in range(1,b):
        #     a.append(i)
        # return a
        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(int(s))
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res

if __name__=="__main__":
    S=Solution()
    print(S.printNumbers(2))