from collections import deque

def bfs(x,y,c,visit):
    visit[x][y]=1
    Q=deque()
    Q.append((x,y))
    while Q:
        v,w=Q.popleft()
        for i in range(4):
            tx=v+dx[i]
            ty=w+dy[i]
            if tx<0 or tx==N or ty<0 or ty==N:continue
            if visit[tx][ty] or grid[tx][ty]!=c:continue
            visit[tx][ty]=1
            Q.append((tx,ty))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
N=int(input())
grid=[list(input()) for _ in range(N)]
visitRGB=[[0]*N for _ in range(N)]
visitRRB=[[0]*N for _ in range(N)]
cnt=0
for i in range(N):
    for j in range(N):
        color='R'
        if visitRGB[i][j]==0:
            if grid[i][j]=='G':
                color='G'
            elif grid[i][j]=='B':
                color='B'
            bfs(i,j,color,visitRGB)
            cnt+=1
print(cnt,end=' ')
cnt=0
for i in range(N):
    for j in range(N):
        if grid[i][j]=='G':
            grid[i][j]='R'
for i in range(N):
    for j in range(N):
        color='R'
        if visitRRB[i][j]==0:
            if grid[i][j]=='B':
                color='B'
            bfs(i,j,color,visitRRB)
            cnt += 1
print(cnt)