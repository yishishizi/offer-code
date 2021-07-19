class Stack():
    def __init__(self):
        self.__item=[]

    def push(self,item):
        self.__item.append(item)#把列表的尾部叫做栈顶
        #self.__item.index(0,item)#把列表的头部叫做栈顶


    def pop(self):
        return self.__item.pop()#删除list末尾的元素，即栈顶的元素，时间复杂度为O(1)
        #self.__item.pop(0)#删除list头部的元素，时间复杂度为O(n)

    def peek(self):
        if self.__item:
            return self.__item[-1]
        else:
            return None

    def is_empty(self):
        return self.__item==[]

    def size(self):
        return len(self.__item)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
