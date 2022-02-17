'''
최대공약수와 최소공배수
두 수 중 작은 수를 골라
그보다 작거나 같은 수 중에서 두 수와 나누어 떨어지는 수를 고르고
그 중 가장 큰 수 = 최대공약수
최대공약수 X 최소공배수 = 두 수의 곱 이므로
두 수의 곱 // 최대공약수 = 최소공배수
'''
num1, num2 = map(int, input().split())      # 두 수 입력값 저장
min_num = min(num1, num2)                   # 두 수 중 작은 수
gcd = 0                                     # 최대공약수 초기화
for i in range(1, min_num + 1):             # 1부터 min_num까지 반복
    if num1 % i == 0 and num2 % i == 0:     # num1과 num2에 동시에 나누어 떨어지면
        gcd = i                             # 최대공약수 변경 저장
print(gcd)                                  # 최대공약수 출력
print(num1 * num2 // gcd)                   # (두 수의 곱 // 최대공약수) 출력 (최소공배수)