from collections import deque

def bfs(v):
    Q=deque([s])
    visit=[0]*(n+1)
    visit[s]=1
    while Q:
        tx = Q.popleft()
        for ty,tz in maps[tx]:
            if not visit[ty] and tz>=v:
                Q.append(ty)
                visit[ty]=1
    return visit[e]

n,m=map(int,input().split())
maps=[[] for _ in range(n+1)]
Min,Max,result=1e9,-1e9,0
for _ in range(m):
    x,y,z=map(int,input().split())
    maps[x].append((y,z))
    maps[y].append((x,z))
    Max=max(Max,z)
    Min=min(Min,z)
s,e=map(int,input().split())
while Min<=Max:
    mid=(Min+Max)//2
    if bfs(mid):
        result=mid
        Min=mid+1
    else:
        Max=mid-1
print(result)