
def min(a,b):
    if a>b:
        return b
    else:
        return a

def coinsCount(n):
    solution=0

    if n==0:
        return 0;

    solution=1+coinsCount(n-1)

    if n>=5:
        solution2=1+coinsCount(n-5)
        solution=min(solution,solution2)

    if n>=7:
        solution3=1+coinsCount(n-7)
        solution=min(solution,solution3)

    return solution

n=input("Enter n: ")
print coinsCount(n)
