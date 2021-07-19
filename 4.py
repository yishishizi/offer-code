# 在节点ListNode定义中，定义为节点为结构变量。
# 节点存储了两个变量：value 和 next。value 是这个节点的值，next 是指向下一节点的指针，当 next 为空指针时，这个节点是链表的最后一个节点。
# 注意注意val只代表当前指针的值，比如p->val表示p指针的指向的值；而p->next表示链表下一个节点，也是一个指针。
# 构造函数包含两个参数 _value 和 _next ，分别用来给节点赋值和指定下一节点

class SignalNode():
    def __init__(self, item,next=None):
        self.elem = item
        self.next = next

class Soulution():
    def reversePrint(self, head):#迭代
        """
        :type head: ListNode
        :rtype: List[int]
        """
        pre,cur=None,head
        while cur!=None:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        while pre:
            print(pre.elem, end=' ')
            pre = pre.next
        print(' ')
        return pre



if __name__ == "__main__":
    # node5 = SignalNode(5, None)
    # node4 = SignalNode(4, node5)
    # node3 = SignalNode(3, node4)
    # node2 = SignalNode(2, node3)
    # node1 = SignalNode(1, node2)
    # pr=Soulution()
    # pr.reversePrint1(node1)


    node=SignalNode(1)
    p=node#这里的p相当于指针，指向当前节点cur
    for i in range(2,6):
        p.next=SignalNode(i)
        p=p.next
    p=node
    while p:
        print(p.elem,end=' ')
        p=p.next

    print(' ')

    l=Soulution()
    ll=l.reversePrint(node)
    while ll:
        print(ll.elem,end=' ')
        ll=ll.next
        print(' ')




# class Solution(object):
#     def reversePrint(self, head):
#         """
#         :type head: ListNode
#         :rtype: List[int]
#         """
#         if head.next == None:  # 递归停止的基线条件
#             return head
#         new_head = self.reversePrint(head.next)
#         head.next.next = head  # 当前层函数的head节点的后续节点指向当前head节点
#         head.next = None  # 当前head节点指向None
#         return new_head
# head = None
# for x in [5, 1, 7, 96]:
#     head = ListNode(x, next=head)
# print(head)
# l=Solution()
# ll=l.reversePrint(head)


# class Solution1(object):
#     def reversePrint1(self, head):
#         """
#         :type head: ListNode
#         :rtype: List[int]
#         """
#         pre,p=None,head
#         while p:
#             tmp=p.next
#             p.next=pre
#             q=p#把当前节点作为pre
#             p=tmp#把当前节点的下个节点作为当前节点
#         return pre
#
#     def printall(self,head):
#         while head:
#             print("%d, " % (head.x), end='')
#             l = head.next
#         print('')
# head = None
# for x in [5, 1, 7, 96]:
#     head = ListNode(x, next=head)
# l1=Solution1()
# #ll2=l1.printall(head)
# ll1=l1.reversePrint1(head)
#
# print(head==ll1)
# print(ll==ll1)
