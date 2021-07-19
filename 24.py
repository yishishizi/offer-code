class Solution:
    def spiralOrder(self, matrix):
        m,n=len(matrix),len(matrix[0])
        ord=[]
        left,right,top,bottom=0,m-1,0,n-1#left,right是列，top,bottom是行
        while left<=right and top <=bottom:
            for i in range(left,right+1):
                ord.append(matrix[top][i])
            for j in range(top+1,bottom+1):
                ord.append(matrix[j][right])
            if left<right and top<bottom:
                for i in range(right-1,left,-1):
                    ord.append(matrix[bottom][i])
                for j in range(bottom,top,-1):
                    ord.append(matrix[j][left])
            left,right,top,bottom=left+1,right-1,top+1,bottom-1
        return ord

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    S=Solution()
    S.spiralOrder(matrix)