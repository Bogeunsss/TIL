import copy

R,C,T=map(int,input().split())
Map=[]
cleaner=[]
for i in range(R):
    temp=list(map(int,input().split()))
    if temp[0]==-1:
        cleaner.append(i)
    Map.append(temp)
visit=[[0]*C for _ in range(R)]
dx,dy=[-1,1,0,0],[0,0,-1,1]

def diffuse(Map):
    diffused = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if Map[i][j]==-1:continue
            cnt=0
            for k in range(4):
                tx=i+dx[k]
                ty=j+dy[k]
                if tx<0 or tx==R or ty<0 or ty==C:continue
                if Map[tx][ty]==-1:continue
                diffused[tx][ty]+=Map[i][j]//5
                cnt+=1
            diffused[i][j]+=Map[i][j]-Map[i][j]//5*cnt
    diffused=clean(diffused)
    Map = copy.deepcopy(diffused)
    return Map
def clean(diffused):
    for  i in reversed(range(1,cleaner[0]+1)):
        diffused[i][0]=diffused[i-1][0]
    diffused[0]=diffused[0][1:]+[0]
    for i in range(cleaner[0]):
        diffused[i][C-1]=diffused[i+1][C-1]
    diffused[cleaner[0]]=[-1,0]+diffused[cleaner[0]][1:C-1]

    for i in range(cleaner[1],R-1):
        diffused[i][0]=diffused[i+1][0]
    diffused[R-1]=diffused[R-1][1:]+[0]
    for i in reversed(range(cleaner[1]+1,R)):
        diffused[i][C-1]=diffused[i-1][C-1]
    diffused[cleaner[1]]=[-1,0]+diffused[cleaner[1]][1:C-1]
    return diffused

for _ in range(T):
    Map=diffuse(Map)
count=0
for i in range(R):
    for j in range(C):
        if Map[i][j]!=-1:
            count+=Map[i][j]
print(count)