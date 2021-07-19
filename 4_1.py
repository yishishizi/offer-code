class SignalNode():
    def __init__(self, item,next=None):
        self.elem = item
        self.next = next

class Soulution1():
    def reversePrint1(self, head):#递归
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head==None or head.next==None:
            return head
        new=self.reversePrint1(head.next)
        head.next.next=head
        head.next=None
        return new

if __name__ == "__main__":
    # node5 = SignalNode(5, None)
    # node4 = SignalNode(4, node5)
    # node3 = SignalNode(3, node4)
    # node2 = SignalNode(2, node3)
    # node1 = SignalNode(1, node2)
    # pr=Soulution()
    # pr.reversePrint1(node1)


    node=SignalNode(1)
    p=node
    for i in range(2,6):
        p.next=SignalNode(i)
        p=p.next
    p=node
    while p:
        print(p.elem,end=' ')
        p=p.next

    print(' ')


    l1 = Soulution1()
    ll1 = l1.reversePrint1(node)
    while ll1:
        print(ll1.elem, end=' ')
        ll1 = ll1.next
        print(' ')