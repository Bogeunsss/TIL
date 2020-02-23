import sys;sys.stdin=open('1210.txt','r')
from collections import deque

def bfs(x,y):
    visited[x][y]=1
    Q=deque()
    Q.append((x,y))
    while Q:
        v,w=Q.popleft()
        for i in range(3):
            tx=v+dx[i]
            ty=w+dy[i]
            if tx<0 or tx==100 or ty<0 or ty==100:continue
            if MAP[tx][ty]==0 or visited[tx][ty]:continue
            if MAP[tx][ty]==2: print(y);break
            visited[tx][ty]=1
            Q.append((tx,ty))

dx=[0,0,1]
dy=[-1,1,0]
for _ in range(10):
    T=int(input())
    MAP=[list(map(int,input().split())) for _ in range(100)]
    visited=[[0]*100 for _ in range(100)]
    for i in range(100):
        if MAP[0][i]:
            bfs(0,i)