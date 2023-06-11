n=int(input())
l=list(map(int,input().split()))
k=int(input())
p=[]
for i in l:
    if l.count(i)==k:
        p.append(i)
if not p:
    print(-1)
else:
    s=set(p)
    for i in s:
         print(i,end=" ")