l = input().split(",")
a = [int(i[1:-1]) for i in  l if int(i[1:-1]) %2==0]
b = [int(i[1:-1]) for i in  l if int(i[1:-1]) %2==1]
print(tuple(a+b))