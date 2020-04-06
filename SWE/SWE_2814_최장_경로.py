def dfs(s,k):
    global ans
    visit[s]=1
    ans=max(ans,k)
    for w in G[s]:
        if visit[w]:continue
        dfs(w,k+1)
    visit[s]=0

for T in range(int(input())):
    n,m=map(int,input().split())
    G=[[] for _ in range(n+1)]
    ans=-1
    for _ in range(m):
        u,v=map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    for i in range(n):
        visit=[0]*(n+1)
        dfs(i,1)
    print('#%d %d'%(T+1,ans))