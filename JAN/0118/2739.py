'''
구구단
입력값 저장 후
해당 값을 1부터 9까지 곱한 각각의 값을 출력
'''
num = int(input())                      # 입력값 저장
for i in range(1, 10):                  # i가 1부터 9까지 반복
    print(f'{num} * {i} = {num * i}')   # 입력값 * i = 곱 형식 출력