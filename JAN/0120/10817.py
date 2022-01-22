'''
세 수
중간값을 구하는 문제
세 개의 수를 정렬한 뒤
가운데 숫자 출력
'''
three = list(map(int, input().split()))    # 입력값 저장
print(sorted(three)[len(three)//2])        # 정렬 후 가운데 인덱스를 이용하여 출력 (짝수에서는 맞지 않음)