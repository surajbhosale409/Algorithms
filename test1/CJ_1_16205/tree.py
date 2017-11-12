tree={}

def addToTree(pcNodes):
    parent=pcNodes[0]
    children=pcNodes[1]

    if parent in tree:
        tree[parent].append( { children : [] } )
    elif children in tree:
        tree[parent]=[{ children: tree[children]}]
        #del tree[children]
    elif len(tree)==0 or (parent not in tree and children not in tree):
        tree[parent]=[ { children : [] } ]



def immediateChildren(parent):
    l=[]
    for child in tree[parent]:
        l.append(child.keys())
    print "Immediate Children of '",parent,"' are/is ",l



def allChildren(parent,l):
    try:
        if len(tree[parent])==0:
            return l
        else:
            for child in tree[parent]:
                l.append(child.keys()[0])
                l=allChildren(child.keys()[0],l)
            return l

    except KeyError:
        return l


def isAncestor(parent,child):
    children=allChildren(parent,[])
    if child in children:
        return True
    else:
        return False


pcNodes=raw_input().strip().split()
pcNodePairs=map(lambda x:x.split('-'),pcNodes)
map(addToTree,pcNodePairs)
print tree,"\n\n"
immediateChildren('b')
immediateChildren('a')
print "All children of 'a' are ",allChildren('a',[])
print "All children of 'n' are ",allChildren('n',[])

print "'a' is ancestor of 'n'",isAncestor('a','n')
print "'n' is ancestor of 'a'",isAncestor('n','a')
