import time

def fiboBU(i,n,A):
    if i<=n:
       A[i]=A[i-1]+A[i-2]
       return fiboBU(i+1,n,A)
    else:
        return A[n]

def fibo(n):
    A=range(0,n+1)
    A[0]=0
    A[1]=1
    for i in range(2,n+1):
        A[i]=-1
    return (fiboBU(2,n,A))


n=input("Enter n: ")
start=time.time()
print "Fibonacci Series ",n," number element is ",fibo(n-1)
end=time.time()
print end-start
