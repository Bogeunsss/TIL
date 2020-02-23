A,B=input().split()
m,n=len(A),len(B)
Map=[['.']*m for _ in range(n)]
same=''
flag=False
idx=jdx=0
for i in range(m):
    for j in range(n):
        if A[i]==B[j]:
            flag=True
            same=A[i]
            idx,jdx=i,j
            break
    if flag:break
for i in range(m):
    Map[jdx][i]=A[i]
for i in range(n):
    Map[i][idx]=B[i]
for i in range(n):
    for j in range(m):
        print(Map[i][j],end='')
    print()