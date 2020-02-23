# n=input()
# ans=n
# cycle=0
# while True:
#     if len(ans)>1:
#         x, y = ans[0], ans[1]
#     else:
#         x, y = '0', ans[0]
#     new_n=str(int(x)+int(y))
#     ans=y+new_n[-1]
#     cycle+=1
#     if ans[0]=='0':
#         if ans[-1]==n:
#             break
#     else:
#         if ans==n:
#             break
# print(cycle)

n=int(input())
nums=list(map(int,input().split()))
Max=Min=num[0]
for i in range(1,n):
    if Max<nums[i]:
        Max=nums[i]
    if Min>nums[i]:
        Min=nums[i]
print(Min,Max)