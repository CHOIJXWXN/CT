'''
촌수
dfs문제이지만 따로 함수 정의하지 않고 해봄
'''
N = int(input())
family = [0] * (N + 1)
a, b = map(int, input().split())
anc1, anc2 = [a], [b]                               # 조상 리스트 생성
ans = 0
T = int(input())
for _ in range(T):
    parent, child = map(int, input().split())
    family[child] = parent                          # 부모는 하나임을 이용

while True:
    if not (a or b):                                # a와 b 모두 0이 되면
        break                                       # 반복문 탈출
    a = family[a]                                   # a를 a의 부모로 업데이트
    b = family[b]                                   # b를 b의 부모로 업데이트
    if a:                                           # a가 0이 아니면
        anc1.append(a)                              # a의 조상 리스트에 추가
    if b:
        anc2.append(b)

for i in range(len(anc1)):                          # a와 b 조상들 모두 반복
    for j in range(len(anc2)):
        if anc1[i] == anc2[j]:                      # 겹칠 때
            ans = i + j                             # 촌수 계산
            break
    else:                                           # 이중 for문 탈출 (exit을 쓰려니 print를 해야해서 못 씀ㅠ)
        continue
    break

print(ans) if ans else print(-1)