n=int(input())
arr=list(map(int,input().split()))
a=b=0
size=len(arr)
if size==1:print('A')
elif size==2:
    if arr[0]==arr[1]:print(arr[0])
    else:print('A')
elif size>2:
    flag=True
    for i in range(size-1):
        if i==0:
            current=arr[i]
            next=arr[i+1]
            afterNext=arr[i+2]
            if next-current==0:
                a=0
                b=next-(current*a)
            else:
                a=(afterNext-next)//(next-current)
                b=next-current*a
        data=arr[i]*a+b
        nextData=arr[i+1]
        if data!=nextData:
            flag=False
    if flag:
        print(arr[-1]*a+b)
    else:
        print('B')