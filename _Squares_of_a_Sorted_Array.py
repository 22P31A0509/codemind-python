n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(i*i)
a=sorted(c)
for j in a:
    print(j,end=" ")