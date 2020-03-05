for T in range(int(input())):
    N=int(input())
    cnt=0
    MAX=0
    ans=[0]*10001
    ans[0]=1
    S=list(map(int,input().split()))
    for i in range(N):
        MAX+=S[i]
        for j in range(MAX,-1,-1):
            if ans[j]:ans[j+S[i]]+=1
        ans[S[i]]+=1
    for i in range(10001):
        if ans[i]:cnt+=1
    print('#%d %d'%(T+1,cnt))