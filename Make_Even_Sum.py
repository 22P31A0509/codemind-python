n=int(input())
p=list(map(int,input().split()))
if n%2==0:
    c=0
    d=0
    for i in p:
        if i%2==0:
            c+=1
        else:
            d+=1
    if c%2==0 and d%2==0:
        print("1")
    else:
        print("0")
        
else:
    print("0")