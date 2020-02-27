# import sys
# def dfs(x,y,d):
#     ans=0
#     if x==N-1 and y==N-1: return 1
#     for i in range(3):
#         if i+d==1:continue # 가로 일 때
#         tx=x+dx[i]
#         ty=y+dy[i]
#         if tx>=N or ty>=N or Map[tx][ty]:continue
#         if i==2 and (Map[x][y+1] or Map[x+1][y]): continue # 대각선 일 때
#         ans+=dfs(tx,ty,i)
#     return ans
# dx=[0,1,1]
# dy=[1,0,1]
# N=int(sys.stdin.readline())
# Map=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# print(dfs(0,1,0))

import sys;input=sys.stdin.readline
N=int(input())
Map=[input().split()+['1'] for _ in range(N)]
Map.append(['1']*(N+1))
wall,road='1','0'

right=[[0]*N for _ in range(N)]
down=[[0]*N for _ in range(N)]
cross=[[0]*N for _ in range(N)]

for i in range(1,N):
    if Map[0][i]=='0':
        right[0][i]=1
    else:break
for i in range(1,N):
    for j in range(1,N):
        if Map[i][j]==road and Map[i-1][j]==road and Map[i][j-1]==road:
            cross[i][j]=right[i-1][j-1]+down[i-1][j-1]+cross[i-1][j-1]
        if Map[i][j]==road:
            right[i][j]=right[i][j-1]+cross[i][j-1]
            down[i][j]=down[i-1][j]+cross[i-1][j]
ans=right[N-1][N-1]+down[N-1][N-1]+cross[N-1][N-1]
print(ans)