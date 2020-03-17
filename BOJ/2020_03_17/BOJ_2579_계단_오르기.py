n=int(input())
stairs=[int(input()) for _ in range(n)]
ans=[[] for _ in range(n)]
for i in range(n):
    if i==0:
        ans[i].append(stairs[0])
    elif i==1:
        ans[i].append(stairs[0]+stairs[1])
    elif i==2:
        ans[i].append(max(ans[0][0]+stairs[2],stairs[1]+stairs[2]))
    else:
        ans[i].append(max(stairs[i]+stairs[i-1]+ans[i-3][0],stairs[i]+ans[i-2][0]))
print(ans[-1][0])