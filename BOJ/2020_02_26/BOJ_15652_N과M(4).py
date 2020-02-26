def permutation(k):
    if k==M:
        for i in range(len(ans)-1):
            if ans[i]>ans[i+1]:return
        print(*ans)
    else:
        for i in range(1,N+1):
            ans.append(i)
            permutation(k+1)
            ans.pop()

N,M=map(int,input().split())
ans=[]
permutation(0)