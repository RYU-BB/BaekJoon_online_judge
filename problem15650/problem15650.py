def go(index):
    if index == m:
        print(*array)

    for i in range(1, n + 1):
        if check[i]:
            continue
        check[i] = True
        array.append(i)
        go(index + 1)

        array.pop()

        for j in range(i + 1, n + 1):
            check[j] = False


n, m = map(int, input().split())
check = [False for _ in range(n + 1)]
array = []

go(0)