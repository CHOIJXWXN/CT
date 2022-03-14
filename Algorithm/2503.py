'''
숫자 야구
'''

N = int(input())
nums = [str(a) + str(b) + str(c) for a in range(1, 10) for b in range(1, 10) for c in range(1, 10) if a != b and b != c and c != a]
for _ in range(N):
    n, s, b = map(int, input().split())
    for num in reversed(nums):
        S, B = 0, 0 
        for i in range(3):
            if str(n)[i] == num[i]:
                S += 1
            elif str(n)[i] in num:
                B += 1
        if (S, B) != (s, b):
            nums.remove(num)
print(len(nums))