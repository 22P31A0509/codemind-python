n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in l:
    if i<a or i>b:
        c.append(i)
if not c:
    print(-1)
else:
    for i in c:
         print(i,end=" ")