def Hanoi_tower(n,t1,t2,t3):
    global cnt
    cnt+=1
    if n==1:
        move.append((t1,t3))
    else:
        Hanoi_tower(n-1,t1,t3,t2)
        move.append((t1,t3))
        Hanoi_tower(n-1,t2,t1,t3)

N=int(input())
cnt=0
move=[]
Hanoi_tower(N,1,2,3)
print(cnt)
for i in range(len(move)):
    print(*move[i])