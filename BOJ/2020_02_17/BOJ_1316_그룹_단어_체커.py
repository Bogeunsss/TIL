N=int(input())
cnt=0
for i in range(N):
    checker = [0] * 26
    word=input()
    checker[ord(word[0])-97]+=1
    flag=True
    for j in range(1,len(word)):
        if word[j-1]!=word[j] and checker[ord(word[j])-97]>0:
            flag=False
            break
        checker[ord(word[j])-97]+=1
    if flag:cnt+=1
print(cnt)