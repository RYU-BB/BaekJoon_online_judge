import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque([(first_num, "")])
    check_list[first_num] = True

    while queue:
        now, cmd = queue.popleft()
        if now == last_num:
            return cmd

        next_num = (now * 2) % max_num
        if not check_list[next_num]:
            check_list[next_num] = True
            queue.append((next_num, cmd + 'D'))

        next_num = now - 1
        if next_num == 0:
            next_num = 9999
        if not check_list[next_num]:
            check_list[next_num] = True
            queue.append((next_num, cmd + 'S'))

        next_num = int((now % 1000) * 10 + now / 1000)
        if not check_list[next_num]:
            check_list[next_num] = True
            queue.append((next_num, cmd + 'L'))

        next_num = int((now % 10) * 1000 + now / 10)
        if not check_list[next_num]:
            check_list[next_num] = True
            queue.append((next_num, cmd + 'R'))


test_num = int(input())
max_num = 10000

for _ in range(test_num):
    first_num, last_num = map(int, input().split())
    check_list = [False for _ in range(10000)]
    print(bfs())
