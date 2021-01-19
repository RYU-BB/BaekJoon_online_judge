def stick(board, y, x):
    stick_ans1, stick_ans2 = 0, 0

    for i in range(4):
        try:
            stick_ans1 += board[y][x + i]
        except IndexError:
            stick_ans1 = 0
            break

    for i in range(4):
        try:
            stick_ans2 += board[y + i][x]
        except IndexError:
            stick_ans2 = 0
            break

    return max(stick_ans1, stick_ans2)


def rec(board, y, x):
    try:
        rec_ans = board[y][x] + board[y + 1][x] + board[y][x + 1] + board[y + 1][x + 1]
    except IndexError:
        rec_ans = 0

    return rec_ans


def j_mino(board, y, x):
    try:
        j_ans1 = board[y][x] + board[y + 1][x] + board[y + 2][x] + board[y + 2][x + 1]
    except IndexError:
        j_ans1 = 0

    try:
        j_ans2 = board[y][x + 1] + board[y + 1][x + 1] + board[y + 2][x + 1] + board[y + 2][x]
    except IndexError:
        j_ans2 = 0

    try:
        j_ans3 = board[y][x] + board[y][x + 1] + board[y + 1][x] + board[y + 2][x]
    except IndexError:
        j_ans3 = 0

    try:
        j_ans4 = board[y][x] + board[y][x + 1] + board[y + 1][x + 1] + board[y + 2][x + 1]
    except IndexError:
        j_ans4 = 0

    return max(j_ans1, j_ans2, j_ans3, j_ans4)


def l_mino(board, y, x):
    try:
        l_ans1 = board[y][x] + board[y][x + 1] + board[y + 1][x] + board[y][x + 2]
    except IndexError:
        l_ans1 = 0

    try:
        l_ans2 = board[y + 1][x] + board[y + 1][x + 1] + board[y + 1][x + 2] + board[y][x + 2]
    except IndexError:
        l_ans2 = 0

    try:
        l_ans3 = board[y][x] + board[y + 1][x] + board[y + 1][x + 1] + board[y + 1][x + 2]
    except IndexError:
        l_ans3 = 0

    try:
        l_ans4 = board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y + 1][x + 2]
    except IndexError:
        l_ans4 = 0

    return max(l_ans1, l_ans2, l_ans3, l_ans4)


def t_mino(board, y, x):
    try:
        t_ans1 = board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y + 1][x + 1]
    except IndexError:
        t_ans1 = 0

    try:
        t_ans2 = board[y][x + 1] + board[y + 1][x] + board[y + 1][x + 1] + board[y + 1][x + 2]
    except IndexError:
        t_ans2 = 0

    try:
        t_ans3 = board[y][x] + board[y + 1][x] + board[y + 2][x] + board[y + 1][x + 1]
    except IndexError:
        t_ans3 = 0

    try:
        t_ans4 = board[y][x + 1] + board[y + 1][x] + board[y + 1][x + 1] + board[y + 2][x + 1]
    except IndexError:
        t_ans4 = 0

    return max(t_ans1, t_ans2, t_ans3, t_ans4)


def s_mino(board, y, x):
    try:
        s_ans1 = board[y][x + 1] + board[y + 1][x] + board[y + 1][x + 1] + board[y + 2][x]
    except IndexError:
        s_ans1 = 0

    try:
        s_ans2 = board[y][x] + board[y + 1][x] + board[y + 1][x + 1] + board[y + 2][x + 1]
    except IndexError:
        s_ans2 = 0

    try:
        s_ans3 = board[y + 1][x] + board[y + 1][x + 1] + board[y][x + 1] + board[y][x + 2]
    except IndexError:
        s_ans3 = 0

    try:
        s_ans4 = board[y][x] + board[y][x + 1] + board[y + 1][x + 1] + board[y + 1][x + 2]
    except IndexError:
        s_ans4 = 0

    return max(s_ans1, s_ans2, s_ans3, s_ans4)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        result = max(result,
                     stick(board, i, j),
                     j_mino(board, i, j),
                     l_mino(board, i, j),
                     t_mino(board, i, j),
                     s_mino(board, i, j),
                     rec(board, i, j))

print(result)
