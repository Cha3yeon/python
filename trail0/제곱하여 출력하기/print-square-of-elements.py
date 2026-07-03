N = int(input())
L = list(map(int,input().split()))
K = [a**2 for  a in L]
for i in K:
    print(i, end =" ")
