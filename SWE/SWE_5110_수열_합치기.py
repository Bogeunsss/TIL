class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertList(self, lst):
        first = last = Node(lst[0])
        for val in lst[1:]:
            new = Node(val, last)
            last.next = new
            last = new
        if self.head is None:
            self.head = first
            self.tail = last
        else:
            cur = self.head
            while cur is not None:
                if cur.data > lst[0]:
                    break
                cur = cur.next
            if cur is None:
                first.prev = self.tail
                self.tail.next = first
                self.tail = last
            elif cur.prev is None:
                last.next = self.head
                self.head.prev = last
                self.head = first
            else:
                prev = cur.prev
                first.prev = prev
                last.next = cur
                prev.next = first
                cur.prev = last
        self.size += len(lst)

    def printFromEnd(self):
        if self.head is None:
            return
        cur = self.tail
        cnt = 0
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.prev
            cnt += 1
            if cnt == 10: break
        print()

for T  in range(int(input())):
    n, m = map(int, input().split())
    ans = LinkedList()
    for _ in range(m):
        arr = list(map(int,input().split()))
        ans.insertList(arr)
    print('#%d'%(T+1), end=' ')
    ans.printFromEnd()