dx=[-1,0,1,0]
dy=[0,1,0,-1]
N,M=map(int,input().split())
r,c,d=map(int,input().split())
Map=[list(map(int,input().split())) for _ in range(N)]
cnt=0
while True:
    if Map[r][c]==0:
        Map[r][c]=2
        cnt+=1
    if Map[r+1][c]!=0 and Map[r-1][c]!=0 and Map[r][c+1]!=0 and Map[r][c-1]!=0:
        if Map[r-dx[d]][c-dy[d]]==1:
            break
        else:
            r-=dx[d]
            c-=dy[d]
    else:
        d=(d+3)%4
        if Map[r+dx[d]][c+dy[d]]==0:
            r+=dx[d]
            c+=dy[d]
print(cnt)