n=int(input())
G=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if G[j][k]==1 or (G[j][i] ==1 and G[i][k]==1):
                G[j][k]=1
for i in range(n):
    for j in range(n):
        print(G[i][j],end=' ')
    print()