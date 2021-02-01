import sys
sys.setrecursionlimit(10 ** 7)


def dfs(j, i):
    sea[j][i] = 0
    for point in points:
        temp_i = i + point[0]
        temp_j = j + point[1]
        if temp_i < 0 or temp_i >= w or temp_j < 0 or temp_j >= h:
            continue
        if sea[temp_j][temp_i] == 1:
            dfs(temp_j, temp_i)


points = [[-1, 0], [0, 1], [1, 0], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    sea = [list(map(int, input().split())) for _ in range(h)]

    count = 0
    for i in range(w):
        for j in range(h):
            if sea[j][i] == 1:
                dfs(j, i)
                count += 1

    print(count)
