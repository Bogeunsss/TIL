'''
1 7 19 37 61
1 6 12 18 24
'''

N=int(input())
bee=[1]
a=1
for i in range(20000):
    # if bee[i]+(6*a)>1000000000:break
    bee.append(bee[i]+(6*a))
    a+=1
    if bee[i]>=N:print(a-1);break