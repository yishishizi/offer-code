class Graph:
    def __init__(self,mat,verxs=0):#mat边的信息，verxs顶点表
        vnum=len(mat)
        for x in mat:
            if len(x)!=vnum:
                raise ValueError("Argument for Graph")

        self.mat=[mat[i][:] for i in range(vnum)]
        self.verxs=verxs
        self.vnum=vnum#顶点个数

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

def BSFmat(graph):
    vistied=[0]*len(graph.verxs)
    q=Squeque(len(graph.verxs))
    print(graph.verxs[0],end='')
    vistied[0]=1
    q.inqueque(0)
    while q.is_empty()!=1:
        i=q.dequeque()
        for j in range(len(graph.verxs)):
            if graph.mat[i][j]==1 and vistied[j]==0:
                print(graph.verxs[j],end='')
                vistied[j]=1
                q.inqueque(j)

if __name__ == "__main__":
    nodes = ['v0', 'v1', 'v2', 'v3', 'v4']
    matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 1, 0, 0]]
    mygraph = Graph(matrix, nodes)
    print(mygraph.verxs)
    print(mygraph.mat)
    BSFmat(mygraph)