def hansu(s):
    c=str(s)
    n=len(c)
    if n<3:
        return 1
    gongcha=int(c[1])-int(c[0])
    for i in range(1,n-1):
        if int(c[i+1])-int(c[i])!=gongcha:
            return 0
    return 1

ins=int(input())
cnt=0
for x in range(1,ins+1):
    if hansu(x):
        cnt+=1
print(cnt)