from stack_list import Stack

class Graph:
    def __init__(self,mat,verxs=0):
        vnum=len(mat)
        for x in mat:
            if len(x)!=vnum:
                raise ValueError("Argument for Graph")

        self.__mat=[mat[i][:] for i in range(vnum)]
        self.__unconn=verxs
        self.__vnum=vnum

    def add_edgs(self,vi,vj,val=1):
         self.__mat[vi][vj]=val

    def get_edgs(self,vi,vj):
        return self.__mat[vi][vj]

    def Dijkstra(self):
        dist=[0,10,float('inf'),30,100]
        visited=[0]*len(self.__unconn)
        pre=[None]*len(self.__unconn)
        for i in range(len(self.__unconn)):
            if self.__mat[0][i]==float('int'):
                pre[i]=-1
            else:
                pre[i]=0
        for i in range(len(self.__unconn)-1):
            mindist=float('int')
            for j in range(len(self.__unconn)):
                if dist[j]<mindist and visited[j]!=1:
                    mindist=dist[j]
                    k=j
            visited[k]=1

            for j in range(len(self.__unconn)):
                if visited[j]!=1 and (mindist+self.__mat[k][j])<dist[j]:
                    dist[j]=dist[k]+self.__mat[k][j]
                    pre[j]=k
        return dist,pre

    def Floyed(self):
        path=[[-1 for i in range(len(self.__unconn))] for j in range(len(self.__unconn))]
        A=[self.__mat[j][:] for i in range(len(self.__unconn))]
        for v in range(len(A)):
            for i in range(len(A)):
                for j in range(len(A)):
                    if A[i][j]>(A[i][v]+A[v][j]):
                        A[i][j]=A[i][v]+A[v][j]
                        path[i][j]=v
        return A,path

    def printpath(self,i,j,path,graph):
        if path[i][j]==-1:
            print(self.__unconn[i],self.__unconn[j])
        else:
            mid=path[i][j]
            print(i,mid,path,graph)
            print(mid,j,path,graph)


    # def TopologicalSort(self):
    #     s=Stack()
    #     for i in range(self.__vnum):
    #         if



