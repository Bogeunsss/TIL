def dfs(x,y):
    res=1
    visit[x][y]=True
    for i in range(4):
        tx,ty=x+dx[i],y+dy[i]
        if tx<0 or tx>=n or ty<0 or ty>=m:continue
        if not (visit[tx][ty] or Map[tx][ty]):
            res+=dfs(tx,ty)
    return res
def solve(wall,x,y):
    global virus,visit
    if wall==3:
        cnt=0
        visit=[[False]*m for _ in range(n)]
        for i,j in v:
            cnt+=dfs(i,j)
        virus=min(virus,cnt)
        return
    for i in range(x,n):
        k=y if i==x else 0
        for j in range(k,m):
            if Map[i][j]==0:
                Map[i][j]=1
                solve(wall+1,i,j+1)
                Map[i][j]=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
n,m=map(int,input().split())
Map=[list(map(int,input().split())) for _ in range(n)]
visit=[[False]*m for _ in range(n)]
v,safe,virus=[],-3,100
for i in range(n):
    for j in range(m):
        if Map[i][j]!=1:safe+=1
        if Map[i][j]==2:v.append((i,j))
solve(0,0,0)
print(safe-virus)