import numpy as np
class Graph:
    def __init__(self,mat,verxs=0):#mat边的信息，verxs顶点表
        vnum=len(mat)
        for x in mat:
            if len(x)!=vnum:
                raise ValueError("Argument for Graph")

        self.mat=[mat[i][:] for i in range(vnum)]
        self.verxs=verxs
        self.vnum=vnum#顶点个数

    def get_edge(self,vi,vj):
        if vi not in self.verxs or vj not in self.verxs:
            print('无效顶点')
            return
        i = self.verxs.index(vi)
        j = self.verxs.index(vj)
        return self.mat[i][j]

    def degree(self,vi):
        i=self.verxs.index(vi)
        in_degree=np.sum(self.mat,axis=1)
        out_degree=np.sum(self.mat,axis=0)
        return in_degree[i],out_degree[i]





if __name__ == "__main__":
    nodes = ['v0', 'v1', 'v2', 'v3', 'v4']
    matrix = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 0], [0, 1, 1, 0, 0]]
    mygraph = Graph(matrix, nodes)
    print(mygraph.verxs)
    print(mygraph.mat)
    print(mygraph.get_edge('v1', 'v2'))
    print(mygraph.degree('v0'))