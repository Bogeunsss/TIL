# from collections import deque
# def bfs(x,y):
#     visit[x][y]=1
#     baechu[x][y]=0
#     Q=deque()
#     Q.append((x,y))
#     while Q:
#         v,w=Q.popleft()
#         for i in range(4):
#             tx=v+dx[i]
#             ty=w+dy[i]
#             if tx<0 or tx==N or ty<0 or ty==M:continue
#             if visit[tx][ty] or baechu[tx][ty]==0: continue
#             visit[tx][ty]=1
#             baechu[tx][ty]=0
#             Q.append((tx,ty))
#     return 1
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
# for T in range(int(input())):
#     M,N,K=map(int,input().split())
#     baechu=[[0]*M for _ in range(N)]
#     visit=[[0]*M for _ in range(N)]
#     cnt=0
#     for _ in range(K):
#         u,v=map(int,input().split())
#         baechu[v][u]=1
#     for i in range(N):
#         for j in range(M):
#             if baechu[i][j]==0 or visit[i][j]:continue
#             cnt+=bfs(i,j)
#     print(cnt)

def dfs(x,y):
    visit[x][y]=1
    for i in range(4):
        tx=x+dx[i]
        ty=y+dy[i]
        if tx<0 or tx==N or ty<0 or ty==M:continue
        if visit[tx][ty] or Baechu[tx][ty]==0:continue
        dfs(tx,ty)
    return 1

dx=[-1,1,0,0]
dy=[0,0,-1,1]
for T in range(int(input())):
    M,N,K=map(int,input().split())
    Baechu=[[0]*M for _ in range(N)]
    visit=[[0]*M for _ in range(N)]
    cnt=0
    for _ in range(K):
        X,Y=map(int,input().split())
        Baechu[Y][X]=1
    for i in range(N):
        for j in range(M):
            if Baechu[i][j]==0 or visit[i][j]:continue
            cnt+=dfs(i,j)
    print(cnt)