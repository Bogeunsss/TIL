from collections import deque
def bfs(x,y):
    Q=deque([(x,y,20)])
    visit=[(x,y,20)]
    while Q:
        dx,dy,beer=Q.popleft()
        if dx==store[-1][0] and dy==store[-1][1]: print('happy');return
        for tx,ty in store:
            if (tx,ty,20) not in visit:
                if beer*50>=abs(tx-dx)+abs(ty-dy):
                    Q.append((tx,ty,20))
                    visit.append((tx,ty,20))
    print('sad')

for t in range(int(input())):
    n=int(input())
    hx,hy=map(int,input().split())
    store=[list(map(int,input().split())) for _ in range(n+1)]
    bfs(hx,hy)