N,M=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
tmp=[]
S=[]

def permutaion(k,m):
    if k==m:
        if sum(tmp) not in S:
            S.append(sum(tmp))
            for i in range(m):print(tmp[i],end=' ')
            print()
    else:
        for i in range(N):
            if nums[i] in tmp:continue
            tmp.append(nums[i])
            permutaion(k+1,m)
            tmp.pop()
permutaion(0,M)