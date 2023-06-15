n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if i==l.count(i):
        c.append(i)
p=set(c)
print(len(p))