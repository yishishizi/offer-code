# class Solution(object):
#     def minArray(self,numbers):
#         if len(numbers)==0:
#             return numbers[0]
#         start=0
#         end=len(numbers)-1
#         while start<end:
#             mid = start + (end - start) // 2
#             if numbers[mid]>numbers[end]:
#                 start=mid+1
#             elif numbers[mid]<numbers[end]:
#                 end=mid
#             else:
#                 end=-1
#         return numbers[start]

class Solution:
    def minArray(self, numbers):
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]


if __name__=="__main__":
    numbers=[3,1,1]
    #numbers = [2, 2, 2, 0, 1]
    S=Solution()
    ii=S.minArray(numbers)
    print(ii)


