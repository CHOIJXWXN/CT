T = int(input())
results = []
for i in range(T):
    R, S = map(str, input().split())
    result = ''
    for s in S:
        result += s * int(R)
    results.append(result)
for result in results:
    print(result)