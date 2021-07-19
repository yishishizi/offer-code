class Graph:
    def __init__(self,mat,verxs=0):#mat边的信息，verxs顶点表
        vnum=len(mat)
        for x in mat:
            if len(x)!=vnum:
                raise ValueError("Argument for Graph")

        self.mat=[mat[i][:] for i in range(vnum)]
        self.verxs=verxs
        self.vnum=vnum#顶点个数

from stack_list import Stack
def DFSmat(graph):#图的深度遍历
    visited=[0]*len(graph.verxs)
    s=Stack()
    s.push(0)
    print(graph.verxs[0],end='')
    visited[0]=1
    i=0
    while s.is_empty()is False:
        i = s.pop()
        for j in range(len(graph.verxs)):
            if graph.mat[i][j]==1 and visited[j]==0:
                print(graph.verxs[j],end='')
                visited[j]=1
                s.push(j)
                i=j
        # if s.is_empty()!=True:
        #     i=s.pop()



if __name__ == "__main__":
    nodes = ['v0', 'v1', 'v2', 'v3', 'v4']
    matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 1, 0, 0]]
    mygraph = Graph(matrix, nodes)
    print(mygraph.verxs)
    print(mygraph.mat)
    DFSmat(mygraph)


