class Queue():
    def __init__(self):
        self.__item=[]


    def emqueue(self,item):
        self.__item.append(item)

    def dequeue(self):
        return self.__item.pop(0)

    def is_empty(self):
        return self.__item==[]

    def size(self):
        return len(self.__item)

if __name__ == "__main__":
    s = Queue()
    s.emqueue(1)
    s.emqueue(2)
    s.emqueue(3)
    s.emqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())