for T in range(int(input())):
    N=int(input())
    string = ''
    for _ in range(N):
        a,b=input().split()
        for i in range(int(b)):
            if len(string)%11==0:
                string+='\n'
            string+=a
    print(string)