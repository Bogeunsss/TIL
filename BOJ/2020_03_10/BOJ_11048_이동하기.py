n,m=map(int,input().split())
dp=[0]*1001
for i in range(1,n+1):
    temp=list(map(int,input().split()))
    for j in range(1,m+1):
        dp[j]=max(dp[j-1],dp[j])+temp[j-1]
print(dp[m])