def bfs():
    queue = [1]
    bfs_check[1] = True
    global count

    while queue:
        V = queue.pop(0)

        for node in node_list[V]:
            if not bfs_check[node]:
                queue.append(node)
                bfs_check[node] = True
                count += 1


com_num = int(input())
line = int(input())
node_list = [[] for _ in range(com_num + 1)]
bfs_check = [False for _ in range(com_num + 1)]
count = 0

for _ in range(line):
    a, b = map(int, input().split())
    node_list[a].append(b)
    node_list[b].append(a)

bfs()
print(count)