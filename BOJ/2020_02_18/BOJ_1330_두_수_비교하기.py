A,B=map(int,input().split())
if A==B:
    ans='=='
elif A>B:
    ans='>'
else:
    ans='<'
print(ans)