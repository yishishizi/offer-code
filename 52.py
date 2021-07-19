class Solution:
    def findContinuousSequence(self, target):
        if target==0 or target==1:return None
        n=target//2+1
        li = [i for i in range(1,n + 1)]
        res=[]
        left,right=0,0
        while left<=n and right<=n:
            s=sum(li[left:right])
            if s<target:
                right+=1
            elif s>target:
                left+=1
            else:
                res.append(li[left:right])
                left+=1
        return res

if __name__ == "__main__":
    S=Solution()
    target = 3
    print(S.findContinuousSequence(target))

