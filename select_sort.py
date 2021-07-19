def select_sort(alist):
    for i in range(len(alist)-1):
        min_=i
        for j in range(i+1,len(alist)):
            if alist[min_]>alist[j]:
                min_=j
        alist[i],alist[min_]=alist[min_],alist[i]

if __name__=="__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    select_sort(li)
    print(li)