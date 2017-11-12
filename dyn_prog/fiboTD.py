import time

def fiboTD(n,A):
    if A[n]!=-1:
        return A[n]
    else:
        A[n]=fiboTD(n-1,A)+fiboTD(n-2,A)
        return A[n]

def fibo(n):
    A=range(0,n+1)
    A[0]=0
    A[1]=1
    for i in range(2,n+1):
        A[i]=-1
    return (fiboTD(n,A))


n=input("Enter n: ")
start=time.time()
print "Fibonacci Series ",n," number element is ",fibo(n-1)
end=time.time()
print end-start
