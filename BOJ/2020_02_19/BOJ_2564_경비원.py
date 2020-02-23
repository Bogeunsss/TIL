# def fix(direction, location, n):
#     if direction==1:
#         block[0][location]=n
#     elif direction==2:
#         block[len(block)-1][location]=n
#     elif direction==3:
#         block[location][0]=n
#     else:
#         block[location][len(block)-1]=n
# def clockwise(x,y,n):
#     cnt=0
#     flag=False
#     if x==1 or x==4:
#         d=1
#     else:
#         d=-1
#     while True:
#         for i in range(len(block[0])):
#             x+=d
#             cnt+=1
#             if x<0 or x>len(block[0])-1: cnt-=1;x-=d;break
#             if block[y][x] == n: flag = True;break
#         if flag:
#             break
#         for j in range(len(block)):
#             y+=d
#             cnt+=1
#             if y<0 or y>len(block)-1: cnt-=1;y-=d;break
#             if block[y][x] == n: flag = True;break
#         if flag:
#             break
#         d*=-1
#     return cnt
#
# row,col=map(int,input().split())
# path=2*row+2*col
# stores=int(input())
# block=[[0 for x in range(row+1)] for y in range(col+1)]
# SUM=0
# for i in range(stores):
#     d,l=map(int,input().split())
#     fix(d,l,i+1)
# X,Y=map(int,input().split())
# fix(X,Y,4)
# if X==1:
#     x,y=Y,0
# elif X==2:
#     x,y=Y,len(block)
# elif X==3:
#     x,y=0,Y
# else:
#     x,y=len(block[0]),Y
#
# for i in range(stores):
#     temp=clockwise(x,y-1,i+1)
#     if temp>path-temp:
#         SUM+=path-temp
#     else:
#         SUM+=temp
# print("%d"%SUM)

# 2 번 째 시도
row,col=map(int,input().split())
row+=1;col+=1
path=2*row+2*col
stores=int(input())
storeFromLeft=0
playerFromLeft=0
storeFromTop=0
playerFromTop=0
clockwise=0
for i in range(stores):
    d,l=map(int,input().split())
    if d==1:
        storeFromLeft=l
    elif d==2:
        storeFromLeft=l
    elif d==3:
        storeFromTop=l
    else:
        storeFromTop=l
X,Y=map(int,input().split())
if X==1:
    playerFromLeft=Y
    clockwise=playerFromLeft+col+storeFromLeft
elif X==2:
    playerFromLeft=Y
elif X==3:
    playerFromTop=Y
else:
    playerFromTop=Y