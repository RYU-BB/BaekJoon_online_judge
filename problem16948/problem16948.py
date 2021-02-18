import sys


def bfs():
    queue = list()
    queue.append((start_y, start_x))

    while queue:
        now_y, now_x = queue.pop(0)
        cnt = chess_board[now_y][now_x]

        if now_y == goal_y and now_x == goal_x:
            print(cnt)
            sys.exit()

        for move_y, move_x in move_list:
            next_y = now_y + move_y
            next_x = now_x + move_x

            if 0 <= next_y < chess_board_size and 0 <= next_x < chess_board_size:
                if not chess_board[next_y][next_x]:
                    chess_board[next_y][next_x] = cnt + 1
                    queue.append((next_y, next_x))


chess_board_size = int(input())
chess_board = [[0 for _ in range(chess_board_size)] for _ in range(chess_board_size)]
start_y, start_x, goal_y, goal_x = map(int, input().split())

move_list = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

bfs()
print(-1)
