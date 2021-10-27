s = input()
cnt=0
for i in s:
    if (int(i)==1) :
        cnt+=1
if (cnt%2==0) :
    sum=0
    ans=0
    for i in range(len(s)):
        sum+=int(s[i])
        if (sum==cnt/2) :
            ans=i
    print(s[0:ans+1:],s[ans+1::])
else :
    print("NO") 