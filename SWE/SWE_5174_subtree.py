def BinarySearchTree(x):
    global ans
    visit[x] = 1
    ans += 1
    for w in G[x]:
        if visit[w]: continue
        BinarySearchTree(w)

for T in range(int(input())):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[] for _ in range(e+2)]
    visit = [0]*(e+2)
    ans = 0
    for i in range(0,len(arr),2):
        G[arr[i]].append(arr[i+1])
    BinarySearchTree(n)
    print('#%d %d' %(T+1, ans))