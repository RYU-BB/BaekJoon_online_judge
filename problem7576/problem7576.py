import sys
from collections import deque

n, m = map(int, input().split())

points = [[-1, 0], [0, 1], [1, 0], [0, -1]]

map_list = [list(map(int, input().split())) for _ in range(m)]
queue = deque()
result = -2

for i in range(m):
    for j in range(n):
        if map_list[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()

    for point in points:
        temp_x = x + point[0]
        temp_y = y + point[1]
        if 0 <= temp_x < m and 0 <= temp_y < n and not map_list[temp_x][temp_y]:
            queue.append([temp_x, temp_y])
            map_list[temp_x][temp_y] = map_list[x][y] + 1

for i in map_list:
    for j in i:
        if not j:
            print(-1)
            sys.exit()
        result = max(result, j)

if result == -1:
    print(0)
else:
    print(result - 1)
