import sys;sys.stdin=open('1234.txt','r')

for T in range(1,11):
    n,nums=input().split()
    ans=[]
    ans.append(nums[0])
    for i in range(1,int(n)):
        if len(ans) and ans[-1]==nums[i]:
            del ans[-1]
        else:
            ans.append(nums[i])
    print('#%d %s'%(T,''.join(list(map(str,ans)))))