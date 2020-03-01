def dfs(k,SUM):
    global ans
    if k==11:
        ans=ans if ans>SUM else SUM
    else:
        for i in range(11):
            if check[i] or ability[k][i]==0: continue
            check[i]=True
            dfs(k+1,SUM+ability[k][i])
            check[i]=False

for T in range(int(input())):
    ability=[list(map(int,input().split())) for _ in range(11)]
    check=[False]*11
    ans=0
    dfs(0,0)
    print(ans)