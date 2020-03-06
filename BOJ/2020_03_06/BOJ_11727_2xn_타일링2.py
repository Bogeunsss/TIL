def tiles(n):
    ans=0
    tmp1=1
    tmp2=3
    for i in range(1,n+1):
        if i==1:ans+=1
        elif i==2:ans+=2
        else:
            ans=tmp1*2+tmp2
            tmp1=tmp2
            tmp2=ans
    return ans
ans=tiles(int(input()))
print(ans%10007)