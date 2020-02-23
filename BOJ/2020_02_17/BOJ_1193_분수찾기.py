'''
1/1
1/2
2/1
3/1
2/2
1/3
1/4
2/3
3/2
4/1
5/1
4/2
3/3
2/4
1/5
'''
# N=int(input())
# i=0
# while N>0:
#     N-=i
#     i+=1
# N=i+N-1
# result=str(N)+'/'+str(i-N)
# if i%2==0:
#     result=str(i-N)+'/'+str(N)
# print(result)
X,i,s=int(input()),2,1
while X>s:print(i,s);s+=i;i+=1