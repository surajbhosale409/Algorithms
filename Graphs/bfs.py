import graph

def notIn(v,q):
    if v in q:
        return False
    else:
        return True

def bfs(startVertex,visited,bfsQueue):

    if visited == graph.graphAdjDict.keys():
        return [visited,bfsQueue]

    if notIn(startVertex,visited):
        visited.append(startVertex)
        for v in graph.graphAdjDict[startVertex]:
            if notIn(v,bfsQueue) and notIn(v,visited):
                bfsQueue.append(v)
        if len(bfsQueue)!=0:
            visited,bfsQueue=bfs(bfsQueue.pop(0),visited,bfsQueue)
    return [visited,bfsQueue]


edges=map(lambda x:x.split('-'),raw_input("Enter Edges: ").split())
print edges
graph.constructGraph(edges)
startVertex=raw_input("Enter start vertex for Breadth First Search: ")
bfsOutput=bfs(startVertex,[],[])
print bfsOutput[0]
