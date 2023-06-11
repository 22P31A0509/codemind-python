n=int(input())
l=list(map(int,input().split()))
n=[]
for i in l:
    if i==l.count(i):
        n.append(i)
s=set(n)
print(len(s))