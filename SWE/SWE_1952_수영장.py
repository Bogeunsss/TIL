def dfs(k,n):
    global Min
    if k>=13:
        Min=min(Min,n)
        return
    dfs(k+1,n+plans[k]*prices[1])
    dfs(k+1,n+prices[2])
    dfs(k+3,n+prices[3])
    dfs(k+12,n+prices[4])

for T in range(int(input())):
    prices=[0]+list(map(int,input().split()))
    plans=[0]+list(map(int,input().split()))
    Min=prices[4]
    dfs(1,0)
    print('#%d %d'%(T+1,Min))