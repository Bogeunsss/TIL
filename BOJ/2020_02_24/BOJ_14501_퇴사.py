N=int(input())
p,q=[0]*(N+1),[0]*(N+1)
ans=0
for i in range(1,N+1):
    p[i],q[i]=map(int,input().split())

def pay(day,money):
    global ans
    if day==N+1:
        if ans<money:
            ans=money
        return
    if day>N+1:
        return
    pay(day+p[day],money+q[day])
    pay(day+1,money)

pay(1,0)
print(ans)