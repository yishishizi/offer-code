class Solution:
    def getLeastNumbers(self, arr, k):
        def quick_sort(alist, start, end):
            if start >= end:
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
            alist[high] = mid_value
            quick_sort(alist, start, low - 1)
            quick_sort(alist, low + 1, end)
        n=len(arr)-1
        quick_sort(arr,0,n)
        return arr[:k]




if __name__ == "__main__":
    S=Solution()
    k=2
    li=[0,1,2,1]
    print(S.getLeastNumbers(li,k))
