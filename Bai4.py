alist=list(map(int,input().split()))
k=int(input())
cnt=0
for i in range(len(alist)) :
    for j in range(i+1,len(alist)) :
        if alist[i]+alist[j]==k:
            cnt+=1
print(cnt)