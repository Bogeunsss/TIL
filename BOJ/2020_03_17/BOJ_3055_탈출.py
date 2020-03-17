from collections import deque
def bfs():
    Q.append((sx,sy,1))
    visit[sx][sy]=1
    while Q:
        x,y,z=Q.popleft()
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if tx<0 or tx>=r or ty<0 or ty>=c:continue
            if Map[tx][ty]=='X' or visit[tx][ty]:continue
            if Map[tx][ty]=='D':
                if z==0:continue
                print(visit[x][y])
                return
            visit[tx][ty]=visit[x][y]+1
            Q.append((tx,ty,z))
    print('KAKTUS')

dx=[-1,1,0,0]
dy=[0,0,-1,1]
r,c=map(int,input().split())
Map=[input() for _ in range(r)]
visit=[[0]*c for _ in range(r)]
Q=deque()
sx=sy=0
for i in range(r):
    for j in range(c):
        if Map[i][j]=='*':
            Q.append((i,j,0))
            visit[i][j]=1
        elif Map[i][j]=='S':
            sx,sy=i,j
bfs()