a,b,c=map(int,input().split())
if a>=b and a>=c:
    if b>c:
        ans=b
    else:
        ans=c
elif b>=a and b>=c:
    if a>c:
        ans=a
    else:
        ans=c
else:
    if a>b:
        ans=a
    else:
        ans=b
print(ans)