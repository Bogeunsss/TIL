from collections import deque
def bfs(s):
    Q=deque([s])
    visit[s]=0
    while Q:
        v=Q.popleft()
        if v==des: return visit[v]
        for w in G[v]:
            if visit[w]!=-1:continue
            visit[w]=visit[v]+1
            Q.append(w)
    return 0
for T in range(int(input())):
    V,E=map(int,input().split())
    G=[[] for _ in range(V+1)]
    visit=[-1]*(V+1)
    for _ in range(E):
        u,v=map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    src,des=map(int,input().split())
    print('#%d %d'%(T+1,bfs(src)))