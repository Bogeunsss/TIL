def perm(n,k,d1,d2,d3,d4):
    global Max,Min
    if k==N:
        Max=max(Max,n)
        Min=min(Min,n)
        return
    if d1:perm(n+num[k],k+1,d1-1,d2,d3,d4)
    if d2:perm(n-num[k],k+1,d1,d2-1,d3,d4)
    if d3:perm(n*num[k],k+1,d1,d2,d3-1,d4)
    if d4:perm(int(n/num[k]),k+1,d1,d2,d3,d4-1)

for T in range(int(input())):
    N=int(input())
    a,b,c,d,=map(int,input().split())
    num=list(map(int,input().split()))
    Max,Min=-1e9,1e9
    perm(num[0],1,a,b,c,d)
    print('#%d %d'%(T+1,Max-Min))