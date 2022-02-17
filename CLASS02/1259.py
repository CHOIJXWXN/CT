while True:
    number = input()
    flag = True
    if number == '0':
        break
    for i in range(len(number) // 2):
        if number[i] != number[-i - 1]:
            flag = False
    print('yes') if flag else print('no')