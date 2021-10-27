D={
    4: "hihi",
    1: "haha",
    9: 10,
    7: [4,3,2,1]
}
D1={k:v for k,v in sorted(D.items(),key=lambda item:item[0])}
print(D1)