from collections import deque
def bfs():
    Q=deque()
    Q.append((0,0,0))
    distance[0][0][0]=1
    while Q:
        x,y,z=Q.popleft()
        if x==n-1 and y==m-1:
            return distance[x][y][z]
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if tx<0 or tx>=n or ty<0 or ty>=m:continue
            if distance[tx][ty][z]:continue
            if Map[tx][ty]=='0':
                distance[tx][ty][z]=distance[x][y][z]+1
                Q.append((tx,ty,z))
            if Map[tx][ty]=='1' and z==0:
                distance[tx][ty][1]=distance[x][y][z]+1
                Q.append((tx,ty,1))
    return -1

dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())
Map=[list(input()) for _ in range(n)]
distance=[[[0,0] for _ in range(m)] for _ in range(n)]
print(bfs())