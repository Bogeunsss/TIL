import sys;sys.stdin=open('1289.txt','r')

for T in range(int(input())):
    origin=input()
    n=len(origin)
    init=[0 for _ in range(n)]
    cnt=0
    for i in range(n):
        if int(origin[i])!=init[i]:
            for j in range(i,n):
                init[j]=int(origin[i])
            cnt+=1
    print(cnt)

# for T in range(int(input())):
#     bit = input()
#     first = [0] * len(bit)
#     cnt = 0
#     now=bit[0]
#     if now=='1': cnt+=1
#     for i in range(1,len(bit)):
#         if now!=bit[i]:
#             cnt+=1
#             now=bit[i]
#     print(cnt)

