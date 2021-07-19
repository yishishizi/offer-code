def bubble_sort(alist):
    for j in range(len(alist)-1):#从头走到尾这样的操作要执行多少次
        count=0
        for i in range(len(alist)-1-j):#每一次遍历，两两比较列表中数的大小
            if alist[i]>alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count+=1
        if count==0:#[32,15,5,1,48,49,50],遍历到48,49,50的时候，顺序已经正确，这时候不在执行外层j的循环，直接跳出
            return

if __name__=="__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(li)
    print(li)