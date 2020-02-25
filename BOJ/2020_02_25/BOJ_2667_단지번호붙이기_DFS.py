def dfs(x,y):
    global cnt
    visit[x][y]=1
    cnt+=1
    for i in range(4):
        tx=x+dx[i]
        ty=y+dy[i]
        if tx<0 or tx==N or ty<0 or ty==N:continue
        if town[tx][ty]=='0' or visit[tx][ty]:continue
        dfs(tx,ty)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
N=int(input())
town=[input() for _ in range(N)]
visit=[[0]*N for _ in range(N)]
danzi=[]
for i in range(N):
    for j in range(N):
        if town[i][j]=='1' and not visit[i][j]:
            cnt=0
            dfs(i,j)
            danzi.append(cnt)
print(len(danzi))
danzi.sort()
for i in range(len(danzi)):
    print(danzi[i])