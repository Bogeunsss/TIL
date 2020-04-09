class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, idx, node):
        if self.head is None or idx == 0:
            if self.head is None:
                self.head = self.tail = node
            else:
                node.next = self.head
                self.head = node
            self.size += 1
        elif idx >= self.size:
            self.append(node)
        else:
            pre, cur = None, self.head
            for _ in range(idx):
                pre = cur
                cur = cur.next
            pre.next = node
            node.next = cur
            self.size += 1

    def delete(self, idx):
        if self.head is None or idx == 0:
            if self.head is None: return
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        elif idx >= self.size:
            if self.head is None: return
            pre, cur = None, self.head
            while cur.next is not None:
                pre = cur
                cur = cur.next
            if pre is None:
                self.head = self.tail = None
            else:
                pre.next = None
                self.tail = pre
        else:
            pre, cur = None, self.head
            for _ in range(idx):
                pre = cur
                cur = cur.next
            pre.next = cur.next
        self.size -= 1

    def index(self, idx):
        if self.head is None:
            return
        cur = self.head
        for _ in range(idx):
            cur = cur.next
        return cur.data

    def change(self, idx, data):
        if self.head is None:
            return
        cur = self.head
        for _ in range(idx):
            cur = cur.next
        cur.data = data

for T in range(int(input())):
    n, m, l = map(int, input().split())
    lst = list(map(int, input().split()))
    myList = LinkedList()
    for element in lst:
        myList.append(Node(element))
    for _ in range(m):
        cmd = list(input().split())
        if cmd[0] == 'I':
            myList.insert(int(cmd[1]), Node(int(cmd[2])))
        elif cmd[0] == 'D':
            myList.delete(int(cmd[1]))
        elif cmd[0] == 'C':
            myList.change(int(cmd[1]), int(cmd[2]))
    if myList.size>l:
        print('#%d %d' %(T+1, myList.index(l)))
    else:
        print('#%d %d' %(T+1, -1))

# for T in range(int(input())):
#     n,m,l=map(int,input().split())
#     lst=list(map(int,input().split()))
#     for _ in range(m):
#         cmd=list(input().split())
#         if cmd[0]=='I':
#             lst.insert(int(cmd[1]),int(cmd[2]))
#         elif cmd[0]=='D':
#             del lst[int(cmd[1])]
#         elif cmd[0]=='C':
#             lst[int(cmd[1])]=int(cmd[2])
#     if len(lst)>l:
#         print('#%d %d'%(T+1,lst[l]))
#     else:
#         print('#%d %d'%(T+1,-1))