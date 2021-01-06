n = int(input())
d = [[0, 0] for _ in range(n + 1)]

d[1][0] = 0
d[1][1] = 1

for i in range(2, n + 1):
    for j in range(2):
        d[i][j] = 0

        if not j:
            d[i][j] += d[i - 1][0] + d[i - 1][1]
        else:
            d[i][j] += d[i - 1][0]

result = 0
result = d[n][0] + d[n][1]

print(result)