class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if self.stack_out==[]:#只有当stack_out为空列表的时候执行这句话
            if self.stack_in==[]:  # 都为空
                return -1
            else:  # 把in栈中的东西全部倒入out栈中
                while self.stack_in!=[]:
                    self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()

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