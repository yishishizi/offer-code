def quick_sort(alist,start,end):
    if start>=end:
        return
    mid_value = alist[start]
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1

        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[high]=mid_value
    quick_sort(alist,start,low-1)
    quick_sort(alist,low+1,end)



if __name__=="__main__":
    li = [5,3,4,2,1]
    quick_sort(li,0,len(li)-1)
    print(li)