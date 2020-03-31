from collections import deque
def bfs(s,m):
    Q=deque([s])
    visit = [0] * (n + 1)
    visit[s]=1
    while Q:
        v=Q.popleft()
        for tv,tw in G[v]:
            if visit[tv]:continue
            visit[tv]=visit[v]+tw
            Q.append(tv)
    if m==1: return visit.index(max(visit))
    else: return max(visit)

n=int(input())
G=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,d,w=map(int,input().split())
    G[u].append((d,w))
    G[d].append((u,w))
print(bfs(bfs(1,1),2)-1)