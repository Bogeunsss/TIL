def d(n):
    m=n
    arr=[]
    while m>0:
        arr.append(m%10)
        m//=10
    new_n=n
    for idx in arr:
        new_n+=idx
    return new_n

ans=[1 for x in range(10001)]
for i in range(1,10001):
    x=d(i)
    if x<=10000:
        ans[x]-=1
for i in range(1,10001):
    if ans[i]==1:
        print(i)