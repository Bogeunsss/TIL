n,m=map(int,input().split())
friends=[[n for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    friends[a-1][b-1]=1
    friends[b-1][a-1]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j: friends[i][j]=0
            else: friends[i][j]=min(friends[i][j],friends[i][k]+friends[k][j])

bacon=[sum(x) for x in friends]
print(bacon.index(min(bacon))+1)