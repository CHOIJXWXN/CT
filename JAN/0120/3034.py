'''
앵그리 창영
상자에 성냥을 담을 수 있는지 판별
상자의 대각선 길이보다 성냥이 작거나 같아야 통과
'''
N, W, H = map(int, input().split())     # 입력값 저장
max_len = (W ** 2 + H ** 2) ** (1/2)    # 대각선 길이 저장
matches = []                            # 성냥 길이를 저장할 리스트 생성
for i in range(N):                      # N개의 성냥을 위해 반복
    matches.append(int(input()))        # 각각의 입력값을 리스트에 추가
for i in range(N):                      # 길이 판별을 위해 N번 반복
    if matches[i] > max_len:            # 성냥 길이가 대각선 길이보다 길면
        print('NE')                     # NE 출력
    else:
        print('DA')                     # 아니면 (짧거나 같으면) DA 출력