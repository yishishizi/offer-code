class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        i,j=len(matrix)-1,0#i代表行，j代表列
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j]>target:i-=1
            elif matrix[i][j]<target:j+=1
            else:return True
        return False