from collections import deque

def bfs():
    while Q:
        cur=Q.popleft()
        if cur==K:
            return visit[cur]
        nextP(cur-1,cur)
        nextP(cur+1,cur)
        nextP(cur*2,cur)
def nextP(nc,c):
    if 0<=nc<Max and (0==visit[nc] or visit[c]+1 < visit[nc]):
        visit[nc]=visit[c]+1
        Q.append(nc)

N,K=map(int,input().split())
Max=100001
visit=[0]*Max
Q=deque([N])
print(bfs())