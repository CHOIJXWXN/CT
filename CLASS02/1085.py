x, y, w, h = map(int, input().split())
move_x = min(x, w-x)
move_y = min(y, h-y)
print(min(move_x, move_y))
