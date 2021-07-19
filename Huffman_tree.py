class Node():
    def __init__(self,item):
        self.lchild=None
        self.rchild = None
        self.parent = None
        self.elem=item

class Huffman_tree():
    def __init__(self):
        self.root=None

    def creat_tree(self,node):
        nodelist=node[:]
        while len(nodelist)>1:
            nodelist.sort(key=lambda item:item.elem)#key=lambda item:item.elem
            node_left=nodelist.pop(0)
            node_right=nodelist.pop(0)

            node_father=Node(node_left.elem+node_right.elem)
            node_father.lchild=node_left
            node_father.rchild=node_right
            node_left.parent=node_father
            node_right.parent=node_father
            nodelist.append(node_father)


        nodelist[0].parent=None
        self.root=nodelist[0]
        return self.root

    def travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)



if __name__ == "__main__":
    tree=Huffman_tree()
    node=[7,5,2,4]
    n=len(node)
    for i in range(n):
        node.append(Node(node[0]))
        node.pop(0)
    tree.creat_tree(node)
    tree.travel()
    print(' ')

