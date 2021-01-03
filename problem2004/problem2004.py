def count_num(n, num):
    count = 0
    div_num = num
    while(n >= div_num):
        count = count + n // div_num
        div_num = div_num * num
    return count


n, m = map(int, input().split())

print(min(count_num(n, 5) - count_num(m, 5) - count_num(n-m, 5), count_num(n, 2) - count_num(m, 2) - count_num(n-m, 2)))