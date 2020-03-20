import sys;input=sys.stdin.readline
from collections import deque

def bfs1(x,y,m):
    Q=deque()
    Q.append((x,y))
    visit[x][y]=1
    land[x][y]=m
    while Q:
        u,v=Q.popleft()
        for i in range(4):
            tx=u+dx[i]
            ty=v+dy[i]
            if tx<0 or tx>=n or ty<0 or ty>=n:continue
            if visit[tx][ty]==0 and land[tx][ty]:
                visit[tx][ty]=1
                land[tx][ty]=m
                Q.append((tx,ty))
def bfs2(s):
    global Min
    distance=[[-1]*n for _ in range(n)]
    Q=deque()
    for i in range(n):
        for j in range(n):
            if land[i][j]==s:
                Q.append((i,j))
                distance[i][j]=0
    while Q:
        x,y=Q.popleft()
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if tx<0 or tx>=n or ty<0 or ty>=n: continue
            if land[tx][ty] and land[tx][ty]!=s:
                Min=min(Min,distance[x][y])
                return
            if land[tx][ty]==0 and distance[tx][ty]==-1:
                distance[tx][ty]=distance[x][y]+1
                Q.append((tx,ty))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
n=int(input())
land=[list(map(int,input().split())) for _ in range(n)]
visit=[[0]*n for _ in range(n)]
Min=1e9
mark=1

for i in range(n):
    for j in range(n):
        if visit[i][j]==0 and land[i][j]:
            bfs1(i,j,mark)
            mark+=1
for i in range(1,mark+1):
    bfs2(i)
print(Min)