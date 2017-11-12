graphAdjDict={}

def reverseDictionary(dl):
    temp={}
    for p in dl:
        temp[p[1]]=p[0]
    return temp

def constructGraph(edges):

    for e in edges:
        if e[0] not in graphAdjDict:
            graphAdjDict[e[0]]=[]
        if e[1] not in graphAdjDict:
            graphAdjDict[e[1]]=[]

        graphAdjDict[e[0]].append(e[1])
        graphAdjDict[e[1]].append(e[0])




def constructWeightedGraph(edges):

    for e in edges:
        if e[0] not in graphAdjDict:
            graphAdjDict[e[0]]=[]
        if e[1] not in graphAdjDict:
            graphAdjDict[e[1]]=[]

        graphAdjDict[e[0]].append( [e[1],int(e[2])] )
        graphAdjDict[e[1]].append( [e[0],int(e[2])] )


def readGraph():
    #v=int(raw_input("Enter Number of vertices: "))
    f=open("input","r")
    edges=f.read().split()
    edges=map(lambda x:x.split('-'),edges)
    constructWeightedGraph(edges)
    for v in graphAdjDict:
        print v,graphAdjDict[v]
    print "\n"




