'''
상근이의 체스판
[{('X'를 B개 출력), ('.'를 B개 출력), ..., ()를 C개 출력}
...
{}를 A개 출력]
[]를 R개 출력
'''
R, C = map(int, input().split())                # R, C 입력값 저장
A, B = map(int, input().split())                # A, B 입력값 저장
for r in range(R):                              # [] R개 출력해야 하므로 R만큼 반복
    if r % 2:                                   # []가 홀수번째 줄이라면
        black = '.'
        white = 'X'
    else:                                       # []가 짝수번째 줄이라면
        black = 'X'
        white = '.'
    for a in range(A):                          # {} A개 출력해야 하므로 A만큼 반복
        for c in range(C):                      # () C개 출력해야 하므로 C만큼 반복
            if c % 2:                           # ()가 홀수번째 요소라면
                print(white * B, end = '')      # white를 B개 연속 출력
            else:                               # ()가 짝수번째 요소라면
                print(black * B, end = '')      # black을 B개 연속 출력
        print()                                 # 하나의 {}가 다 출력되면 개행