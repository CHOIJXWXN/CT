'''
딱지놀이
'''
N = int(input())
for i in range(N):
    flag = True
    a, *A = map(int, input().split())
    b, *B = map(int, input().split())
    for j in range(4, 0, -1):
        if A.count(j) > B.count(j):
            print('A')
            flag = False
            break
        elif A.count(j) < B.count(j):
            print('B')
            flag = False
            break
    if flag:
        print('D')