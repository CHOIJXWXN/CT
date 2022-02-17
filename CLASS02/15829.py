L = int(input())
word = input()
hash_sum = 0
r = 31
M = 1234567891
for i in range(L):
    hash_sum += (ord(word[i]) - 96) * (r ** i)
print(hash_sum % M)