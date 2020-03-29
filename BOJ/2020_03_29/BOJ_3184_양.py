from collections import deque
def bfs(i,j):
    global sheep, wolf
    Q=deque()
    Q.append((i,j))
    visit[i][j]=1
    o,v=0,0
    while Q:
        x,y=Q.popleft()
        if yard[x][y]=='o': o+=1
        if yard[x][y]=='v': v+=1
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if tx<0 or tx>=r or ty<0 or ty>=c:continue
            if visit[tx][ty]==0 and yard[tx][ty]!='#':
                Q.append((tx,ty))
                visit[tx][ty]=1
    if o>v: sheep+=o
    else: wolf+=v

dx=[-1,1,0,0]
dy=[0,0,-1,1]
r,c=map(int,input().split())
yard=[list(input().strip()) for _ in range(r)]
visit=[[0]*c for _ in range(r)]
sheep=wolf=0
for i in range(r):
    for j in range(c):
        if visit[i][j]==0 and yard[i][j]!='#':
            bfs(i,j)
print(sheep,wolf)