house_n = int(input())
d = [[0, 0, 0] for _ in range(house_n)]

for i in range(house_n):
    color = list(map(int, input().split()))

    if not i:
        d[i] = color
    else:
        for j in range(3):
            if j == 0:
                d[i][j] = min(d[i - 1][1] + color[j], d[i - 1][2] + color[j])
            if j == 1:
                d[i][j] = min(d[i - 1][0] + color[j], d[i - 1][2] + color[j])
            if j == 2:
                d[i][j] = min(d[i - 1][0] + color[j], d[i - 1][1] + color[j])

print(min(d[house_n - 1]))
