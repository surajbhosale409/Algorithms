import graph

markedVertices=[]
finalVD={}
vertexWithParent={}



def findMinDistancesFromSourceToAllVertices(source,verticesDistances):

    if len(verticesDistances)==0:
        return

    for v in graph.graphAdjDict[source]:
        if v[0] not in markedVertices:
            new=finalVD[source][0]+v[1]
            if new<verticesDistances[v[0]]:
                verticesDistances[v[0]]=new
                vertexWithParent[v[0]]=source

    if len(verticesDistances)!=0:
        m=min(verticesDistances.values())
        reversedVerticesDistances=graph.reverseDictionary(verticesDistances.items())
        v=reversedVerticesDistances[m]
        finalVD[v]=[m,vertexWithParent[v]]
        markedVertices.append(v)
        verticesDistances.pop(v)
        findMinDistancesFromSourceToAllVertices(v,verticesDistances)



def getOptimumPath(s,d,path):
    if d==s:
        path.append(d)
        return path
    path.append(d)
    return getOptimumPath(s,finalVD[d][1],path)


def dijkstrasShortestPathAlgo():
    source,destination=raw_input("\nEnter source and destination (source-destination): ").strip().split('-')

    verticesDistances={}
    for v in graph.graphAdjDict.keys():
        verticesDistances[v]=99999999

    verticesDistances[source]=0
    markedVertices.append(source)
    finalVD[source]=[0,None]
    verticesDistances.pop(source)

    findMinDistancesFromSourceToAllVertices(source,verticesDistances)   #Calculating minimum distances for all vertices from
                                                                        #Given source using dijkstras algorithm
    path=getOptimumPath(source,destination,[])
    path.reverse()
    print "Optimum path for",source,"to",destination,"is:",path,"with distance:",finalVD[destination][0]


graph.readGraph()
dijkstrasShortestPathAlgo()
