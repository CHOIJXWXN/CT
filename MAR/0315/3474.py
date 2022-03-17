'''
교수가 된 현우
n!의 값에서 오른쪽에서부터 0이 몇 개가 붙어 있는지 계산
0의 몇 개냐? = 10의 몇 제곱의 배수이냐?

소인수분해 : 소수의 곱으로 나타내는 것 ex) 36 = 2 * 2 * 3 * 3 = 2^2 * 3^2
                              ex) 98 = 2 * 7 * 7 = 2 * 7^2

10은 2 * 5이기 때문에 n!을 소인수분해 했을 때 2^i * 5^j * ... 라면 n!은 10^min(i, j)의 배수
1부터 임의의 수 x까지 무조건 j보다 i가 큼

            1 2 3 4 5 6 7 8 9 10
5의 배수              1         1
2의 배수        1   2   1   3   1

따라서 n이 10의 몇 제곱의 배수인지 알기 위해서는 그 안에 5의 배수가 몇 번 들어가는지 알면 됨

100에는 5의 배수가 몇 개가 있을까? > 20개
그럼 100!은 10^20으로만 나누어떨어질까? X

1 * 2 * 3 * 4 * 5 * ... * 10 * ... 15 * ... 20 * ... * 25 * ... * 30 * ...
                                                        ^
                                        여기에서 5가 두 번 곱해짐 (하지만 우리는 한 번만 셈)

따라서 25의 배수가 몇 개 있는지, 125의 배수가 몇 개, 625의 배수...다 구해야 함

1. n까지 5의 배수 개수 구하기 = n // 5 개
2. n까지 25의 배수 개수 구하기 = n // 25 개
3. ...

개수가 0이 될 때까지 혹은 n보다 5^x가 커질 때까지 반복하면 됨

똑같은 문제는 아니지만 야옹님 문제집에 있는 1407번 문제도 배수에 관련된 문제니 참고
'''
import sys
T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    cnt = 0
    i = 5               # 시작은 5의 배수 개수 구하기
    while True:         # 무한 반복 시작
        if i > n:       # 나누는 수가 나누어질 수보다 커지면 (어차피 몫이 0이 나올 테니까)
            break       # 반복문 탈출
        cnt += n // i   # i의 배수 개수를 cnt에 추가
        i *= 5          # 5면 25로, 25면 125로, 125면 625로, ... 업데이트
    print(cnt)