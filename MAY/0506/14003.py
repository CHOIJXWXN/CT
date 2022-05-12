'''
가장 긴 증가하는 부분 수열 5
12015 참고
'''
import sys

read = sys.stdin.readline
N = int(read())
A = list(map(int, read().split()))
d = [A[0]]              # 가장 작은 값으로 계속 업데이트 될 리스트
idx = [0] * N           # d의 값이 바뀔 때마다 해당 값이 몇 번째에 삽입되는지 그 index를 저장할 리스트
lenD = 0                # 총 길이 - 1
for i in range(N):
    if d[-1] < A[i]:                # d 중에서 가장 큰 값이 현재 비교할 값보다 작으면
        d.append(A[i])              # d의 마지막에 현재값 추가
        lenD += 1                   # 길이 + 1
        idx[i] = lenD               # idx 리스트에 현재값의 index 대입
    else:
        s, e = 0, len(d)
        while s < e:
            m = (s + e) // 2
            if d[m] < A[i]:
                s = m + 1
            else:
                e = m
        d[e] = A[i]                 # d의 값 업데이트
        idx[i] = e                  # idx 리스트에 현재값의 index 대입
print(lenD + 1)
print(d)
print(idx)
ans = list()
for i in range(N - 1, -1, -1):      # idx 리스트의 마지막부터 거꾸로 반복
    if idx[i] == lenD:              # index를 하나씩 줄여가며 제일 뒤의 값을 찾아 ans에 추가
        ans.append(A[i])
        lenD -= 1
print(*reversed(ans))
