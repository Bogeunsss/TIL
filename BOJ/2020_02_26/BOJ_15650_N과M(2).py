def permutation(k,idx):
    if k==M:
        print(*ans)
    else:
        for i in range(idx,N+1):
            if visit[i]:continue
            visit[i]=1
            ans.append(i)
            permutation(k+1,i)
            ans.pop()
            visit[i]=0

N,M=map(int,input().split())
visit=[0]*(N+1)
ans=[]
permutation(0,1)