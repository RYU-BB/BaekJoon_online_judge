def go(index, start):
    if index == m:
        print(*array)
        return

    for i in range(start, n + 1):
        check[i] = True
        array.append(i)
        go(index + 1, i)

        array.pop()
        check[i] = False


n, m = map(int, input().split())
check = [False for _ in range(n + 1)]
array = []

go(0, 1)