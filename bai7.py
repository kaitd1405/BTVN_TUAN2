n = int(input())
D=dict()
list=[]
for i in range(n):
    list.append(input().split())
    D[list[i][1]]=0
for i in list:
    D[i[1]]+=1
D1={k:v for k,v in sorted(D.items(),key=lambda item:item[1],reverse=True)}
# print(D1)
# print(list)
for i in D1:
    for j in list :
        if (j[1]==i) :
            print(j[0])
    break

