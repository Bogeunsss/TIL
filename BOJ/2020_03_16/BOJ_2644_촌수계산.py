from collections import deque
def bfs(s):
    Q=deque()
    Q.append(s)
    while Q:
        v=Q.popleft()
        if v==h2: return distance[v]
        for w in G[v]:
            if distance[w]:continue
            distance[w]=distance[v]+1
            Q.append(w)
    return -1
n=int(input())
h1,h2=map(int,input().split())
m=int(input())
G=[[] for _ in range(n+1)]
distance=[0]*(n+1)
for _ in range(m):
    x,y=map(int,input().split())
    G[x].append(y)
    G[y].append(x)
print(bfs(h1))