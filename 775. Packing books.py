# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if y%z==0:
        print((y//z)*x)
    else:
        print((y//z+1)*x)