numbers = list(map(int, input().split()))
sum = 0
for number in numbers:
    sum += number ** 2
print(sum % 10)