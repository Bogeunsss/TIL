for T in range(int(input())):
    n=int(input())
    arr=[]
    hap=0
    for i in range(n):
        m=int(input())
        arr.append(m)
        hap+=m
    avg=hap//n
    total=0
    for i in range(n):
        if arr[i]<avg:
            total+=avg-arr[i]
    print("#%d %d"%(T+1,total))