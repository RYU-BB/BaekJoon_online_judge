test_num = int(input())
max = 1000001
d = [0] * max
d[0], d[1], d[2] = 1, 1, 2

for i in range(3, max):
    d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % 1000000009

for _ in range(test_num):
    n = int(input())
    print(d[n])
