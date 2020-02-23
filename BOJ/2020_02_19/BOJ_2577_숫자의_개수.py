gop=1
arr=[0 for _ in range(10)]
for i in range(3):
    gop*=int(input())
print(gop)
while gop>10:
    arr[gop%10]+=1
    gop//=10
    
for i in range(len(arr)):
    print(arr[i])