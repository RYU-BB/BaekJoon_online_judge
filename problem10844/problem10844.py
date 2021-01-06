mod = 1000000000
n = int(input())
d = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        d[i][j] = 0
        if (j - 1) >= 0:
            d[i][j] += d[i - 1][j - 1]
        if (j + 1) <= 9:
            d[i][j] += d[i - 1][j + 1];
        d[i][j] %= mod

result = 0
for i in range(0, 10):
    result += d[n][i]

print(result % mod)