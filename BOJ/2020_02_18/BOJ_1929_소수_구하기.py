M,N=map(int,input().split())
arr=[False]*1000001
arr[1]=True

for i in range(2,N+1):
    if arr[i]:continue
    if i*i>N:break
    for j in range(i*i,N+1,i):
        if not arr[j]: arr[j]=True
for i in range(M,N+1):
    if not arr[i]:print(i)