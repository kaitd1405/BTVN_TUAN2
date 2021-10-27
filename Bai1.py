a="TRE TRAU"
b=input()
i=1
for _ in b :
    if _==a[i]:
        i+=1
        if i>=7 : break
print("TRE TRAU") if i==7 else print("KHONG TRE TRAU")
