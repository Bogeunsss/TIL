def dfs(cur, k):
    global ans
    if k==int(n):
        ans = max(ans, int(''.join(num)))
    else:
        for i in range(cur, len(num)):
            for j in range(i+1, len(num)):
                if num[i] <= num[j]:
                    num[i], num[j] = num[j], num[i]
                    dfs(i, k+1)
                    num[j], num[i] = num[i], num[j]

for T in range(int(input())):
    num, n = input().split()
    num = list(num)
    ans = 0
    dfs(0,0)
    print('#%d %d' %(T+1, ans))