from sys import stdin

r = 1000001

prime_check = [True] * (r + 1)

for i in range(2, int(r ** 0.5)):
    if prime_check[i]:
        for j in range(i * 2, r, i):
            if prime_check[j]:
                prime_check[j] = False

while True:
    num = int(stdin.readline())

    if not num:
        break

    for i in range(2, r):
        if prime_check[i] == True:
            if prime_check[num - i] == True:
                print(num, "=", i, "+", num-i)
                break