"""
안정적인 문자열
뒤에서부터 판별

}}}{{{}}{}}{{}
s =
close   닫힌 괄호 개수    4
cnt     연산 횟수        1 + (close//2)

"""
import sys
read = sys.stdin.readline

t = 1                               # 테스트케이스 변수
while True:
    s = list(read().rstrip())

    if '-' in s:                    # 탈출 조건
        break

    close, cnt = 0, 0               # 닫는 괄호 수, 연산 수 초기화

    while s:                        # s가 빌 때까지
        last = s.pop()              # s의 마지막 글자 추출

        if last == '}':             # 닫는 괄호이면 + 1
            close += 1
        else:                       # 여는 괄호이면
            if close:                   # 닫는 괄호가 존재하면
                close -= 1              # 걔 삭제
            else:                       # 남은 닫는 괄호 없으면
                cnt += 1                # 연산 한 번 해서 닫는 괄호로 바꿔주기
                close += 1              # 바꿔줬으니 닫는 괄호 + 1

    cnt += close // 2               # 모든 문자열 다 탐색했는데 닫는 괄호가 남아있으면 그 중 반만 여는 괄호로 바꿔주면 되므로 close의 반만 연산에 추가
    print(f'{t}. {cnt}')
    t += 1
