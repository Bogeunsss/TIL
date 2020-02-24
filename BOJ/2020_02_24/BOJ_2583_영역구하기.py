from collections import deque

def bfs(x,y):
    global cnt
    Q=deque()
    Q.append((x,y))
    visit[x][y]=1
    cnt+=1
    while Q:
        v,w=Q.popleft()
        for i in range(4):
            tx=v+dx[i]
            ty=w+dy[i]
            if tx<0 or tx==M or ty<0 or ty==N:continue
            if visit[tx][ty] or Map[tx][ty]!=0:continue
            visit[tx][ty]=1
            cnt+=1
            Q.append((tx,ty))
    return 1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
M,N,K=map(int,input().split())
Map=[[0]*N for _ in range(M)]
visit=[[0]*N for _ in range(M)]
ans=[]
for i in range(K):
    r1,c1,r2,c2=map(int,input().split())
    for j in range(r1,r2):
        for k in range(c1,c2):
            Map[k][j]=1

for i in range(M):
    for j in range(N):
        if Map[i][j]==0 and visit[i][j]==0:
            cnt=0
            bfs(i,j)
            ans.append(cnt)
ans.sort()
print(len(ans))
print(*ans)