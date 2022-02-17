'''
덩치
'''
N = int(input())    # 사람 수 입력값 저장

unrank = []         # 사람 리스트
rank = []           # 랭킹 순서 리스트

for i in range(N):                                  # 모든 사람 반복
    unrank.append(list(map(int, input().split())))  # 무게 / 키 정보를 리스트로 받아 언랭에 저장

for i in range(N):      # 모든 사람 반복
    cnt = 1             # 자신보다 덩치가 더 큰 사람 수
    for j in range(N):  # 모든 사람 반복
        if unrank[i][0] < unrank[j][0] and unrank[i][1] < unrank[j][1]: # 언랭에 있는 사람 중 자신보다 덩치가 크면
            cnt += 1    # cnt + 1
    rank.append(cnt)    # 랭킹 리스트에 자신보다 덩치가 더 큰 사람의 수를 추가
    
print(*rank)            # 랭킹 리스트 출력