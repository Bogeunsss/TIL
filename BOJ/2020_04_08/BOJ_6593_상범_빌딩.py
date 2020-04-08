from collections import deque
def bfs(i,j,k):
    Q=deque([(i,j,k)])
    while Q:
        x,y,z=Q.popleft()
        if building[x][y][z]=='E':
            return f'Escaped in {visit[x][y][z]} minute(s).'
        for i in range(6):
            tx=x+dx[i]
            ty=y+dy[i]
            tz=z+dz[i]
            if tx<0 or tx>=l or ty<0 or ty>=r or tz<0 or tz>=c: continue
            if visit[tx][ty][tz] or building[tx][ty][tz]=='#': continue
            visit[tx][ty][tz]=visit[x][y][z]+1
            Q.append((tx,ty,tz))
    return 'Trapped!'
dx=[0,0,1,-1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]
while True:
    l,r,c = map(int,input().split())
    if l==0 and r==0 and c==0: break
    building=[]
    ex=ey=ez=0
    for i in range(l):
        temp=[]
        for j in range(r):
            temp.append(list(input()))
        space=input()
        building.append(temp)
    visit=[[[0]*c for _ in range(r)] for _ in range(l)]
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k]=='S':
                    print(bfs(i,j,k))