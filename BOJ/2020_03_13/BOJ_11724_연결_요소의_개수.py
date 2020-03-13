from collections import deque
def bfs(s):
    Q=deque([s])
    if visit[s]:return 0
    visit[s]=1
    while Q:
        v=Q.popleft()
        for w in G[v]:
            if visit[w]:continue
            visit[w]=1
            Q.append(w)
    return 1

n,m=map(int,input().split())
G=[[] for _ in range(n+1)]
visit=[0]*(n+1)
cnt=0
for _ in range(m):
    u,v=map(int,input().split())
    G[u].append(v)
    G[v].append(u)
for i in range(1,n+1):
    cnt+=bfs(i)
print(cnt)