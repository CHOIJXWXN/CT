# k층 n호
# def live(h, w):
#     if h == 0:
#         return w
#     if w == 1:
#         return 1
#     if w == 2:
#         return w + 1
#     else:
#         return live(h - 1, w) + live(h, w - 1)

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    floor_list = [i for i in range(1, n + 1)]
    for floor in range(k):
        for i in range(1, n):
            floor_list[i] += floor_list[i - 1]
    print(floor_list[-1])
        

    # print(live(k, n))