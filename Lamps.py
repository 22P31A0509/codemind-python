n,k,x,y=map(int,input().split())
c=n-k
if x<y:
    print(n*x)
else:
    print((k*x)+(c*y))
