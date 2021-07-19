class Deque():
    def __init__(self):
        self.__item=[]

    def add_front(self,item):
        self.__item.insert(0,item)

    def add_rear(self,item):
        self.__item.append(item)

    def pop_front(self):
        return self.__item.pop(0)

    def pop_rear(self):
        return self.__item.pop()

    def is_empty(self):
        return self.__item==[]

    def size(self):
        return len(self.__item)