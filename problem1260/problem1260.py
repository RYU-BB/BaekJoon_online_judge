def dfs(index):
    dfs_check[index] = True
    print(index, end=' ')

    for i in range(1, n + 1):
        if not dfs_check[i] and node_list[index][i] == 1:
            dfs(i)


def bfs(index):
    queue = [index]
    bfs_check[index] = True
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, n + 1):
            if not bfs_check[i] and node_list[V][i] == 1:
                queue.append(i)
                bfs_check[i] = True


n, m, v = map(int, input().split())

node_list = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dfs_check = [False for _ in range(n + 1)]
bfs_check = [False for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    node_list[x][y] = node_list[y][x] = 1


dfs(v)
print()
bfs(v)
