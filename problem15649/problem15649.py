n, m = map(int, input().split())
num = 1

for i in range(m):
    num *= (n - i)

num_list = [i + 1 for i in range(n)]

for i in range(num):
    for j in range(m):
        print(num_list[j], end=" ")