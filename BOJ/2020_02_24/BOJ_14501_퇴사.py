def pay(n,day):
    global money
    if n>=N:return
    if schedule[n][0]>=day:
        if schedule[n][0]==day:money+=schedule[n][1]
        return
    money+=schedule[n][1]
    pay(n+schedule[n][0],day-schedule[n][0])
N=int(input())
# schedule[0] : Ti, schedule[1]: Pi
schedule=[list(map(int,input().split())) for _ in range(N)]
Max=0
for i in range(N):
    money=0
    pay(i,N-i)
    if Max<money:
        Max=money
print(Max)