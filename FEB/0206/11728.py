'''
배열 합치기
'''
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.extend(B)
print(*sorted(A))