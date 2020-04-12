from collections import deque
def bfs():
    Q=deque([(sx-1,sy-1,sz-1)])
    while Q:
        x,y,z=Q.popleft()
        if x==ex-1 and y==ey-1 and z==ez-1:
            print(visit[x][y][z])
        else:
            for i in range(1,4):
                tx=x+dx[z]*i
                ty=y+dy[z]*i
                if tx<0 or tx>=n or ty<0 or ty>=m: break
                if status[tx][ty]: break
                if not visit[tx][ty][z]:
                    Q.append((tx,ty,z))
                    visit[tx][ty][z]=visit[x][y][z]+1
            for i in range(4):
                if i==z: continue
                k=2 if (i+z)%4==1 else 1
                if not visit[x][y][i]:
                    Q.append((x,y,i))
                    visit[x][y][i]=visit[x][y][z]+k

dx=[0,0,1,-1]
dy=[1,-1,0,0]
n,m=map(int,input().split())
status=[list(map(int,input().split())) for _ in range(n)]
visit=[[[0]*4 for _ in range(m)] for _ in range(n)]
sx,sy,sz=map(int,input().split())
ex,ey,ez=map(int,input().split())
bfs()