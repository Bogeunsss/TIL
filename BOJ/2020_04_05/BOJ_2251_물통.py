from collections import deque

def bfs():
    Q.append((0,0))
    visit[0][0]=1
    while Q:
        x,y=Q.popleft()
        z=c-x-y
        if x==0: ans.append(z)
        w=min(x,b-y)
        move(x-w,y+w)
        w=min(x,c-z)
        move(x-w,y)
        w=min(y,a-x)
        move(x+w,y-w)
        w=min(y,c-z)
        move(x,y-w)
        w=min(z,a-x)
        move(x+w,y)
        w=min(z,b-y)
        move(x,y+w)

def move(x,y):
    if not visit[x][y]:
        visit[x][y]=1
        Q.append((x,y))

a,b,c=map(int,input().split())
visit=[[0]*(b+1) for _ in range(a+1)]
ans=[]
Q=deque()
bfs()
ans.sort()
print(*ans)