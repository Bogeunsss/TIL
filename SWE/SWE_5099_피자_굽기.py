from collections import deque

for T in range(int(input())):
    n,m=map(int,input().split())
    C=list(map(int,input().split()))
    Q=deque()
    for i in range(n):
        Q.append([C[i],i])
    i=0
    while len(Q)!=1:
        Q[0][0]//=2
        if not Q[0][0]:
            if n+i<m:
                Q.popleft()
                Q.append([C[n+i],n+i])
                i+=1
            else:
                Q.popleft()
        else:
            Q.append(Q.popleft())
    print('#%d %d'%(T+1,Q[0][1]+1))