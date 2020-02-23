def permutation(k,idx,n):
    global ans
    if k==M:
        Min=0
        for r1 in range(N):
            for c1 in range(N):
                if town[r1][c1]==1:
                    chickenStreet=0xffffffffffff
                    for i in range(M):
                        r2,c2=store[i][0],store[i][1]
                        tmp=abs(r1-r2)+abs(c1-c2)
                        if chickenStreet>tmp:
                            chickenStreet=tmp
                    Min+=chickenStreet
        if ans>Min:
            ans=Min
    else:
        for i in range(idx,n):
            if visit[i]:continue
            visit[i]=1
            store.append(chicken[i])
            permutation(k+1,i,n)
            store.pop()
            visit[i]=0

N,M=map(int,input().split())
town=[list(map(int,input().split())) for _ in range(N)]
chicken=[(i,j) for j in range(N) for i in range(N) if town[i][j]==2]
n=len(chicken)
visit=[0]*n
store=[]
ans=0xffffffffffff
permutation(0,0,n)
print(ans)