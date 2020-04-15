# 유클리드 알고리즘
'''
a>b 일 때
n=a%b
만약 n==0 이면 b가 최대 공약수(GCD)
n!=0 이면 a=b, b=n 하고 반복
'''


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0

    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x, y
for T in range(int(input())):
    a,b=map(int,input().split())
    print('#%d'%(T+1),end=' ')
    print(*egcd(a,b))