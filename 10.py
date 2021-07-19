class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited=set([(0,0)])
        for i in range(m):
            for j in range(n):
                if ((i-1,j) in visited or (i,j-1) in visited) and self.get(i)+self.get(j)<=k:
                    visited.add((i,j))
        return len(visited)

    def get(self,x):
        sum=0
        while x!=0:
            sum+=x%10
            x=x//10
        return sum

if __name__=="__main__":
    S=Solution()
    print(S.movingCount(2,3,1))