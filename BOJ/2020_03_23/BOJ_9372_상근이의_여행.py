from collections import deque
def bfs(s):
    global Min
    Q=deque([s])
    visit=[0]*(V+1)
    visit[s]=1
    cnt=0
    while Q:
        v=Q.popleft()
        for w in G[v]:
            if visit[w]:continue
            cnt+=1
            visit[w]=1
            Q.append(w)
    return min(Min,cnt)

for T in range(int(input())):
    V,E=map(int,input().split())
    G=[[] for _ in range(V+1)]
    Min=1e9
    for _ in range(E):
        u,v=map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    for i in range(1,V+1):
        Min=bfs(i)
    print(Min)