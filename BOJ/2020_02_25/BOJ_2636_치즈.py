from collections import deque

def bfs(x,y):
    visit=[[0]*M for _ in range(N)]
    visit[x][y]=1
    Q=deque()
    Q.append((x,y))
    while Q:
        v,w=Q.popleft()
        for i in range(4):
            tx=v+dx[i]
            ty=w+dy[i]
            if tx<0 or tx==N or ty<0 or ty==M:continue
            if visit[tx][ty]==0:
                if Map[tx][ty]>=1:
                    Map[tx][ty]+=1
                else:
                    Q.append((tx,ty))
                    visit[tx][ty]=1
def melt():
    global p
    isMelt,cnt=False,0
    for i in range(N):
        for j in range(M):
            if Map[i][j]>=2:
                Map[i][j]=0
                isMelt=True
                cnt+=1
    if cnt:p=cnt
    return isMelt

dx=[-1,1,0,0]
dy=[0,0,-1,1]
N,M=map(int,input().split())
Map=[list(map(int,input().split())) for _ in range(N)]
ans=p=0
while True:
    bfs(0,0)
    if melt():
        ans+=1
    else:break

print(ans)
print(p)