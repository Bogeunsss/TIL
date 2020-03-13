from collections import deque
def bfs():
    while Q:
        x,y,z=Q.popleft()
        for i in range(6):
            tx=x+dx[i]
            ty=y+dy[i]
            tz=z+dz[i]
            if tx<0 or tx>=h or ty<0 or ty>=n or tz<0 or tz>=m:continue
            if tomato[tx][ty][tz]:continue
            tomato[tx][ty][tz]=tomato[x][y][z]+1
            Q.append((tx,ty,tz))
def ripe():
    ans=0
    for i in range(h):
        for j in range(n):
            if 0 in tomato[i][j]: return -1
            ans=max(ans,max(tomato[i][j]))
    return ans-1
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]
m,n,h=map(int,input().split())
tomato=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
Q=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==1:
                Q.append((i,j,k))
bfs()
print(ripe())