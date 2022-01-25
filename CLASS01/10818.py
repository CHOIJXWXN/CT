N = int(input())
numbers = list(map(int, input().split()))
sort_num = sorted(numbers) 
print(sort_num[0], sort_num[-1])