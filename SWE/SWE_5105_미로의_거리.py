from collections import deque
def bfs(_x,_y):
    Q=deque([(_x,_y)])
    dist[_x][_y]=0
    while Q:
        x,y=Q.popleft()
        if maze[x][y]=='3': return dist[x][y]-1
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if tx<0 or tx>=n or ty<0 or ty>=n: continue
            if maze[tx][ty]=='1' or dist[tx][ty]!=-1:continue
            dist[tx][ty]=dist[x][y]+1
            Q.append((tx,ty))
    return 0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for T in range(int(input())):
    n=int(input())
    maze=[input() for _ in range(n)]
    dist=[[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j]=='2':
                print('#%d %d'%(T+1,bfs(i,j)))