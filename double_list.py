from linked_list import SignalList
class Node():
    def __init__(self,item):
        self.elem=item
        self.next=None
        self.prev=None

class DoubleList():
    def __init__(self,node=None):
        self.__head=node

    def is_empty(self):
        return self.__head is None

    def length(self):
        n=0
        cur=self.__head
        while cur:
            n+=1
            cur=cur.next
        return n

    def travel(self):
        cur=self.__head
        while cur:
            print(cur.elem,end=',')
            cur=cur.next
        print("")

    def add(self,item):
        node = Node(item)
        if self.__head is None:
            self.__head=node
        else:
            node.next = self.__head  # 这里的head理解为第一个节点
            self.__head = node  # 把node标识为头节点
            node.next.prev = node



    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
            node.prev=cur

    def insert(self,pos,item):#pos起始从0开始
        node=Node(item)
        n=0
        cur = self.__head
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            while n < pos-1:
                cur = cur.next
                n += 1
            node.next = cur.next
            cur.next.prev = node
            cur.next=node
            node.prev=cur

    def search(self,item):
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False


    def remove(self,item):
        #node=SignalNode(item)
        cur=self.__head
        while cur!=None:
            if cur.elem == item:
                if cur==self.__head:
                    cur=cur.next
                    if cur.next:#判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next=cur.next
                    if cur.next:
                        cur.next.prev=cur.prev
                    cur = cur.next
            else:
                cur=cur.next


if __name__ == "__main__":
    dll = DoubleList()
    print(dll.is_empty())
    print(dll.length())
    dll.add(7)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.insert(3, 100)  # 9 8 1 100 2 3456
    dll.travel()
    dll.insert(10, 200)
    dll.insert(3, 100)
    dll.insert(4, 100)  # 7 1 2 100 3 4 5 6
    dll.insert(6, 100)
    dll.travel()
    dll.search(10000)
    dll.remove(100)
    dll.travel()
    dll.remove(200)
    dll.travel()
