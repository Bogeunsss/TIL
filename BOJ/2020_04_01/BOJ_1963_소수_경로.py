from collections import deque
def bfs():
    Q=deque([(a,0)])
    while Q:
        c,cnt=Q.popleft()
        if c==b: return cnt
        strc=str(c)
        cnt+=1
        for i in range(4):
            for j in map(str,range(10)):
                if i==0 and j=='0':continue
                n=int(strc[:i]+j+strc[i+1:])
                if primes[n] and not visit[n]:
                    visit[n]=1
                    Q.append((n,cnt))
    return 'Impossible'

N=10000
primes=[False,False]+[True]*(N-1)
for i in range(2,N+1):
    if primes[i]:
        for j in range(2*i,N+1,i):
            primes[j]=False

for T in range(int(input())):
    visit=[0]*(N+1)
    a,b=map(int,input().split())
    print(bfs())