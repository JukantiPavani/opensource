a = int(input())
b = int(input())
result = str(a)*b
for i in result:
    if i == '1':
        print("true")
        break
    else:
        print("false")
        break
