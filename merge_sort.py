def merge_sort(alist):
    n=len(alist)
    if n<=1:
        return alist
    mid=n//2
    #left和righ是划分之后形成的有序列表
    left=merge_sort(alist[:mid])
    right=merge_sort(alist[mid:])
    l,r=0,0
    result=[]
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    result+=left[l:]
    result+=right[r:]
    return result
if __name__=="__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    result=merge_sort(li)
    print(result)
