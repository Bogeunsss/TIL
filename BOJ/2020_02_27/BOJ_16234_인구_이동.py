from collections import deque
def bfs(x,y):
    global move
    visit = set()
    visit.add((x,y))
    Q=deque()
    Q.append((x,y))
    Sum,n=0,0
    while Q:
        v,w=Q.popleft()
        Sum+=population[v][w]
        n+=1
        for i in range(4):
            tx=v+dx[i]
            ty=w+dy[i]
            if tx<0 or tx==N or ty<0 or ty==N:continue
            if ty<N and (tx,ty) not in visit and (tx,ty) not in total_visit:
                d=abs(population[tx][ty]-population[v][w])
                if L<=d<=R:
                    move=True
                    Q.append((tx,ty))
                    visit.add((tx,ty))
    return Sum//n,visit

dx=[-1,1,0,0]
dy=[0,0,-1,1]
N,L,R=map(int,input().split())
population=[list(map(int,input().split())) for _ in range(N)]
ans=0
while True:
    total_visit=set()
    move=False
    alliance=[]
    for i in range(N):
        for j in range(N):
            if (i,j) not in total_visit:
                moved,visit=bfs(i,j)
                alliance.append((moved,visit))
                total_visit|=visit
    for (moved,alli) in alliance:
        for city in alli:
            x,y=city
            population[x][y]=moved
    if not move:break
    ans+=1
print(ans)