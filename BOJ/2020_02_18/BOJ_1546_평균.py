n=int(input())
arr=list(map(int,input().split()))
Max=0
for i in range(n):
    if Max<arr[i]:
        Max=arr[i]
hap=0
for i in range(n):
    hap+=(arr[i]/Max)*100
print("%f"%(hap/n))