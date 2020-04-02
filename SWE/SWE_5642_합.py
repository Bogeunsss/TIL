for T in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split()))
    Max=-1e9
    Sum=0
    for i in range(n): # 1 3 -8 18 -8
        Sum+=nums[i]
        Max=max(Sum,Max)
        if Sum<0: Sum=0
    print('#%d %d'%(T+1,Max))