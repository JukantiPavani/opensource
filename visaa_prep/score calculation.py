N = int(input())
for i in range(N):
    m,n = list(map(int,input().split()))
    if(n == 0):
        print(0)
    else:
        points = m//10
        print(points*n)
    
