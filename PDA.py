a=int(input())
c=0
for i in range(1,(a//2)+1):
    if a%i==0:
        c+=i
if a==c:
    print("PERFECT")
elif c<a:
    print("DEFICIENT")
else:
    print("ABUNDANT")