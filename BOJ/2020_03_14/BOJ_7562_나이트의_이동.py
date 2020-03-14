from collections import deque
def bfs():
    Q=deque()
    Q.append((srcX,srcY))
    while Q:
        x,y=Q.popleft()
        if x==desX and y==desY:
            print(board[x][y])
            return
        for i in range(8):
            tx=x+dx[i]
            ty=y+dy[i]
            if tx<0 or tx>=n or ty<0 or ty>=n:continue
            if board[tx][ty]:continue
            board[tx][ty]=board[x][y]+1
            Q.append((tx,ty))

dx=[2,1,-1,-2,-2,-1,1,2]
dy=[1,2,2,1,-1,-2,-2,-1]
for _ in range(int(input())):
    n=int(input())
    srcX,srcY=map(int,input().split())
    desX,desY=map(int,input().split())
    board=[[0]*n for _ in range(n)]
    bfs()