def go(index):
    if index == m:
        print(*array)
        return

    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        array.append(num_list[i])
        go(index + 1)

        array.pop()
        check[i] = False


n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
check = [False for _ in range(n + 1)]
array = []

go(0)