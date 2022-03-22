'''
트리 순회
'''
import sys

def preorder(r):
    print(chr(r + ord('A')), end = '')
    if c[r][0]:
        preorder(c[r][0])
    if c[r][1]:
        preorder(c[r][1])
def inorder(r):
    if c[r][0]:
        inorder(c[r][0])
    print(chr(r + ord('A')), end = '')
    if c[r][1]:
        inorder(c[r][1])
def postorder(r):
    if c[r][0]:
        postorder(c[r][0])
    if c[r][1]:
        postorder(c[r][1])
    print(chr(r + ord('A')), end = '')

N = int(input())
c = [[0, 0] for _ in range(26)]
for _ in range(N):
    P, C1, C2 = map(str, sys.stdin.readline().split())
    if C1 != '.':
        c[ord(P) - ord('A')][0] = ord(C1) - ord('A')
    if C2 != '.':
        c[ord(P) - ord('A')][1] = ord(C2) - ord('A')
preorder(0)
print()
inorder(0)
print()
postorder(0)

'''
  A
B   C

pre  : A > B > C
in   : B > A > C
post : B > C > A

              1
      2               3
  4       5       6       7
8   9                  10   11

pre  : 1 > 2 > 4 > 8 > 9 > 5 > 3 > 6 > 7 > 10 > 11
in   : 8 > 4 > 9 > 2 > 5 > 1 > 6 > 3 > 10 > 7 > 11
post : 8 > 9 > 4 > 5 > 2 > 6 > 10 > 11 > 7 > 3 > 1
'''