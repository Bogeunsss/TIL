# from collections import deque
# def isConnect(src,des,d):
#     if d==0:
#         if src==3 or src==5 or src==6: return False
#         else:
#             if des==1 or des==2 or des==5 or des==6: return True
#     elif d==1:
#         if src==2 or src==4 or src==5: return False
#         else:
#             if des==1 or des==3 or des==4 or des==5: return True
#     elif d==2:
#         if src==3 or src==4 or src==7: return False
#         else:
#             if des==1 or des==2 or des==4 or des==7: return True
#     elif d==3:
#         if src==2 or src==6 or src==7: return False
#         else:
#             if des==1 or des==3 or des==6 or des==7: return True
#
# def bfs(_r,_c):
#     Q=deque([(_r,_c)])
#     visit[_r][_c]=1
#     times=1
#     while Q:
#         for _ in range(len(Q)):
#             x,y=Q.popleft()
#             if times==l: return
#             for i in range(4):
#                 tx=x+dx[i]
#                 ty=y+dy[i]
#                 if tx<0 or tx>=n or ty<0 or ty>=m: continue
#                 if not tunnel[tx][ty] or visit[tx][ty]: continue
#                 if isConnect(tunnel[x][y],tunnel[tx][ty],direction[i]):
#                     visit[tx][ty]=1
#                     Q.append((tx,ty))
#         times+=1
#
# dx=[-1,0,1,0]
# dy=[0,-1,0,1]
# direction=[0,1,2,3]
# for T in range(int(input())):
#     n,m,r,c,l=map(int,input().split())
#     tunnel=[list(map(int,input().split())) for _ in range(n)]
#     visit=[[0]*m for _ in range(n)]
#     bfs(r,c)
#     cnt=0
#     for i in range(n):
#         for j in range(m):
#             if visit[i][j]: cnt+=1
#     print('#%d %d'%(T+1,cnt))

from copy import deepcopy
def check(n,r,N):
    global tmp, visit
    if n == N//3+1:
        # print(tmp)
        tmp2=deepcopy(tmp)
        a.append(tmp2)
        return
    else:
        for i in range(r,N):
            if visit[i] == 0:
                tmp.append(i)
                visit[i] = 1
                check(n+1,i,N)
                tmp.pop()
                visit[i] = 0

for tc in range(int(input())):
    N = int(input())
    synergy = [list(map(int,input().split())) for _ in range(N)]
    visit = [0] * N
    tmp =[]
    a = []
    check(0,0,N)
    print(a)