import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    visit[x][y]=1
    for dx,dy in (-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1):
        tx,ty=x+dx,y+dy
        if tx<0 or tx>=n or ty<0 or ty>=m: continue
        if not visit[tx][ty] and store[tx][ty]:
            dfs(tx,ty)

n,m=map(int,input().split())
store=[list(map(int,input().split())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if not visit[i][j] and store[i][j]:
            dfs(i,j)
            ans+=1
print(ans)