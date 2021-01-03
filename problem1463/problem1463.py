n = int(input())
d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1

    if not i % 2 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1

    if not i % 3 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1

print(d[n])