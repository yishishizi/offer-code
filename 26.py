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

    def levelOrder(self):
        root=self.root
        visited=1
        li = []
        if root is None:
            return li
        queue = [root]
        while queue:
            tmp = []
            n=len(queue)
            for i in range(n):
                cur_node = queue.pop(0)
                tmp.append(cur_node.elem)
                if cur_node.lchild: queue.append(cur_node.lchild)
                if cur_node.rchild: queue.append(cur_node.rchild)
            if visited % 2== 0:
                tmp=tmp[::-1]
            visited+=1
            li.append(tmp)
        return li



if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.breadth_travel()
    print(tree.levelOrder())