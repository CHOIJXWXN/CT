N, M = map(int, input().split())
cards = list(map(int, input().split()))
result_sum = cards[0] + cards[1] + cards[2]
min_diff = M

for first in range(N - 2):
    for second in range(first + 1, N - 1):
        for last in range(second + 1, N):
            sum_card = cards[first] + cards[second] + cards[last]
            diff = M - sum_card
            if 0<= diff < min_diff:
                min_diff = diff
                result_sum = sum_card
print(result_sum)