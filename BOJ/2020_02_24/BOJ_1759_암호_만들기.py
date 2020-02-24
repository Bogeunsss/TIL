def permutation(k,idx):
    if k==L:
        vowels_cnt=0
        not_vowels=0
        for i in ans:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                vowels_cnt+=1
                continue
            not_vowels+=1
        if vowels_cnt>=1 and not_vowels>=2:
            print(''.join(ans))
    else:
        for i in range(idx,C):
            if visit[i]:continue
            visit[i]=1
            ans.append(hint[i])
            permutation(k+1,i)
            ans.pop()
            visit[i]=0

L,C=map(int,input().split())
hint=sorted(input().split())
visit=[0]*C
ans=[]
permutation(0,0)