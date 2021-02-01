def dfs(i, j):
    global count
    map[i][j] = '0'
    count += 1
    for point in points:
        temp_i = i + point[0]
        temp_j = j + point[1]
        if temp_i < 0 or temp_i >= n or temp_j < 0 or temp_j >= n:
            continue
        if map[temp_i][temp_j] == '1':
            dfs(temp_i, temp_j)


n = int(input())

map = [list(input()) for _ in range(n)]
apt = list()
points = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for i in range(n):
    for j in range(n):
        if map[i][j] == '1':
            count = 0
            dfs(i, j)
            apt.append(count)

print(len(apt))
apt.sort()
for i in apt:
    print(i)

