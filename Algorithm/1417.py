'''
국회의원 선거
'''
N = int(input())
cs = list()
DS = int(input())
for _ in range(N - 1):
    m = int(input())
    if m >= DS:
        cs.append(m)
cnt = 0
while True:
    cs.sort()
    if not cs or DS >= cs[-1]:
        if cs and DS == cs[-1]:
            cnt += 1
        break
    cnt = cnt + (cs[-1] - DS) // 2 + 1 if (cs[-1] - DS) % 2 else cnt + (cs[-1] - DS) // 2
    DS += cnt
    cs[-1] -= cnt
print(cnt)