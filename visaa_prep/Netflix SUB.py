a,b,c,y = list(map(int,input().split()))
if (a+b >= y):
    print("YES")
elif (b+c >= y):
    print("YES")
elif (c+a >= y):
    print("YES")
else:
    print("NO")
