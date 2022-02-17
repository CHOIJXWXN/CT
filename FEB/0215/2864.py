'''
5와 6의 차이
최댓값 : 5를 모두 6으로 변환하여 더한 값
최솟값 : 6을 모두 5로 변환하여 더한 값
'''
A, B = map(str, input().split())
print(int(A.replace('6', '5')) + int(B.replace('6', '5')), int(A.replace('5', '6')) + int(B.replace('5', '6')))