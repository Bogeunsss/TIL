score=int(input())
if 90<=score<=100:
    ans='A'
elif 80<=score<90:
    ans='B'
elif 70<=score<80:
    ans='C'
elif 60<=score<70:
    ans='D'
else:
    ans='F'
print(ans)