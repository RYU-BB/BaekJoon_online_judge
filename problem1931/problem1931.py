n = int(input())
conference_time = list()
count = 1

for _ in range(n):
    start_time, end_time = map(int, input().split())
    conference_time.append((start_time, end_time))

conference_time.sort(key=lambda x: (x[1], x[0]))

conference_end = conference_time[0][1]

for i in range(1, n):
    if conference_time[i][0] >= conference_end:
        count += 1
        conference_end = conference_time[i][1]

print(count)
