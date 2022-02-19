'''
빙고
3번 빙고가 될 때 몇 번째 수를 부른 순간인지
'''
bingo = [0] * 12        # 가로 0~4 세로 5~9 우상향 10 우하향 11
my_bingo = [0] * 25     # 1부터 25까지 각각 좌표값 저장
result = 0              # 몇 번째 숫자인지 저장할 변수
flag = True

# 나의 빙고판 입력값 저장 (숫자 N은 my_bingo의 N - 1인덱스에 행과 열, 즉 좌표값 저장)
for i in range(5):
    line = list(map(int, input().split()))
    for j in range(5):
        my_bingo[line[j] - 1] = [i, j]

# 사회자가 번호를 부르는 중
for i in range(5):
    ans = list(map(int, input().split()))
    
    if not flag:    # 이미 빙고가 3개 이상 완성되었으면
        continue    # 사회자 말이 끝날 때까지 계속 continue
    
    # 사회자가 한 줄에 불렀던 다섯 숫자 반복
    for j in range(5):
        bingo[my_bingo[ans[j] - 1][0]] += 1                             # 해당되는 가로 + 1
        bingo[my_bingo[ans[j] - 1][1] + 5] += 1                         # 해당되는 세로 + 1
        if my_bingo[ans[j] - 1][0] + my_bingo[ans[j] - 1][1] == 4:      # 우상향 빙고 + 1
            bingo[10] += 1                                                  
        if my_bingo[ans[j] - 1][0] == my_bingo[ans[j] - 1][1]:          # 우하향 빙고 + 1
            bingo[11] += 1
        
        if bingo.count(5) >= 3:                                         # 빙고가 3개 이상이 되면
            result = 5 * i + j + 1                                      # 지금 부르는 숫자가 몇 번째인지 계산하고
            flag = False                                                # flag 전환 (더 이상 계산하지 않기 위함)
            break                                                       # 반복문 탈출

print(result)