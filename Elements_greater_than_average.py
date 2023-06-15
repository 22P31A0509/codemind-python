n=int(input())
l=list(map(int,input().split()))
c=[]
s=sum(l)
a=s//n
for i in l:
    if i>=a:
        c.append(i)
print(len(c))