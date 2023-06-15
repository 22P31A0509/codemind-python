n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(0,n,1):
    if i%2!=0:
        c.append(l[i])
for i in c:
    if i%2==0:
        print(False)
        break
else:
    print(True)
       