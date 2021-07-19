class Anode:#边表节点
    def __init__(self,edgedata,weight=0):
        self.edgedata=edgedata
        self.weight=weight
        self.next=None
class Vnode:#顶点表节点
    def __init__(self,vertdata):
        self.vertdata=vertdata
        self.firsta=None

class Graph:
    def __init__(self):
        self.vertlist=[]
        self.numvert=0

    def add_vert(self,key):#添加到顶点表中
        vertex=Vnode(key)
        self.vertlist.append(vertex)
        self.numvert+=1

    def add_edge(self,vert1,vert2,weight=0):#添加边
        i=0
        while i<len(self.vertlist):
            if vert1==self.vertlist[i].vertdata:
                n1=self.vertlist[i]
                break
            i+=1

        if i==len(self.vertlist):
            n1=self.add_vert(vert1)
        i=0
        while i<len(self.vertlist):
            if vert2 == self.vertlist[i].vertdata:
                n2 = self.vertlist[i]
                break
            i += 1

        if i == len(self.vertlist):
            n2 = self.add_vert(vert2)

        j=self.vertlist.index(n2)
        p=Anode(j)
        p.next=n1.firsta
        n1.firsta=p


if __name__ == "__main__":
    g=Graph()
    # while True:
    #     s=input('请输入图的顶点值，输入#结束')
    #     if s=='#':
    #         break
    #     else:
    #         g.add_vert(s)
    # while True:
    #     vert1,vert2=input('请输入边的两个顶点，用逗号隔开，输入#结束后').split(',')
    #     if vert1=='#':
    #         break
    #     else:
    #         g.add_edge(vert1,vert2)
    g.add_vert('v0')
    g.add_vert('v1')
    g.add_vert('v2')
    g.add_vert('v3')
    g.add_vert('v4')
    g.add_edge('v0', 'v3')
    g.add_edge('v0', 'v1')
    g.add_edge('v1', 'v4')
    g.add_edge('v1', 'v2')
    g.add_edge('v1', 'v0')
    g.add_edge('v2', 'v4')
    g.add_edge('v2', 'v3')
    g.add_edge('v2', 'v1')
    g.add_edge('v3', 'v2')
    g.add_edge('v3', 'v0')
    g.add_edge('v4', 'v2')
    g.add_edge('v4', 'v1')



    for i in range(g.numvert):
        print(g.vertlist[i].vertdata,end='')


