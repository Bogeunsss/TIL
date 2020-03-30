from collections import deque
def bfs():
    visit=[0]*n
    Q=deque([A])
    while Q:
        v=Q.popleft()
        if v==B:
            w=[]
            while v!=A:
                w.append(cmd[v])
                v=path[v]
            print(''.join(map(str,w[::-1])))
        else:
            tv=(v*2%n,v-1 if v else n-1,v%m*10+v//m,v//10+v%10*m)
            for i in range(4):
                if not visit[tv[i]]:
                    visit[tv[i]]=1
                    path[tv[i]]=v
                    cmd[tv[i]]=c[i]
                    Q.append(tv[i])
n,m,c=10000,1000,'DSLR'
path=[0]*n
cmd=[0]*n
for T in range(int(input())):
    A,B=map(int,input().split())
    bfs()