cards = list(range(1, int(input()) + 1))
result = []
for i in range(len(cards)):
    result.append(cards.pop(0))
    if cards:
        cards.append(cards[0])
        cards.pop(0)
    else:
        break
print(*result)