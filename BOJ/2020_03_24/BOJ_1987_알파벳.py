import sys;input=sys.stdin.readline
def dfs(x,y,z):
    global cnt
    cnt=max(cnt,z)
    visit[ord(alpha[x][y])-ord('A')]=1
    for i in range(4):
        tx=x+dx[i]
        ty=y+dy[i]
        if tx<0 or tx>=r or ty<0 or ty>=c:continue
        if not visit[ord(alpha[tx][ty])-ord('A')]:
            visit[ord(alpha[tx][ty])-ord('A')]=1
            dfs(tx,ty,z+1)
            visit[ord(alpha[tx][ty])-ord('A')]=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]
r,c=map(int,input().split())
alpha=[list(input().strip()) for _ in range(r)]
visit=[0]*26
cnt=0
dfs(0,0,1)
print(cnt)