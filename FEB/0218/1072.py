'''
게임
현재 승률에서 몇 게임을 더 이겨야 승률이 오르는지 계산 (이후 게임은 모두 이긴다고 가정)

Z = Y * 100  (버림)
      X

Z + 1 = (Y + i) * 100   (버림)
            (X + i)

(Z + 1) * (X + i) = (Y + i) * 100

(Z + 1)*X + (Z + 1)*i = 100*Y + 100*i

(Z + 1)*X - 100*Y = 100*i - (Z + 1)*i

(Z + 1)*X - 100*Y = (100 - Z - 1)*i

i = (Z + 1)*X - 100*Y
       100 - Z - 1

해당 i가 정수라면 그대로 그대로 출력
해당 i가 소숫점 뒷자리를 가진다면 올림으로 출력
'''
X, Y = map(int, input().split())
Z = Y * 100 // X
if Z == 99 or Z == 100:
    print('-1')
# else:
#     i = 1
#     while True:
#         if ((Y + i) * 100 // (X + i)) - Z == 1:
#             print(i)
#             break
#         i += 1
else:
    game = (((Z + 1) * X) - 100 * Y) / (100 - Z - 1)
    if game % 1 > 1e-6:
        print(int(game) + 1)
    else:
        print(int(game))