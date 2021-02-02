from collections import deque
import sys
input = sys.stdin.readline

queen_move = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

test_n = int(input())

for _ in range(test_n):
    l = int(input())
    chess_board = [[0 for _ in range(l)] for _ in range(l)]

    first_row, first_col = map(int, input().split())
    goal_row, goal_col = map(int, input().split())
    queue = deque()
    queue.append([first_row, first_col])

    while queue:
        row, col = queue.popleft()
        if row == goal_row and col == goal_col:
            print(chess_board[goal_row][goal_col])
            break

        for move in queen_move:
            _row = row + move[0]
            _col = col + move[1]

            if _row < 0 or _row >= l or _col < 0 or _col >= l:
                continue
            if not chess_board[_row][_col]:
                chess_board[_row][_col] = chess_board[row][col] + 1
                queue.append([_row, _col])