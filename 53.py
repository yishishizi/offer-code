class Solution:
    def reverseWords(self, s):
        s.strip()
        res=[]
        left,right=len(s)-1,len(s)-1
        while left>=0:
            while s[left]!=' ' and left>=0:
                left-=1
            res.append(s[left+1:right+1])
            while s[left]==' ':
                left-=1
            right=left
        return ' '.join(res)

if __name__ == "__main__":
    S=Solution()
    s=" the sky is blue"
    print(S.reverseWords(s))


