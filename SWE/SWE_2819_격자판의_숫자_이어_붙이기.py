def dfs(x,y,cnt,s):
    global string
    s+=str(board[x][y])+'0'
    cnt+=1
    if cnt==7:
        string.add(s)
    else:
        for i in range(4):
            tx=x+dx[i]
            ty=y+dy[i]
            if tx<0 or tx>=N or ty<0 or ty>=N:continue
            dfs(tx,ty,cnt,s)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
for T in range(int(input())):
    N=4
    board=[list(map(int,input().split())) for _ in range(N)]
    string=set()
    for i in range(N):
        for j in range(N):
            dfs(i,j,0,'')
    print('#%d %d'%(T+1,len(string)))