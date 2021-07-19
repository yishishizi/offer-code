class SignalNode(object):
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SignalList(object):
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
        print('')

    def add(self,item):
        node=SignalNode(item)
        node.next=self.__head
        self.__head=node

    def append(self,item):
        node=SignalNode(item)
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

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
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False


    def remove(self,item):
        #node=SignalNode(item)
        pre,cur=None,self.__head
        while cur!=None:
            if cur.elem == item:
                if cur==self.__head:
                    cur=cur.next
                else:
                    pre.next=cur.next
                    cur = cur.next
            else:
                pre=cur
                cur=cur.next

    def reverseList(self):
        head=self.__head
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    # def remove(self,item):
    #     #node=SignalNode(item)
    #     pre,cur=None,self.__head
    #     while cur!=None:
    #         if cur.elem == item:
    #             if cur==self.__head:
    #                 cur=cur.next
    #             else:
    #                 pre.next=cur.next
    #             break
    #         else:
    #             pre=cur
    #             cur=cur.next










if __name__ == "__main__":
    ll = SignalList()
    #print(ll.is_empty())
    #print(ll.length())
    # ll.add(9)

    ll.append(1)
    #print(ll.is_empty())
    #print(ll.length())

    ll.append(2)
    #ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    #ll.travel()
    # ll.add(7)
    # ll.insert(3, 100)
    # ll.insert(4, 100)# 7 1 2 100 3 4 5 6
    # ll.insert(6, 100)
    ll.travel()
    ll.reverseList()
    # ll.search(10000)
    # ll.remove(100)
    # ll.travel()

