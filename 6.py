class CQueue:

    def __init__(self):
        self.item1=[]
        self.item2=[]


    def appendTail(self, value: int) -> None:
        while self.item2 != []:
            a = self.item2.pop()
            self.item1.append(a)
        self.item1.append(value)


    def deleteHead(self) -> int:
        while self.item1:
            b = self.item1.pop()
            self.item2.append(b)
        if not self.item2:
            return -1
        else:
            return self.item2.pop()

obj = CQueue()
obj.appendTail(5)
obj.appendTail(2)
obj.appendTail(3)
obj.appendTail(1)
print(obj.deleteHead())
print(obj.deleteHead())
obj.appendTail(4)
obj.appendTail(14)
obj.appendTail(6)
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.deleteHead())

