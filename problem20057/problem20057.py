def left_move():
    global board
    global tornado_point
    global over_sand
    tornado_point[1] -= 1
    y = tornado_point[0]
    x = tornado_point[1]
    last_x = x - 1
    last_y = y
    sand = board[y][x]

    for point_info in left_move_list:
        temp_y = y + point_info[0]
        temp_x = x + point_info[1]
        sand -= int(board[y][x] * point_info[2])

        if temp_y > n - 1 or temp_y < 0 or temp_x > n - 1 or temp_x < 0:
            over_sand += int(board[y][x] * point_info[2])
            continue
        board[temp_y][temp_x] += int(board[y][x] * point_info[2])

    if last_y > n - 1 or last_y < 0 or last_x > n - 1 or last_x < 0:
        over_sand += sand
    else:
        board[last_y][last_x] += sand

    board[y][x] = 0


def right_move():
    global board
    global tornado_point
    global over_sand
    tornado_point[1] += 1
    y = tornado_point[0]
    x = tornado_point[1]
    last_x = x + 1
    last_y = y
    sand = board[y][x]

    for point_info in right_move_list:
        temp_y = y + point_info[0]
        temp_x = x + point_info[1]
        sand -= int(board[y][x] * point_info[2])

        if temp_y > n - 1 or temp_y < 0 or temp_x > n - 1 or temp_x < 0:
            over_sand += int(board[y][x] * point_info[2])
            continue
        board[temp_y][temp_x] += int(board[y][x] * point_info[2])

    if last_y > n - 1 or last_y < 0 or last_x > n - 1 or last_x < 0:
        over_sand += sand
    else:
        board[last_y][last_x] += sand

    board[y][x] = 0


def up_move():
    global board
    global tornado_point
    global over_sand
    tornado_point[0] -= 1
    y = tornado_point[0]
    x = tornado_point[1]
    last_y = y - 1
    last_x = x
    sand = board[y][x]

    for point_info in up_move_list:
        temp_y = y + point_info[0]
        temp_x = x + point_info[1]
        sand -= int(board[y][x] * point_info[2])

        if temp_y > n - 1 or temp_y < 0 or temp_x > n - 1 or temp_x < 0:
            over_sand += int(board[y][x] * point_info[2])
            continue
        board[temp_y][temp_x] += int(board[y][x] * point_info[2])

    if last_y > n - 1 or last_y < 0 or last_x > n - 1 or last_x < 0:
        over_sand += sand
    else:
        board[last_y][last_x] += sand

    board[y][x] = 0


def down_move():
    global board
    global tornado_point
    global over_sand
    tornado_point[0] += 1
    y = tornado_point[0]
    x = tornado_point[1]
    last_y = y + 1
    last_x = x
    sand = board[y][x]

    for point_info in down_move_list:
        temp_y = y + point_info[0]
        temp_x = x + point_info[1]
        sand -= int(board[y][x] * point_info[2])

        if temp_y > n - 1 or temp_y < 0 or temp_x > n - 1 or temp_x < 0:
            over_sand += int(board[y][x] * point_info[2])
            continue
        board[temp_y][temp_x] += int(board[y][x] * point_info[2])

    if last_y > n - 1 or last_y < 0 or last_x > n - 1 or last_x < 0:
        over_sand += sand
    else:
        board[last_y][last_x] += sand

    board[y][x] = 0


left_move_list = [(-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02),
                  (-1, -1, 0.1), (1, -1, 0.1), (1, 1, 0.01), (-1, 1, 0.01),
                  (0, -2, 0.05)]

right_move_list = [(-1, 0, 0.07), (-2, 0, 0.02), (1, 0, 0.07), (2, 0, 0.02),
                   (-1, 1, 0.1), (1, 1, 0.1), (1, -1, 0.01), (-1, -1, 0.01),
                   (0, 2, 0.05)]

up_move_list = [(0, -1, 0.07), (0, -2, 0.02), (0, 1, 0.07), (0, 2, 0.02),
                   (-1, 1, 0.1), (-1, -1, 0.1), (1, 1, 0.01), (1, -1, 0.01),
                   (-2, 0, 0.05)]

down_move_list = [(0, -1, 0.07), (0, -2, 0.02), (0, 1, 0.07), (0, 2, 0.02),
                   (1, 1, 0.1), (1, -1, 0.1), (-1, 1, 0.01), (-1, -1, 0.01),
                   (2, 0, 0.05)]

n = int(input())
board = [[int(x) for x in input().split()] for _ in range(n)]
over_sand = 0

tornado_point = [n // 2, n // 2]

for i in range(1, n // 2 + 1):
    left_move()
    for _ in range(i * 2 - 1):
        down_move()
    for _ in range(i * 2):
        right_move()
    for _ in range(i * 2):
        up_move()
    for _ in range(i * 2):
        left_move()

print(over_sand)
