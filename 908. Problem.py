# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    if abs((n-m))%2 == 0:
        print("YES")
    else:
        print("NO")