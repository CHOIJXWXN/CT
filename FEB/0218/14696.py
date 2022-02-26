'''
딱지놀이
'''
N = int(input())
for i in range(N):
    a, *A = map(int, input().split())
    b, *B = map(int, input().split())
    for j in range(4, 0, -1):
        if A.count(j) > B.count(j):
            print('A')
            break
        elif A.count(j) < B.count(j):
            print('B')
            break
    else:
        print('D')