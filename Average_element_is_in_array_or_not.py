n=int(input())
l=list(map(int,input().split()))
s=sum(l)
a=s//n
for i in l:
    if i==a:
        print(True)
        break
else:
    print(False)