N = int(input())
result = 1
for i in range(1, N+1):
    for j in range(i):
        print(result,end=" ")
        result += 1
    print( )
