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
    rec_ans = 0

    for i in range(2):
        try:
            if i == 1:
                rec_ans = board[y + i][x + i] + board[y + i][x] + board[y][x + i]
            else:
                rec_ans += board[y + i][x + i]
        except IndexError:
            rec_ans = 0
            break

    return rec_ans


def j_mino(board, y, x):
    j_ans1, j_ans2, j_ans3, j_ans4 = 0, 0, 0, 0

    for i in range(3):
        try:
            if i == 0:
                j_ans1 += board[y][x] + board[y + 1][x]
            else:
                j_ans1 += board[y][x + i]
        except IndexError:
            j_ans1 = 0
            break

    for i in range(3):
        try:
            if i == 2:
                j_ans2 += board[y + 1][x + i] + board[y][x + i]
            else:
                j_ans2 += board[y + 1][x + i]
        except IndexError:
            j_ans2 = 0
            break

    for i in range(3):
        try:
            if i == 0:
                j_ans3 += board[y][x] + board[y + 1][x]
            else:
                j_ans3 += board[y + 1][x + i]
        except IndexError:
            j_ans3 = 0
            break

    for i in range(3):
        try:
            if i == 2:
                j_ans4 += board[y][x + i] + board[y + 1][x + i]
            else:
                j_ans4 += board[y][x + i]
        except IndexError:
            j_ans4 = 0
            break

    return max(j_ans1, j_ans2, j_ans3, j_ans4)


def l_mino(board, y, x):
    l_ans1, l_ans2, l_ans3, l_ans4 = 0, 0, 0, 0

    for i in range(3):
        try:
            if i == 0:
                l_ans1 += board[y][x] + board[y][x + 1]
            else:
                l_ans1 += board[y + i][x]
        except IndexError:
            l_ans1 = 0
            break

    for i in range(3):
        try:
            if i == 2:
                l_ans2 += board[y + i][x] + board[y + i][x + 1]
            else:
                l_ans2 += board[y + i][x]
        except IndexError:
            l_ans2 = 0
            break

    for i in range(3):
        try:
            if i == 0:
                l_ans3 += board[y][x] + board[y][x + 1]
            else:
                l_ans3 += board[y + i][x + 1]
        except IndexError:
            l_ans3 = 0
            break

    for i in range(3):
        try:
            if i == 2:
                l_ans4 += board[y + i][x] + board[y + i][x + 1]
            else:
                l_ans4 += board[y + i][x + 1]
        except IndexError:
            l_ans4 = 0
            break

    return max(l_ans1, l_ans2, l_ans3, l_ans4)


def t_mino(board, y, x):
    t_ans1, t_ans2, t_ans3, t_ans4 = 0, 0, 0, 0

    for i in range(3):
        try:
            if i == 1:
                t_ans1 += board[y][x + i] + board[y + i][x + i]
            else:
                t_ans1 += board[y][x + i]
        except IndexError:
            t_ans1 = 0
            break

    for i in range(3):
        try:
            if i == 1:
                t_ans2 += board[y][x + i] + board[y + i][x + i]
            else:
                t_ans2 += board[y + 1][x + i]
        except IndexError:
            t_ans2 = 0
            break

    for i in range(3):
        try:
            if i == 1:
                t_ans3 += board[y + i][x] + board[y + i][x + i]
            else:
                t_ans3 += board[y + i][x]
        except IndexError:
            t_ans3 = 0
            break

    for i in range(3):
        try:
            if i == 2:
                t_ans4 += board[y + i][x] + board[y + i][x + i]
            else:
                t_ans4 += board[y + i][x + 1]
        except IndexError:
            t_ans4 = 0
            break

    return max(t_ans1, t_ans2, t_ans3, t_ans4)


def s_mino(board, y, x):
    s_ans1, s_ans2, s_ans3, s_ans4 = 0, 0, 0, 0

    for i in range(3):
        try:
            if i == 0:
                s_ans1 += board[y][x + 1]
            elif i == 2:
                s_ans1 += board[y + i][x]
            else:
                s_ans1 += board[y + i][x + i] + board[y + i][x]
        except IndexError:
            s_ans1 = 0
            break

    for i in range(3):
        try:
            if i == 0:
                s_ans2 += board[y][x]
            elif i == 2:
                s_ans2 += board[y + i][x + 1]
            else:
                s_ans2 += board[y + i][x + i] + board[y + i][x]
        except IndexError:
            s_ans2 = 0
            break

    for i in range(3):
        try:
            if i == 0:
                s_ans3 += board[y + 1][x]
            elif i == 2:
                s_ans3 += board[y][x + i]
            else:
                s_ans3 += board[y][x + i] + board[y + 1][x + i]
        except IndexError:
            s_ans3 = 0
            break

    for i in range(3):
        try:
            if i == 0:
                s_ans4 += board[y][x]
            elif i == 2:
                s_ans4 += board[y + 1][x + i]
            else:
                s_ans4 += board[y][x + i] + board[y + 1][x + i]
        except IndexError:
            s_ans4 = 0
            break

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
