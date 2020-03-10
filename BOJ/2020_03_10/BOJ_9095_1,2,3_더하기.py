dp=[1,2,4]
dp.extend(sum(dp[-3:]) for _ in range(4,11))
for T in range(int(input())):
    n=int(input())
    print(dp[n-1])