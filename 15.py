from linked_list import SignalList
class SignalNode(object):
    def __init__(self,elem):
        self.elem=elem
        self.next=None
class Solution:
    def deleteNode(self, head, val):
        pre, cur = None, head
        while cur != None:
            if cur.elem == val:
                if cur == head:
                    cur = cur.next
                else:
                    pre.next = cur.next
                    cur = cur.next
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    ll = SignalList()
    ll.add(4)
    ll.append(5)
    ll.append(1)
    ll.append(9)
    ll.travel()
    S=Solution()
    S.deleteNode(ll,5)
    ll.travel()

