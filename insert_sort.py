# def insert_sort(alist):
#     for j in range(1,len(alist)):
#         i = j
#         while i>0:
#             if alist[i]<alist[i-1]:
#                 alist[i],alist[i-1]=alist[i-1],alist[i]
#                 i-=1
#             else:
#                 break

def insert_sort(alist):
    for j in range(1,len(alist)):#外层循环，从无序序列中取出多少个元素，执行内层循环的次数
        for i in range(j,0,-1):#内存循环，从无序序列取出第一个原始，即i位置的元素，然后将其插入到有序序列中正确的位置
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
            else:
                break



if __name__=="__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(li)
    print(li)
    li1 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    insert_sort(li1)
    print(li1)