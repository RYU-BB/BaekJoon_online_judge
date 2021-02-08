import math


def bfs(start_r, start_b, dirs, cnt):
    global min_cnt
    if cnt > 10:
        return
    dy, dx = dirs

    ry, rx = start_r
    by, bx = start_b

    r_cnt, b_cnt = 0, 0

    r_out, b_out = False, False

    next_y, next_x = ry + dy, rx + dx

    while 0 <= next_y < n and 0 <= next_x < m:
        r_cnt += 1

        if board[next_y][next_x] == 'O':
            r_out = True
            break
        elif board[next_y][next_x] == '#':
            start_r = (ry, rx)
            r_cnt -= 1
            break
        elif board[next_y][next_x] == '.':
            ry, rx = next_y, next_x
            next_y, next_x = ry + dy, rx + dx

    next_y, next_x = by + dy, bx + dx

    while 0 <= next_y < n and 0 <= next_x < m:
        b_cnt += 1

        if board[next_y][next_x] == 'O':
            b_out = True
            break
        elif board[next_y][next_x] == '#':
            start_b = (ry, rx)
            b_cnt -= 1
            break
        elif board[next_y][next_x] == '.':
            by, bx = next_y, next_x
            next_y, next_x = by + dy, bx + dx

    if start_r == start_b:
        if r_cnt > b_cnt:
            start_r = (ry - dy, rx - dx)
        else:
            start_b = (by - dy, bx - dx)

    if b_out:
        return

    elif r_out and not b_out:
        min_cnt = min(min_cnt, cnt)
        return
    elif r_cnt == b_cnt == 0:
        return
    else:
        for point in move_point:
            bfs(start_r, start_b, point, cnt + 1)


n, m = map(int, input().split())
board = list()
move_point = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for y in range(n):
    arr = list(input())
    board.append(arr)

    for x in range(m):
        if arr[x] == 'R':
            r = (y, x)
        if arr[x] == 'B':
            b = (y, x)

min_cnt = math.inf

for move in move_point:
    bfs(r, b, move, 1)

if min_cnt == math.inf:
    print(-1)
else:
    print(min_cnt)
