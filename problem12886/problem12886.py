from collections import deque, defaultdict


def bfs():
    queue = deque([(a, b, c)])
    visit_check[(a, b, c)] = True

    while queue:
        temp_a, temp_b, temp_c = queue.popleft()
        if temp_a == temp_b == temp_c:
            return 1
        for x, y in ((temp_a, temp_b), (temp_a, temp_c), (temp_b, temp_c)):
            if x == y:
                continue
            elif x < y:
                y -= x
                x += x
            elif x > y:
                x -= y
                y += y
            z = total_num - x - y
            if not visit_check[(x, y, z)]:
                visit_check[(x, y, z)] = True
                queue.append((x, y, z))

    return 0


a, b, c = map(int, input().split())
visit_check = defaultdict(bool)
total_num = a + b + c

print(0) if total_num % 3 else print(bfs())
