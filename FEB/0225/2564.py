'''
경비원
왼쪽 위 꼭짓점을 원점으로 해서 펼쳐서 길이 계산
'''
w, h = map(int, input().split())
n = int(input())
stores = []
sum = 0
for i in range(n + 1):
    d, x = map(int, input().split())
    if d == 4:
        x = w + x
    if d == 2:
        x = w + h + w - x
    if d == 3:
        x = w + h + w + h - x
    stores.append(x)
for i in range(n):
    sum += w + h - abs(abs(stores[n] - stores[i]) - (w + h))
print(sum)