dial=[[],[],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
s=input()
seconds=0
for i in range(len(s)):
    for j in range(len(dial)):
        if s[i] in dial[j]:
            seconds+=j+1
print(seconds)