def dfs(v):
    global cnt
    visit[v]=1
    for w in G[v]:
        if visit[w]:continue
        cnt += 1
        dfs(w)
V=int(input())
E=int(input())
G=[[] for _ in range(V+1)]
visit=[0]*(V+1)
cnt=0
for _ in range(E):
    u,v=map(int,input().split())
    G[u].append(v)
    G[v].append(u)
dfs(1)
print(cnt)