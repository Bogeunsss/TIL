from collections import deque
def bfs(s):
    Q=deque([s])
    visit[s]=0
    while Q:
        v=Q.popleft()
        if v==G:return visit[v]
        for i in (U,-D):
            tv=v+i
            if 1<=tv<=F and visit[tv]==-1:
                visit[tv]=visit[v]+1
                Q.append(tv)
    return "use the stairs"
F,S,G,U,D=map(int,input().split())
visit=[-1]*(F+1)
print(bfs(S))