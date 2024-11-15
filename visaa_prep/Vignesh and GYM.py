a,b,c = list(map(int,input().split()))
if(a+b <= c):
    print(2)
elif(a <= c):
    print(1)
else:
    print(0)
