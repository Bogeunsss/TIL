from collections import deque
def bfs(_x,_y):
    Q=deque([(_x,_y)])
    while Q:
        x,y=Q.popleft()
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if tx<0 or tx>=n or ty<0 or ty>=n: continue
            if D[tx][ty]>D[x][y]+Map[tx][ty]:
                D[tx][ty]=D[x][y]+Map[tx][ty]
                Q.append((tx,ty))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for T in range(int(input())):
    n=int(input())
    Map=[list(map(int,list(input()))) for _ in range(n)]
    D=[[1e9]*n for _ in range(n)]
    D[0][0]=0
    bfs(0,0)
    print('#%d %d'%(T+1,D[n-1][n-1]))