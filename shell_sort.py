def shell_sort(alist):
    n=len(alist)
    gap=n//2
    while gap>=1:
        #插入算法与普通的插入算法的区别就是gap步长
        for j in range(gap,n):
            i=j
            while i>0:
                if alist[i]<alist[i-gap] and i-gap>=0:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    i-=gap
                else:
                    break
        gap//=2
        print(alist)


if __name__=="__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(li)
    print(li)