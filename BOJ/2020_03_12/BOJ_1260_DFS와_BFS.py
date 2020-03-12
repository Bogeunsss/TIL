from collections import deque
def dfs(v):
    visit[v]=1;print(v,end=' ')
    for w in G[v]:
        if visit[w]:continue
        dfs(w)
def bfs(v):
    visit=[0]*(n+1)
    Q=deque()
    Q.append(v)
    visit[v]=1;print(v,end=' ')
    while Q:
        s=Q.popleft()
        for w in G[s]:
            if visit[w]:continue
            visit[w]=1;print(w,end=' ')
            Q.append(w)

n,m,v=map(int,input().split())
G=[[] for _ in range(n+1)]
visit=[0]*(n+1)
for _ in range(m):
    x,y=map(int,input().split())
    G[x].append(y)
    G[y].append(x)
for i in range(len(G)):
    G[i]=sorted(G[i])
dfs(v)
print()
bfs(v)