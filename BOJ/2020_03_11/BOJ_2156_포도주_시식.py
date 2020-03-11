n=int(input())
wine=[int(input()) for _ in range(n)]
dp=[0]+[wine[0]]
if n>1:dp.append(wine[0]+wine[1])
for i in range(3,n+1):
    c1=wine[i-1]+dp[i-2]
    c2=wine[i-1]+wine[i-2]+dp[i-3]
    c3=dp[i-1]
    Max=max(c1,c2,c3)
    dp.append(Max)
print(dp[n])