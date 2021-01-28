import sys


def dfs(index, depth):
    if depth == 4:
        print(1)
        sys.exit()
    for i in friends[index]:
        if not dfs_check[i]:
            dfs_check[i] = True
            dfs(i, depth + 1)
            dfs_check[i] = False


n, m = map(int, input().split())

friends = [[] for _ in range(n)]
dfs_check = [False for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    friends[x].append(y)
    friends[y].append(x)

for i in range(n):
    dfs_check[i] = True
    dfs(i, 0)
    dfs_check[i] = False

print(0)