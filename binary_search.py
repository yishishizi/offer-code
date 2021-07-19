def binary_search(alist,item):
    n=len(alist)
    if n>0:
        mid=n//2
        if alist[mid]==item:
            return True
        elif alist[mid]>item:
            return binary_search(alist[:mid],item)
        else:
            return binary_search(alist[mid+1:],item)
    else:
        return False

def binary_search_(alist,item):
    n=len(alist)
    start=0
    end=n-1
    while start<=end:
        mid = (start + end) // 2
        if alist[mid]==item:
                return True
        elif alist[mid] > item:
            end=mid-1
        else:
            start=mid+1
    return False

if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(li, 55))
    print(binary_search(li, 100))
    print(binary_search_(li, 55))
    print(binary_search_(li, 100))