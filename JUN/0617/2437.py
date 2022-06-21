"""
저울

a ~ m로
K까지 모두 나타낼 수 있다고 치자                         이 때 s = K + 1
그 다음 수가 n일 때,
1, ..., K과 n, 1 + n, ..., K + n 나타낼 수 있음
즉, n이 K + 2이면 K + 1은 나타낼 수 없음
n이 K + 1 이하일 때에만 지속 가능
지속 가능할 때에는 이제 1부터 K + n까지 나타낼 수 있음       이 때 s = K + n + 1

14225 참고
"""
import sys

N = int(input())        # 입력
num = list(map(int, sys.stdin.readline().rstrip().split()))
num.sort()              # 정렬
s = 1                   # 현재 나타내지 못하는 수 중 최솟값 (즉 현재 연속적으로 나타낼 수 있는 최댓값 + 1)
for n in num:
    if s < n:           # s가 n보다 작으면 s는 더이상 지속 불가
        break
    s += n              # s가 n보다 크거나 같으면 + n
print(s)
