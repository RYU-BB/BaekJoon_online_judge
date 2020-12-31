from sys import stdin

r = 1000001

prime_check = [True] * (r + 1)

for i in range(2, int(r ** 0.5)):
    if prime_check[i]:
        for j in range(i * 2, r, i):
            if prime_check[j]:
                prime_check[j] = False

test_num = int(stdin.readline())

for _ in range(test_num):
    num = int(stdin.readline())
    count = 0

    for i in range(2, num // 2 + 1):
        if prime_check[i] == True:
            if prime_check[num - i] == True:
                count += 1
    print(count)