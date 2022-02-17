N = int(input())
order = []
for i in range(N):
    order.append(input())
order = list(set(order))
order.sort()
order.sort(key = len)
for word in order:
    print(word)