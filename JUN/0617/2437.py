"""
저울

n까지 모두 나타낼 수 있다고 치자                         이 때 s = n + 1
그 다음 수가 m일 때,
(1 ~ n) 과 m 의 조합으로 수를 나타낼 수 있음
즉, m이 n + 2이면 n + 1은 나타낼 수 없음
m이 n + 1 이하일 때에만 지속 가능
지속 가능할 때에는 이제 1부터 n + m까지 나타낼 수 있음       이 때 s = n + m + 1
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
