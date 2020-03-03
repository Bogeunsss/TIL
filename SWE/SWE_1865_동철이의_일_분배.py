# N-Queen 문제
# def adjacent(x):
#     for i in range(x):
#         if row[x]==row[i] or abs(row[x]-row[i])==x-i:
#             return False
#     return True
# def nQueen(x):
#     global cnt
#     if x==N:
#         cnt+=1
#     else:
#         for i in range(N):
#             row[x]=i
#             if adjacent(x):
#                 nQueen(x+1)
# for T in range(int(input())):
#     N=int(input())
#     row=[0]*N
#     cnt=0
#     nQueen(0)
#     print('#%d %d'%(T+1,cnt))
# def adjacent(x):
#     for i in range(x):
#         if R[x]==R[i] or abs(R[x]-R[i])==x-i: return False
#         return True
# def dfs(x):
#     if x==N:
#         pass
#     else:
#         for i in range(N):
#             R[x]=i
#             if adjacent(x):
#                 dfs(x+1)
# for T in range(int(input())):
#     N=int(input())
#     P=[list(map(int,input().split())) for _ in range(N)]
#     R=[0]*N
#     for i in range(N):
#         dfs(i)

def dfs(SUM,cnt):
    global MAX
    if SUM<=MAX:return
    if cnt==N:
        MAX=max(MAX,SUM)
    for i in range(N):
        if visit[i]==0:
            visit[i]=1
            dfs(SUM*P[cnt][i],cnt+1)
            visit[i]=0
for T in range(int(input())):
    N=int(input())
    P=[list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            P[i][j]/=100
    MAX=0
    visit=[0]*N
    dfs(100,0)
    print('#%d %.6f'%(T+1,MAX))