class Solution:
    def constructArr(self, a):
        if a==[]:return []
        B=[0]*len(a)
        tmp,B[0]=1,1
        for i in range(1,len(a)):
            B[i]=a[i-1]*B[i-1]

        for i in range(len(a)-1,-1,-1):
            B[i]=tmp*B[i]
            tmp=a[i]*tmp
        return B

if __name__ == "__main__":
    S=Solution()
    a=[1,2,3,4,5]
    print(S.constructArr(a))



