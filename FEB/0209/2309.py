'''
일곱 난쟁이
일곱 난쟁이 키의 합이 100이어야 함
그렇게 골라낸 일곱 난쟁이를 키 순으로 정렬
'''
heights = [int(input()) for i in range(9)]      # 9명의 키 입력값 저장

out = sum(heights) - 100                        # 빼내야 할 두 난쟁이의 키의 합 계산
flag = True                                     # 이중 for문 탈출을 위한 플래그

for i in range(8):                              # 첫번째부터 여덟번째까지 반복
    for j in range(i+1, 9):                     # 위에서 고른 난쟁이의 다음 번째 부터 아홉번째까지 반복
        if heights[i] + heights[j] == out:      # 그렇게 고른 두 난쟁이의 키의 합이 out과 같다면
            heights.remove(heights[j])          # 난쟁이 키 리스트에서 제거
            heights.remove(heights[i])          # 난쟁이 키 리스트에서 제거 (2)
            flag = False                        # 이중 for문 탈출을 위한 플래그 변경
            break                               # 안쪽 for문 탈출
    if not flag:                                # 플래그 이용하여
        break                                   # 바깥쪽 for문 탈출

for height in sorted(heights):                  # 정렬된 키 리스트에서
    print(height)                               # 모든 키 요소 반복 출력