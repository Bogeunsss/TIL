# class Node:
#     def __init__(self, d=0, n=None):
#         self.data=d
#         self.next=n
#
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.size=0
#
#     def append(self, node):
#         if self.head==None:
#             self.head=node
#         else:
#             cur=self.head
#             while cur.next!=None:
#                 cur=cur.next
#             cur.next=node
#
#     def insert(self, idx, node):
#         curNode=self.head
#         prevNode=self.head
#         curIdx=0
#         if idx==0:
#             if self.head:
#                 nextNode=self.head
#                 self.head=node
#                 self.head.next=nextNode
#             else:
#                 self.head=node
#         else:
#             while curIdx<idx:
#                 if curNode:
#                     prevNode=curNode
#                     curNode=curNode.next
#                 else:
#                     break
#                 curIdx+=1
#             if curIdx==idx:
#                 node.next=curNode
#                 prevNode.next=node
#             else:
#                 return -1
#
# for T in range(int(input())):
#     n,m,l=map(int,input().split())
#     lst=list(map(int,input().split()))
#     index_info=[list(map(int,input().split())) for _ in range(m)]
#     ans=LinkedList()

for T in range(int(input())):
    n,m,l=map(int,input().split())
    lst=list(map(int,input().split()))
    for _ in range(m):
        idx,data=map(int,input().split())
        lst.insert(idx,data)
    print('#%d %d'%(T+1,lst[l]))
