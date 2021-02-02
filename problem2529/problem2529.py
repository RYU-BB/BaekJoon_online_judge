def possible(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True


def solve(idx, s):
    global max_num, min_num
    if idx == n + 1:
        if not len(min_num):
            min_num = s
        else:
            max_num = s
        return
    for i in range(10):
        if not num_check[i]:
            if idx == 0 or possible(s[-1], str(i), sign[idx - 1]):
                num_check[i] = True
                solve(idx + 1, s + str(i))
                num_check[i] = False


n = int(input())
sign = list(input().split())
num = [i for i in range(10)]
num_check = [False for _ in range(10)]
max_num, min_num = "", ""

solve(0, "")
print(max_num)
print(min_num)