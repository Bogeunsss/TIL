import sys; input=sys.stdin.readline
from collections import deque
def bfs(s):
    global hack
    Q=deque([s])
    visit[s]=1
    cnt=0
    while Q:
        v=Q.popleft()
        for w in G[v]:
            if visit[w]:continue
            Q.append(w)
            visit[w]=1
            cnt+=1
    if hack<cnt:
        hack=cnt
        ans.clear()
        ans.append(s)
    elif hack==cnt:
        ans.append(s)

n,m=map(int,input().split())
G=[[] for _ in range(n+1)]
ans=[]
hack=0
for _ in range(m):
    u,v=map(int,input().split())
    G[v].append(u)
for i in range(1,n+1):
    visit=[0]*(n+1)
    bfs(i)
ans.sort()
for i in ans:
    print(i,end=' ')
print()