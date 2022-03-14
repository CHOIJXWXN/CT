'''
나의 인생에는 수학과 함께

BOJ1987 (알파벳) 문제처럼 순열 + dfs 문제
1. 0, 0부터 아래쪽과 오른쪽만 탐색
2. 거쳐간 칸의 모든 값을 큐에 추가
3. N-1, N-1에 도착하면 식 계산
4. 되돌아가서 다른 길로 가보기 위해서 계산 후에는 넣었던 값을 다시 큐에서 제거
5. 3에서 계산한 값 중 가장 큰 값과 가장 작은 값 출력
'''

def dfs(r, c):
    rs = 0
    if r == N - 1 and c == N - 1:               # 3
        formula.append(path[N - 1][N - 1])
        temp = formula[:]
        rs += int(temp.pop(0))
        while temp:
            op = temp.pop(0)
            if op == '+':
                rs += int(temp.pop(0))
            elif op == '-':
                rs -= int(temp.pop(0))
            elif op == '*':
                rs *= int(temp.pop(0))
        rs_list.append(rs)
        return
    formula.append(path[r][c])                  # 2
    if 0 <= r + 1 < N:
        dfs(r + 1, c)                           # 1
        formula.pop()                           # 4
    if 0 <= c + 1 < N:
        dfs(r, c + 1)                           # 1
        formula.pop()                           # 4

N = int(input())
path = list()
formula = list()
rs_list = list()
for i in range(N):
    path.append(input().replace(' ', ''))
dfs(0, 0)
print(max(rs_list), min(rs_list))               # 5