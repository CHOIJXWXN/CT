'''
비밀 이메일
N(문자열 길이)의 약수 페어 a < b 중 가장 큰 a값을 R, 그와 짝인 값을 C
이를 R * C 행렬에 1행에 C개 ~ R행에 C개 순서로 알파벳 추가할 때,
1열에 R개 ~ C열에 R개 순서로 암호화한 것을 해독
'''
code = input()                                  # 입력값 저장
length = len(code)                              # 이메일 길이
for i in range(int(length**(1/2)), 0, -1):      # R의 후보 중 최댓값은 sqrt(N)이므로 sqrt(N)부터 1까지 1씩 줄어드는 range 반복
    if (length % i == 0):                       # 나누어 떨어지면 R과 C를 구하고 반복문 탈출
        R = i
        C = length // R
        break
for i in range(R):                              # 여기서부터는 계산 영역
    for j in range(C):
        print(code[j * R + i], end = '')