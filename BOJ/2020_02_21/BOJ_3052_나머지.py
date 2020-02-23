arr=[0 for _ in range(42)]
cnt=0
for i in range(10):
    n=int(input())
    if arr[n%42]==0:
        arr[n%42]+=1
for i in range(42):
    if arr[i]==1:
        cnt+=1
print(cnt)