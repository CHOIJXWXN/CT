'''
컵홀더
일반석 S는 양 옆에 컵홀더 O
커플석 LL은 중간에 컵홀더 X
컵홀더를 사용할 수 있는 최대 사람의 수 출력
'''
N = int(input())    # 사람 수 입력값 저장
seat = input()      # 좌석 상태 문자열 저장
# 일반석은 *S*로, 커플석은 *LL*로, 컵홀더가 겹치는 **부분은 *로 변환하여 *개수 저장
holder = seat.replace('S', '*S*').replace('LL', '*LL*').replace('**', '*').count('*')
# 컵홀더보다 사람이 많을 때는 컵홀더의 개수를, 그렇지 않으면 사람 수를 출력
print(holder) if holder < N else print(N)