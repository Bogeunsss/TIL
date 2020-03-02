def dfs(x,y):
    global cnt
    visit[x][y]=1
    branch.append(rooms[x][y])
    cnt+=1
    for i in range(4):
        tx=x+dx[i]
        ty=y+dy[i]
        if tx<0 or tx>=N or ty<0 or ty>=N:continue
        if visit[tx][ty]:continue
        if rooms[tx][ty]-rooms[x][y]==1:
            dfs(tx,ty)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for T in range(int(input())):
    N=int(input())
    rooms=[list(map(int,input().split())) for _ in range(N)]
    MAX_num=MAX_cnt=0
    branch=[]
    # for i in range(N):
    #     for j in range(N):

    for i in range(N):
        for j in range(N):
            if len(branch)>0:
                if rooms[i][j] in branch: continue
                else: branch.clear()
            visit = [[0] * N for _ in range(N)]
            cnt = 0
            dfs(i, j)
            if cnt>MAX_cnt:
                MAX_cnt=cnt
                MAX_num=rooms[i][j]
            elif cnt==MAX_cnt:
                MAX_num=min(MAX_num,rooms[i][j])
    print('#%d %d %d'%(T+1,MAX_num,MAX_cnt))
# from collections import deque
#
# def bfs(x,y):
#     global cnt
#     visit[x][y]=1
#     cnt+=1
#     Q=deque()
#     Q.append((x,y))
#     while Q:
#         for i in range(4):
#             tx=x+dx[i]
#             ty=y+dy[i]
#             if tx<0 or tx>=N or ty<0 or ty>=N:continue
#             if visit[tx][ty]:continue
#             if rooms[tx][ty]-rooms[x][y]==1:
#                 visit[tx][ty]=1
#                 cnt+=1
#                 Q.append((tx,ty))
#
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
# for T in range(int(input())):
#     N=int(input())
#     rooms=[list(map(int,input().split())) for _ in range(N)]
#     MAX_num=MAX_cnt=0
#     for i in range(N):
#         for j in range(N):
#             visit=[[0]*N for _ in range(N)]
#             cnt=0
#             bfs(i,j)
#             if cnt>MAX_cnt:
#                 MAX_cnt=cnt
#                 MAX_num=rooms[i][j]
#             elif cnt==MAX_cnt:
#                 MAX_num=min(MAX_num,rooms[i][j])
#     print('#%d %d %d'%(T+1,MAX_num,MAX_cnt))