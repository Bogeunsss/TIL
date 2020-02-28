board=[[0 for x in range(101)] for y in range(101)]
n=int(input())
for T in range(1,n+1):
    a,b,c,d=map(int,input().split())
    for i in range(a,a+c):
        for j in range(b,b+d):
            board[i][j]=T
for i in range(1,n+1):
    cnt=0
    for j in range(len(board)):
        for k in range(len(board[j])):
            if board[j][k]==i:
                cnt+=1
    print(cnt)