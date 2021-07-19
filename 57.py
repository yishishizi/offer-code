class Solution:
    def lastRemaining(self, n, m):
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x

if __name__ == "__main__":
    S=Solution()
    n = 5
    m = 3
    print(S.lastRemaining(n,m))
