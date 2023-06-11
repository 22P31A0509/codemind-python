n=int(input())
l=list(map(int,input().split()))
n=[]
for i in l:
    if i==l.count(i):
        n.append(i)
if not  n:
    print(-1)
else:
    a=min(n)
    b=max(n)
    print(a,b)