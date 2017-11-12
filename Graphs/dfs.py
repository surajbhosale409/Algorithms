import graph

def notIn(v,q):
    if v in q:
        return False
    else:
        return True

def dfs(startVertex,visited,dfsStack):

    if visited == graph.graphAdjDict.keys():
        return [visited,dfsStack]

    if notIn(startVertex,visited):
        visited.append(startVertex)
        for v in graph.graphAdjDict[startVertex]:
            if notIn(v,dfsStack) and notIn(v,visited):
                dfsStack.append(v)
        if len(dfsStack)!=0:
            visited,dfsStack=dfs(dfsStack.pop(len(dfsStack)-1),visited,dfsStack)
    return [visited,dfsStack]


edges=map(lambda x:x.split('-'),raw_input("Enter Edges: ").split())
print edges
graph.constructGraph(edges)
startVertex=raw_input("Enter start vertex for Breadth First Search: ")
dfsOutput=dfs(startVertex,[],[])
print dfsOutput[0]
