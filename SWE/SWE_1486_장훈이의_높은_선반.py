import sys;sys.stdin=open('1486.txt','r')

def subset(n):
    global Min
    for i in range(1<<n):
        temp=[]
        for j in range(n):
            if i&(1<<j):temp.append(c[j])
        if sum(temp)>=B:
            if Min>sum(temp)-B:
                Min=sum(temp)-B
for T in range(int(input())):
    N,B=map(int,input().split())
    c=list(map(int,input().split()))
    Min=0xffffffffffff
    visit=[0]*N
    subset(len(c))
    print('#%d %d'%(T+1,Min))