import sys;input=sys.stdin.readline
def dfs(idx,res):
    global ans
    if idx>=n//2:
        ans=max(ans,int(res))
    else:
        cur=eval(res+op[idx]+nums[idx+1])
        dfs(idx+1,str(cur))
        if idx+1<n//2:
            after=eval(nums[idx+1]+op[idx+1]+nums[idx+2])
            cur=eval(res+op[idx]+str(after))
            dfs(idx+2,str(cur))
n=int(input())
eq=list(input())
nums,op=[],[]
ans=-1e9
for i in range(n):
    if i%2==0: nums.append(eq[i])
    else: op.append(eq[i])
if n==1: print(nums[0])
elif n==3: print(eval(nums[0]+op[0]+nums[1]))
else:
    dfs(0,nums[0])
    print(ans)