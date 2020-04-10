class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, new):
        if self.head is None:
            self.head = new
            new.prev = new.next = new
        else:
            tail = self.head.prev
            new.prev = tail
            new.next = self.head
            tail.next = new
            self.head.prev = new
        self.size += 1

    def print(self):
        if self.head is None:
            return
        cnt = 0
        cur = self.head.prev
        for _ in range(self.size):
            print(cur.data, end=' ')
            cur = cur.prev
            cnt += 1
            if cnt >= 10: break
        print()

def solution():
    cur = ans.head
    for _ in range(k):
        for _ in range(m):
            cur = cur.next
        prev= cur.prev
        new = Node(prev.data + cur.data, prev, cur)
        prev.next = new
        cur.prev = new
        cur = new
        ans.size += 1

for T in range(int(input())):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = LinkedList()
    for val in arr:
        ans.append(Node(val))
    solution()
    print('#%d'%(T+1), end=' ')
    ans.print()