class Solution:
    def verifyPostorder(self, postorder):
        if postorder ==[]:
            return True
        root=postorder[-1]
        cur_index=0
        for i in range(len(postorder)):
            if postorder[i]>=root:
                cur_index=i
                break
        lchild=postorder[:cur_index]
        rchild=postorder[cur_index:-1]#这个地方要把最后一个根节点去掉
        for elem in rchild:
            if elem<root:
                return False
        return self.verifyPostorder(lchild) and self.verifyPostorder(rchild)





if __name__ == "__main__":
    a=[4, 8, 6, 12, 16, 14, 10]
    S=Solution()
    print(S.verifyPostorder(a))