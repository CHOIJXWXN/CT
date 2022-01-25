word = input().upper()
char_num = {}

for char in set(word):
    char_num[char] = 0

for char in word:
    char_num[char] += 1

alphabets = []
for alphabet, cnt in char_num.items():
    if cnt == max(char_num.values()):
        alphabets.append(alphabet)
if len(alphabets) == 1:
    print(alphabets[0])
else:
    print('?')