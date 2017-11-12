
ls=[19,5,4,3,6,8,2,1,9,15]
ls1=[19,9,7,5,13,5,6,7,8,9,10]

def lastIndex(ls,ele):
    index=i=0

    for e in ls:
        if e==ele:
            index=i
        i+=1

    return index


def getIndexOfMax(ls):
    return lastIndex(ls,max(ls))



def lenLongIncSSeq(ls):
    lenls=[]

    for e in ls:
       if len(lenls)!=0:
            prev=ls[getIndexOfMax(lenls)]
       else:
            prev=ls[0]

       print e,"\t",prev,"\t",lenls
       if e>prev:
          lenls.append(max(lenls)+1)
       else:
          lenls.append(1)

    return max(lenls)

print ("Length of longest increasing subsequence is: ",lenLongIncSSeq(ls1),"\n")
