class Solution:
    def minNumber(self, nums):
        def quick_sort(arr,start,end):
            if start>=end: return
            mid_values=arr[start]
            low=start
            high=end
            while low<high:
                while low<high and arr[high]+mid_values>=mid_values+arr[high]:
                    high-=1
                arr[low]=arr[high]
                while low<high and arr[low]+mid_values<mid_values+arr[low]:
                    low+=1
                arr[high]=arr[low]
            arr[high]=mid_values
            quick_sort(arr,start,low-1)
            quick_sort(arr,low+1,end)
        vals=[str(num) for num in nums]
        quick_sort(vals,0,len(vals)-1)
        return ''.join(vals)

if __name__ == "__main__":
    S=Solution()
    arr=[1,1,1]
    print(S.minNumber(arr))