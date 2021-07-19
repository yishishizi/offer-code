class Squeque():
    def __init__(self,maxsize):
        self.queue=maxsize*[None]
        self.front=0
        self.rear=0
        self.maxsize=maxsize

    def is_empty(self):
        if self.front==self.rear:
            return 1
        else:
            return 0

    def inqueque(self,data):
        if (self.rear+1)%self.maxsize==self.front:
            return None
        else:
            self.queue[self.rear]=data
            self.rear=(self.rear+1)%self.maxsize

    def dequeque(self):
        if self.is_empty()==1:
            return None
        else:
            data=self.queue[self.front]
            self.front=(self.front+1)%self.maxsize
            return data