def BinarySearchTree(v):
    global SUM
    if v*2>n:
        SUM += G[v]
    else:
        BinarySearchTree(v*2)
        if v*2 != n:
            BinarySearchTree(v*2+1)

for T in range(int(input())):
    n, m, l = map(int, input().split())
    G = [[] for _ in range(n+1)]
    SUM = 0
    for _ in range(m):
        node, value = map(int, input().split())
        G[node] = value
    BinarySearchTree(l)
    print('#%d %d' %(T+1, SUM))