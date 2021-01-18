n, m = map(int, input().split())

impossible = [list(map(int, input().split())) for _ in range(m)]
cnt = 0

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            for combination in impossible:
                if combination == [i, j]:
                    cnt -= 1
                    break
                if combination == [j, k]:
                    cnt -= 1
                    break
                if combination == [i, k]:
                    cnt -= 1
                    break
            cnt += 1

print(cnt)
