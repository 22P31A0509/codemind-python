n=int(input())
c=0
d=0
for i in range(1,n+1,1):
      c+=i*i
      d+=i
p=d*d
print(abs(c-p))