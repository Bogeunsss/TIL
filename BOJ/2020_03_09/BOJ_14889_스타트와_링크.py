import sys;input=sys.stdin.readline
def dfs(cnt,idx):
    global ans
    if idx==n:return
    if cnt==n//2:
        start=link=0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    start+=teams[i][j]
                if not visit[i] and not visit[j]:
                    link+=teams[i][j]
        ans=min(ans,abs(start-link))
        return
    visit[idx]=True
    dfs(cnt+1,idx+1)
    visit[idx]=False
    dfs(cnt,idx+1)
n=int(input())
teams=[list(map(int,input().split())) for _ in range(n)]
visit=[False]*n
ans=1e9
dfs(0,0)
print(ans)