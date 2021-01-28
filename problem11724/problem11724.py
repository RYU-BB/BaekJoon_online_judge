def bfs(index):
    queue = [index]
    check_list[index] = True
    while queue:
        V = queue.pop(0)
        for node in node_list[V]:
            if not check_list[node]:
                queue.append(node)
                check_list[node] = True

    
n, m = map(int, input().split())

node_list = [[] for _ in range(n + 1)]
check_list = [False for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    node_list[x].append(y)
    node_list[y].append(x)

cnt = 0
for i in range(1, n + 1):
    if not check_list[i]:
        bfs(i)
        cnt += 1

print(cnt)