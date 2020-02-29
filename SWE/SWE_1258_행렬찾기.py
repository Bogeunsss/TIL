import sys;sys.stdin=open('1258.txt','r')

for T in range(int(input())):
    N=int(input())
    m=[list(map(int,input().split())) for _ in range(N)]
    visit=[[0]*N for _ in range(N)]
    l,size=[],[]
    for i in range(N):
        for j in range(N):
            if m[i][j] and not visit[i][j]:
                sub_m = []
                di,dj=i,j
                while True:
                    if m[di][dj]==0:break
                    temp = []
                    while True:
                        if m[di][dj]==0:break
                        temp.append(m[di][dj])
                        visit[di][dj]=1
                        dj+=1
                    di+=1
                    dj=j
                    sub_m.append(temp)
                c=len(sub_m[0])
                r=len(sub_m)
                l.append((r,c))
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j][0]*l[j][1]>l[j+1][0]*l[j+1][1]:
                l[j],l[j+1]=l[j+1],l[j]
            if l[j][0]*l[j][1]==l[j+1][0]*l[j+1][1]:
                if l[j][0]>l[j+1][0]:
                    l[j],l[j+1]=l[j+1],l[j]
    print('#%d %d'%(T+1,len(l)),end=' ')
    for i in range(len(l)):
        for j in range(len(l[i])):
            print('%d'%l[i][j],end=' ')
    print()