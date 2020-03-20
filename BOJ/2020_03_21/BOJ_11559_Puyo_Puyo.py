import sys;input=sys.stdin.readline
from collections import deque
def drop():
    for j in range(m):
        for i in range(n-1,-1,-1):
            if field[i][j]=='.':continue
            for k in range(n-1,i-1,-1):
                if field[k][j]=='.':
                    field[k][j]=field[i][j]
                    field[i][j]='.'
def bfs(x,y,z,visit):
    Q=deque()
    block=[(x,y)]
    Q.append((x,y))
    visit[x][y]=1
    while Q:
        u,v=Q.popleft()
        for i in range(4):
            tx=u+dx[i]
            ty=v+dy[i]
            if tx<0 or tx>=n or ty<0 or ty>=m:continue
            if visit[tx][ty]==0 and field[tx][ty]==z:
                visit[tx][ty]=1
                block.append((tx,ty))
                Q.append((tx,ty))
    if len(block)>=4:
        for x,y in  block:
            field[x][y]='.'
        return True
    else:
        return False
def crash():
    isCrash=False
    visit=[[0]*m for _ in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if visit[i][j] or field[i][j]=='.':continue
            if bfs(i,j,field[i][j],visit):isCrash=True
    return isCrash

dx=[1,-1,0,0]
dy=[0,0,1,-1]
n,m=12,6
field=[list(input().strip()) for _ in range(n)]
ans=0
while crash():
    drop()
    ans+=1
print(ans)