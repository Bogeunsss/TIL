from collections import deque
def bfs(_x,_y,_z):
    Q=deque([(_x,_y,_z)])
    while Q:
        x,y,z=Q.popleft()
        j=4 if z==k else 12
        if x==h-1 and y==w-1:
            return visit[x][y][z]
        for i in range(j):
            tx=x+dx[i]
            ty=y+dy[i]
            tz=z if i<4 else z+1
            if tx<0 or tx>=h or ty<0 or ty>=w:continue
            if visit[tx][ty][tz] or Map[tx][ty]:continue
            visit[tx][ty][tz]=visit[x][y][z]+1
            Q.append((tx,ty,tz))
    return -1

dx=[-1,1,0,0,-2,-2,2,2,-1,1,-1,1]
dy=[0,0,-1,1,-1,1,-1,1,2,2,-2,-2]
k=int(input())
w,h=map(int,input().split())
Map=[list(map(int,input().split())) for _ in range(h)]
visit=[[[0]*(k+1) for _ in range(w)] for _ in range(h)]
print(bfs(0,0,0))