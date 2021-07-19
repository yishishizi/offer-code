class SignalNode(object):
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SignalcycList(object):
    def __init__(self,node=None):
        self.__head=node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        n=1
        cur=self.__head
        while cur.next!=self.__head:
            n+=1
            cur=cur.next
        return n

    def travel(self):
        if self.is_empty():
            return None
        cur=self.__head
        while cur.next!=self.__head:
            print(cur.elem,end=',')
            cur=cur.next
        print(cur.elem)


    def add(self,item):
        node=SignalNode(item)
        if self.is_empty():
            self.__head=node
            node.next=node
        cur=self.__head
        while cur.next!=self.__head:
            cur=cur.next
        node.next = self.__head
        cur.next=node
        self.__head = node

    def append(self,item):
        node=SignalNode(item)
        if self.is_empty():
            self.__head=node
            node.next = node
        else:
            cur=self.__head
            while cur.next!=self.__head:
                cur=cur.next
            cur.next=node
            node.next=self.__head

    def insert(self,pos,item):#pos起始从0开始
        node=SignalNode(item)
        n=0
        pre = self.__head
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            while n < (pos-1):
                pre = pre.next
                n += 1
            node.next = pre.next
            pre.next = node

    def search(self,item):
        cur=self.__head
        if self.is_empty():
            return False
        while cur.next!=self.__head:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        if cur.elem==item:
            return True
        return False


    def remove(self,item):
        #node=SignalNode(item)
        if self.is_empty():
            return None
        pre,cur=None,self.__head
        while cur.next!=self.__head:
            if cur.elem == item:
                if cur==self.__head:
                    #头结点
                    #找尾节点
                    rear=self.__head
                    while rear.next!=self.__head:
                        rear=rear.next
                    cur=cur.next
                    rear.next=cur
                    self.__head=cur#把当前的cur标识为头节点
                else:
                    #中间节点
                    pre.next=cur.next
                    cur = cur.next
            else:
                pre=cur
                cur=cur.next
        #退出循，cur指向尾节点
        if cur.elem==item:
            if cur==self.__head:
                self.__head=None
            else:
                pre.next = cur.next



if __name__ == "__main__":
    ll = SignalcycList()
    # print(ll.is_empty())
    # print(ll.length())
    ll.add(9)

    ll.append(1)
    # print(ll.is_empty())
    # print(ll.length())

    ll.append(2)
    # ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # ll.travel()
    ll.add(7)
    ll.insert(3, 100)
    ll.insert(4, 100)  # 7 1 2 100 3 4 5 6
    ll.insert(6, 100)
    ll.travel()
    ll.search(10000)
    ll.remove(7)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(100)
    ll.travel()