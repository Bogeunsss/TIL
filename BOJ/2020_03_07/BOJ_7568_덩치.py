N=int(input())
data=[tuple(map(int,input().split())) for _ in range(N)]
for i in data:
    s=1
    for j in data:
        if i[0]<j[0] and i[1]<j[1]:s+=1
    print(s,end=' ')