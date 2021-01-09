test_n = int(input())

for _ in range(test_n):
    n = int(input())
    d = [[1] * 10] * 2 + [[0] * 10 for _ in range(n - 1)]

    for i in range(2, n + 1):
        for j in range(10):
            for k in range(j, -1, -1):
                d[i][j] += d[i - 1][k]

    print(sum(d[n]))
