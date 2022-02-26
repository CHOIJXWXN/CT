'''
수열
연속해서 증가(일정)하거나 연속해서 감소(일정)한 수열의 길이의 최댓값
'''
N = int(input())
nums = list(map(int, input().split()))
asc, desc, max_cnt = 1, 1, 1
# 전체 반복
for i in range(N - 1):
    # 갈수록 커지면
    if nums[i] - nums[i + 1] < 0:
        # 오름차순 + 1
        asc += 1
        # 계속 max 업데이트
        max_cnt = max(max_cnt, asc)
        # 올랐기 때문에 내림차순은 다시 원점
        desc = 1
    # 갈수록 작아지면
    elif nums[i] - nums[i + 1] > 0:
        desc += 1
        max_cnt = max(max_cnt, desc)
        asc = 1
    # 앞뒤가 같으면 둘 다 포함이므로 둘 다 커지고 max 업데이트
    else:
        asc += 1
        desc += 1
        max_cnt = max(max_cnt, max(asc, desc))
print(max_cnt)