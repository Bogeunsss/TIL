for T in range(int(input())):
    N=int(input())
    bus=[list(map(int,input().split())) for _ in range(N)]
    P=int(input())
    stop=[0]*(5001)
    for i in range(len(bus)):
        for j in range(bus[i][0],bus[i][1]+1):
            stop[j]+=1
    print("#%d"%(T+1),end=' ')
    for i in range(P):
        c=int(input())
        print(stop[c],end=' ')
    print()