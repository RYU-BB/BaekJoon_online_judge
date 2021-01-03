max = 100001
d = [[0, 0, 0, 0] for _ in range(max)]
d[1], d[2], d[3] = [1, 0, 0], [0, 1, 0], [1, 1, 1]

for i in range(4, max):
    d[i][0] = (d[i - 1][1] + d[i - 1][2]) % 1000000009
    d[i][1] = (d[i - 2][0] + d[i - 2][2]) % 1000000009
    d[i][2] = (d[i - 3][0] + d[i - 3][1]) % 1000000009

test_num = int(input())

for _ in range(test_num):
    n = int(input())
    print(sum(d[n]) % 1000000009)