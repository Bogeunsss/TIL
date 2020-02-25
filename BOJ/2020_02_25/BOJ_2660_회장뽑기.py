from collections import deque

def bfs(s):
    visit=[0]*(N+1)
    Q=deque()
    Q.append(s)
    visit[s]=1
    level=0
    while Q:
        for _ in range(len(Q)):
            v=Q.popleft()
            for w in G[v]:
                if visit[w]:continue
                visit[w]=1
                Q.append(w)
        if Q:
            level+=1
    return level

N=int(input())
G=[[] for _ in range(N+1)]
leader=[]
ls=100
while True:
    x,y=map(int,input().split())
    if x==-1 and y==-1:break
    G[x].append(y)
    G[y].append(x)
for i in range(1,N+1):
    score=bfs(i)
    if score<ls:
        if leader:
            leader=[]
        leader.append(i)
        ls=score
    elif score==ls:
        leader.append(i)
print(ls,len(leader))
leader.sort()
print(*leader)