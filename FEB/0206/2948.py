'''
2009년
'''
D, M = map(int, input().split())
thirtyone = [1, 3, 5, 7, 8, 10, 12]
thirty = [4, 6, 9, 11]
for i in range(1, M):
    if i in thirtyone:
        D += 31
    elif i in thirty:
        D += 30
    elif i == 2:
        D += 28

day = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
print(day[D%7])