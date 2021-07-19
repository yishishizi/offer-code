class Node():
    def __init__(self,item):
        self.elem=item
        self.lchild=None
        self.rchild=None

class Tree():
    def __init__(self):
        self.root=None

    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
            return
        queue=[self.root]
        while queue:
            cur_node = queue.pop(0)#pop---删除第一个元素
            if cur_node.lchild is None:
                cur_node.lchild=node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild=node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        if self.root is None:
            return
        queue=[self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)




    def preorder(self,node):
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)


    def preorder_iter(self):
        if self.root is None:
            return
        stack=[]
        stack.append(self.root)
        while stack:
            node=stack.pop()
            if node:
                print(node.elem, end=" ")
                stack.append(node.rchild)
                stack.append(node.lchild)





    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        self.inorder(node.rchild)

    def inorder_iter(self):
        if self.root is None:
            return
        stack=[]
        root=self.root
        while root or stack:
            if root:
                stack.append(root)
                root = root.lchild
            else:
                root=stack.pop()
                print(root.elem, end=" ")
                root=root.rchild


    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=" ")

    def postorder_iter(self):
        if self.root is None:
            return
        stack=[]
        prev=None
        root = self.root
        while root or stack:
            while root:
                stack.append(root)
                root = root.lchild
            root=stack.pop()
            if not root.rchild or root.rchild==prev:
                print(root.elem, end=" ")
                prev=root
                root=None
            else:
                stack.append(root)
                root=root.rchild
class Solution():
    def isSubStructure(self, A, B):
        def isSame(tree1,tree2):
            t1=tree1.root
            t2=tree2.root
            if t2 is None:return True
            if t1 is None: return False
            if t1.elem != t2.elem :
                return False
            return isSame(t1.lchild,t2.lchild) and isSame(t1.rchild,t2.rchild)
        if A is None or B is None: return False
        if isSame(A,B):return True
        return self.isSubStructure(A.rchild,B) or self.isSubStructure(A.lchild,B)
    #
    #
    # def equal(self,A,B):
    #     queue=[(A,B)]
    #     while queue:
    #         nodeA,nodeB=queue.pop(0)
    #         if nodeA is None or nodeA.elem != nodeB.elem:
    #             return False
    #         if nodeB.lchild:
    #             queue.append((nodeA.lchild,nodeB.lchild))
    #         if nodeB.rchild:
    #             queue.append((nodeA.rchild,nodeB.rchild))
    #     return True


        # roota=A.root
        # rootb=B.root
        # if rootb is None or roota is None:
        #     return False
        # queuel=[roota]
        # while queuel:
        #     cur_node = queuel.pop(0)
        #     if cur_node.elem==rootb.elem:
        #         while rootb:
        #             if rootb.lchild is None: return True
        #             if cur_node.lchild is None and not rootb.lchild: return False
        #             if not cur_node.lchild and not rootb.lchild:
        #                 if cur_node.lchild==rootb.lchild:
        #                     cur_node=cur_node.lchild
        #                     rootb=rootb.lchild
        #             # if cur_node.rchild:
        #             #     if cur_node.rchild==rootb.rchild or rootb.rchild is None:
        #             #         cur_node=cur_node.rchild
        #             #         rootb=rootb.rchild
        #             # if prev ==cur_node:
        #             #     return False
        #         return True
        #     if cur_node.lchild is not None:
        #         queuel.append(cur_node.lchild)
        #     if cur_node.rchild is not None:
        #         queuel.append(cur_node.rchild)
        # return False




if __name__ == "__main__":
    A=[1,2,3]
    treeA=Tree()
    for i in A:
        treeA.add(i)
    B=[3,1]
    treeB = Tree()
    for i in B:
        treeB.add(i)
    S=Solution()
    print(S.isSubStructure(treeA,treeB))
    A1 = [3,4,5,1,2]
    treeA1 = Tree()
    for i in A1:
        treeA1.add(i)
    B1 = [4,1]
    treeB1 = Tree()
    for i in B1:
        treeB1.add(i)
    S = Solution()
    print(S.isSubStructure(treeA1, treeB1))
