import sys;sys.setrecursionlimit(100000)
input=sys.stdin.readline

def dfs(idx,group):
    visit[idx]=group
    for i in G[idx]:
        if not visit[i]:
            if not dfs(i,-group): return False
        elif visit[i]==visit[idx]:return False
    return True

for T in range(int(input())):
    V,E=map(int,input().split())
    G=[[] for _ in range(V+1)]
    visit=[0]*(V+1)
    ans=True
    for _ in range(E):
        u,v=map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    for i in range(1,V+1):
        if not visit[i]:
            if not dfs(i,1):
                ans=False
                break
    print("YES" if ans else "NO")