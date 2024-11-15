V,C = list(map(str,input().split()))
if(V == 'P' and C == 'R'):
    print("Vignesh")
elif(V=='S' and C == 'R'):
    print("Charan")
elif(V=='S' and C == 'P'):
    print("Vignesh")
elif(V=='R' and C == 'S'):
    print("Vignesh")
elif(V=='P' and C == 'S'):
    print("Charan")
elif(V=='R' and C == 'P'):
    print("Charan")
else:
    print("NULL")
