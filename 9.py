class Solution:
    def exist(self, board, word):
        m,n,k=len(board),len(board[0]),0#m代表行数，n代表列数
        for i in range(m):
            for j in range(n):
                if self.DFS(k,i,j,m,n,board,word):#找首字母符合的字母
                    return True
        return False

    def DFS(self,k,i,j,m,n,board,word):
        if i<0 or i>=m or j<0 or j>=n or board[i][j]!=word[k]:#board的长度是5，但区间为0-4，当i或j等于5时越界了
            return False
        if k==len(word)-1:
            return True
        tmp=board[i][j]
        board[i][j]='\0'
        res=self.DFS(k+1,i-1,j,m,n,board,word) or self.DFS(k+1,i+1,j,m,n,board,word) or self.DFS(k+1,i,j-1,m,n,board,word) or self.DFS(k+1,i,j+1,m,n,board,word)
        board[i][j]=tmp
        return res

if __name__=="__main__":
    S=Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "BCCED"
    print(S.exist(board,word))













