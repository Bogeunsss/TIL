N,M=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
ans=[]

def permutation(k,m):
    if k==m:
        for i in range(m):print(ans[i],end=' ')
        print()
    else:
        for i in nums:
            if i in ans:continue
            ans.append(i)
            permutation(k+1,m)
            ans.pop()

permutation(0,M)