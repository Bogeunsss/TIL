from collections import deque

def bfs(x,y):
    global cnt
    visit[x][y]=1
    Q = deque()
    Q.append((x,y))
    while Q:
        v,w=Q.popleft()
        for i in range(4):
            tx=v+dx[i]
            ty=w+dy[i]
            if tx<0 or tx==N or ty<0 or ty==N:continue
            if town[tx][ty]==0 or visit[tx][ty]:continue
            cnt+=1
            visit[tx][ty]=1
            Q.append((tx,ty))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
N=int(input())
town=[list(map(int,list(input()))) for _ in range(N)]
visit=[[0]*N for _ in range(N)]
danzi=[]
for i in range(N):
    for j in range(N):
        if town[i][j] and not visit[i][j]:
            cnt=1
            bfs(i,j)
            danzi.append(cnt)
print(len(danzi))
danzi.sort()
for i in range(len(danzi)):
    print(danzi[i])