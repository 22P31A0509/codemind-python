n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if i!=1 and i!=0:
        print(False)
        break
else:
    print(True)