N = int(input())
members = []
for i in range(N):
    member = list(input().split())
    member.append(i)
    members.append(member)
members = sorted(members, key = lambda x: (int(x[0]), x[2]))  # int 변환 주의
for i in range(N):
    print(members[i][0], members[i][1])