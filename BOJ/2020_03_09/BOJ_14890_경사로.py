import sys;input=sys.stdin.readline
def slope(x,chk):
    global ans
    cnt=1
    for y in range(n-1):
        dir=Map[x][y+1]-Map[x][y] if chk else Map[y+1][x]-Map[y][x]
        if dir==0:
            cnt+=1
        elif dir==1 and cnt>=l:cnt=1
        elif dir==-1 and cnt>=0:cnt=1-l
        else:return
    if cnt>=0:ans+=1

n,l=map(int,input().split())
Map=[list(map(int,input().split())) for _ in range(n)]
ans=0
for i in range(n):
    slope(i,1)
    slope(i,0)
print(ans)