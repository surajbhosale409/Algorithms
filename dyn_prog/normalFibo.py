import time

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))

n=input("Enter n: ")
start=time.time()
print fibo(n-1)
end=time.time()
print end-start
