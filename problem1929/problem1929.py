r = 1000001

prime_check = [False] * 2 + [True] * (r + 1)

for i in range(2, int(r ** 0.5)):
    if prime_check[i]:
        for j in range(i * 2, r, i):
            if prime_check[j]:
                prime_check[j] = False

n, m = map(int, input().split())

for i in range(n, m + 1):
    if prime_check[i]:
        print(i)