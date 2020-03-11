n=int(input())
nums=[0,1,1]
for i in range(3,91):
    nums.append(nums[i-2]+nums[i-1])
print(nums[n])