n=int(input())
l=list(map(int,input().split()))
s=int(input())
for i in l:
    if i==s:
        print(True)
        break
else:
    print(False)