from collections import deque

def bfs(x,y):
    Q=deque([x])
    visit=[0]*(n+1)
    visit[x]=1
    while Q:
        v=Q.popleft()
        for w in G[v]:
            if visit[w]: continue
            if w==y: return True
            visit[w]=1
            Q.append(w)
    return False

n,k=map(int,input().split())
G=[[] for _ in range(n+1)]
for _ in range(k):
    u,v=map(int,input().split())
    G[u].append(v)
s=int(input())
events=[list(map(int,input().split())) for _ in range(s)]
for event in events:
    e1=bfs(event[0],event[1])
    e2=bfs(event[1],event[0])
    if e1 and not e2: print(-1)
    elif not e1 and e2: print(1)
    elif not e1 and not e2: print(0)