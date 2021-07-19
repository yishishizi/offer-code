from linked_list import SignalNode,SignalList
# class SignalNode(object):
#     def __init__(self,elem):
#         self.elem=elem
#         self.next=None

# class SignalList(object):
#     def __init__(self,node=None):
#         self.__head=node
#
#     def is_empty(self):
#         return self.__head is None
#
#     def length(self):
#         n=0
#         cur=self.__head
#         while cur:
#             n+=1
#             cur=cur.next
#         return n
#
#     def travel(self):
#         cur=self.__head
#         while cur:
#             print(cur.elem,end=',')
#             cur=cur.next
#         print('')
#
#     def add(self,item):
#         node=SignalNode(item)
#         node.next=self.__head
#         self.__head=node
#
#     def append(self,item):
#         node=SignalNode(item)
#         if self.is_empty():
#             self.__head=node
#         else:
#             cur=self.__head
#             while cur.next!=None:
#                 cur=cur.next
#             cur.next=node
#
#     def insert(self,pos,item):#pos起始从0开始
#         node=SignalNode(item)
#         n=0
#         pre = self.__head
#         if pos<=0:
#             self.add(item)
#         elif pos>(self.length()-1):
#             self.append(item)
#         else:
#             while n < (pos-1):
#                 pre = pre.next
#                 n += 1
#             node.next = pre.next
#             pre.next = node
#
#     def search(self,item):
#         cur=self.__head
#         while cur!=None:
#             if cur.elem==item:
#                 return True
#             else:
#                 cur=cur.next
#         return False
#
#
#     def remove(self,item):
#         #node=SignalNode(item)
#         pre,cur=None,self.__head
#         while cur!=None:
#             if cur.elem == item:
#                 if cur==self.__head:
#                     cur=cur.next
#                 else:
#                     pre.next=cur.next
#                     cur = cur.next
#             else:
#                 pre=cur
#                 cur=cur.next

class HashTable(object):
    def __init__(self,size=101):
        self.size=size
        self.T=[SignalList() for i in range(self.size)]

    def h(self,k):
        return  k % self.size

    def insert(self,item):
        i=self.h(item)
        if self.search(item):
            print("重复插入")
        else:
            self.T[i].append(item)

    def search(self,item):
        i=self.h(item)
        return self.T[i].search(item)

if __name__ == "__main__":
    ll = SignalList()
    # ll.append(1)
    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # ll.append(5)
    # ll.append(6)
    for i in range(1,7):
        ll.append(i)
    ll.travel()
    ht=HashTable()
    ht.insert(0)
    ht.insert(1)
    ht.insert(0)
    print(ht.search(0))
