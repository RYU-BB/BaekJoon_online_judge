n, k = map(int, input().split())
mod = 1000000000
d = [1]
d += [0] * n

for _ in range(1, k + 1):
    for idx in range(1, n + 1):
        d[idx] = (d[idx] + d[idx-1]) % mod

print(d[n])