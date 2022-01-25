A = int(input())
B = int(input())
C = int(input())
nums = [0] * 10
mul = A * B * C
while mul >= 1:
    nums[mul % 10] += 1
    mul //= 10
for num in nums:
    print(num)