class Solution(object):
    def minArray(self,numbers):
        # min_pos=0
        # for i in range(1,len(numbers)):
        #     if numbers[min_pos]>numbers[i]:
        #         min_pos=i
        # return numbers[min_pos:]+numbers[:min_pos],numbers[min_pos]
        left = 0
        right = len(numbers) - 1
        while left<= right:
            mid_vals = (left + right) // 2
            if numbers[mid_vals] > numbers[right]:
                left = mid_vals + 1
            if numbers[mid_vals] <= numbers[right]:
                right = mid_vals - 1
        return numbers[left]

if __name__=="__main__":
    #numbers=[3,4,5,1,2]
    numbers = [2, 2, 2, 0, 1]
    S=Solution()
    min=S.minArray(numbers)

    print(min)




            
