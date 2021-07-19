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

    def getKthFromEnd(self,k,lens):
        count=1
        cur=self.__head
        n=lens-k + 1
        while count!=n and cur:
            cur=cur.next
            count+=1
        self.__head=cur
        return self.__head

    def reverseList(self):
        pre,cur=None,self.__head
        while cur:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        self.__head=pre
        return self.__head






if __name__ == "__main__":
    ll = SignalList()
    ll.add(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.travel()
    ll.reverseList()
    ll.travel()