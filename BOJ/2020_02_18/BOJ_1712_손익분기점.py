A,B,C=map(int,input().split())
BEP=0
if B>=C:BEP=-1
else:BEP=A//(C-B)+1
print(BEP)