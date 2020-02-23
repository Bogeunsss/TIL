M=int(input())
N=int(input())

arr=[False]*10001
arr[0]=True
arr[1]=True

Sum,Min=0,0xffffffffffff

for i in range(2,N+1):
    if arr[i]:continue
    if i*i>N:break
    for j in range(i*i,N+1,i):
        if not arr[j]:arr[j]=True
for i in range(M,N+1):
    if not arr[i]:
        Sum+=i
        if Min>i:Min=i
if Sum==0:print(-1)
else:
    print(Sum)
    print(Min)