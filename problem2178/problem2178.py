n, m = map(int, input().split())

points = [[-1, 0], [0, 1], [1, 0], [0, -1]]

map_list = [list(input()) for _ in range(n)]

queue = [[0, 0]]
map_list[0][0] = 1

while queue:
    x, y = queue.pop(0)

    for point in points:
        temp_x = x + point[0]
        temp_y = y + point[1]
        if 0 <= temp_x < n and 0 <= temp_y < m and map_list[temp_x][temp_y] == '1':
            queue.append([temp_x, temp_y])
            map_list[temp_x][temp_y] = map_list[x][y] + 1

print(map_list[n - 1][m - 1])
