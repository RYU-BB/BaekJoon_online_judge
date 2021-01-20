import sys
input = sys.stdin.readline


def dfs(index, equation, add, sub, mul, div):
    global max_num, min_num
    if index == n:
        max_num = max(max_num, equation)
        min_num = min(min_num, equation)
        return

    if add:
        dfs(index + 1, equation + num_list[index], add - 1, sub, mul, div)
    if sub:
        dfs(index + 1, equation - num_list[index], add, sub - 1, mul, div)
    if mul:
        dfs(index + 1, equation * num_list[index], add, sub, mul - 1, div)
    if div:
        dfs(index + 1, -(-equation // num_list[index]) if equation < 0 else equation // num_list[index],
            add, sub, mul, div - 1)


n = int(input())
num_list = list(map(int, input().split()))
op_num = list(map(int, input(). split()))
max_num = -1000000001
min_num = 1000000001

dfs(1, num_list[0], op_num[0], op_num[1], op_num[2], op_num[3])
print(max_num)
print(min_num)
