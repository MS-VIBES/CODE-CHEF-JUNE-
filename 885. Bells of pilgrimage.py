# FOR LOOP
# cook your dish here
t=int(input())
for i in range(t):
    n,x,k,p=map(int,input().split())
    if(n==k):
        p+= (x*10)+((k-x)*5)+20
    else:
        if(x>=k):
            p += k*10
        else:
            p += (x*10)+((k-x)*5)
    print(p)

#WHILE LOOP
t=int(input())
while(t>0):
    t-=1
    a,b,c,d=map(int, input().split())
    if(b>=c):
        d+=c*10
    else:
        d+=b*10
        d+=(min(a,c)-b)*5
    if c==a:
        d+=20
    print(d)

#COMPREHENSION
# cook your dish here
mana=int(input())
for m in range(mana):
  n,x,k,p=map(int,input().split())
  if n==k:print(p+(x*10)+((k-x)*5)+20)
  elif x>=k:print(p+(k*10))
  else: print(p+(x*10)+(k-x)*5)