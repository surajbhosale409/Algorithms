
ls=[19,9,7,5,13,5,6,7,8,9,10]
ls1=[16,15,6,7,5,8,5,9,5,4,5,6,7]


def getExtensions(i,ls,ext):
    t=[]
    if i==0:
        return [1]
    else:
        for j in range(0,i):
            if ls[i]>ls[j]:
                t.append(ext[j]+1)
            else:
                t.append(1)
        return t


def lenLongIncSSeq(ls):
    ext=[]

    for i in range(0,len(ls)):
            ext.append(0)

    for i in range(0,len(ls)):
        t=getExtensions(i,ls,ext)
        ext[i]=max(t)

    return max(ext)

print "For list: ",ls," Length of longest subsequence is: ",lenLongIncSSeq(ls)
print "For list: ",ls1," Length of longest subsequence is: ",lenLongIncSSeq(ls1)
