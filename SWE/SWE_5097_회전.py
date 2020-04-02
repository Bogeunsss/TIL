from collections import deque
for T in range(int(input())):
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    Q=deque()
    for i in x:
        Q.append(i)
    for _ in range(m):
        nx=Q.popleft()
        Q.append(nx)
    print('#%d %d'%(T+1,Q.popleft()))