import math

A,B,V=map(float,input().split())
if V==A:print(1)
else:print(int(math.ceil((V-A)/(A-B)))+1)

'''
30 = 7-4+7-4+7-4+7-4+7-4+7-4+7-4+7-4+7
5 = 2-1+2-1+2-1+2-1+2
'''