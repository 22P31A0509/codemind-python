a=int(input())
if a%5!=0:
    print(-1)
else:
    print((a//10)+((a%10)//5))
