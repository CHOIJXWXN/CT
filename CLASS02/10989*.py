N = int(input())
nums = [0] * N
for i in range(N):
    nums[i] = int(input())

# nums = []
# for i in range(N):
#     nums.append(int(input()))

# quick sort
i = 0
pivot = nums[i]
for j in range(i):
    while nums[j] > pivot:
        nums[j], nums[j+1] = nums[j+1], nums[j]    